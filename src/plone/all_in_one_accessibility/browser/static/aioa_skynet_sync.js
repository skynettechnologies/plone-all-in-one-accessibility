/*
 * Browser-side Skynet API calls for the "All in One Accessibility Setting"
 * add/edit form.
 *
 * Ported from the Skynet plone module, which makes both calls from the
 * browser (never from the server):
 *
 *   static/src/js/aioa_register_domain.js -> registerDomain()
 *   static/src/js/aioa_save_sync_patch.js -> syncWidgetSettings()
 *
 * Why the browser and not Zope: the calls then leave from the editor's own
 * IP and show up in DevTools -> Network, instead of coming from one server
 * IP that Skynet can rate-limit (HTTP 429) for every site behind it.
 *
 * Flow
 * ----
 *  0. Every time the form opens: a static upgrade notice (Pro/10-day-trial
 *     message + cache note) is inserted at the very top, same copy as the
 *     plone module's banner. See insertUpgradeNotice().
 *  1. Every time the form opens: the same EU/non-EU IP lookup add-user-domain
 *     uses is run once, and its result is written straight into the hidden
 *     no_required_eu field (see setNoRequiredEuField()) so that field always
 *     saves whatever CDN Skynet actually registered this domain under --
 *     there is no manual "non-EU CDN" choice on the form any more.
 *  2. add-user-domain itself: once per domain per browser (localStorage
 *     flag), at most MAX_REGISTER_ATTEMPTS failures.
 *  3. When Save was just clicked: a short-lived marker was stored in
 *     sessionStorage before the redirect; if it's still fresh and the
 *     reloaded form shows no validation errors, widget-setting-update-
 *     platform is called first with the values now shown in the form --
 *     i.e. the values that were just saved. (The plone module does the
 *     same: its hook runs after the record has been saved.) This runs
 *     *before* step 4 so the read-back below reflects the save, not the
 *     dashboard's pre-save state.
 *  4. widget-settings is fetched (read-only) and used for two things:
 *     the widget token is saved into the hidden aioa_token field
 *     (applyWidgetToken()), and -- mirroring the plone module's
 *     fetchApiResponse()/populateSettings() -- the current color,
 *     position and icon/size values are written into the form
 *     (applyDashboardSettings()), so changes made directly on the
 *     Skynet/ADA dashboard show up here too, not just changes made from
 *     this form.
 *
 * Only loaded on the settings object's own add/edit views, see
 * browser/viewlets.py (AccessibilityCSSViewlet).
 */
(function () {
  'use strict';

  var ADD_USER_DOMAIN_URL = 'https://ada.skynettechnologies.us/api/add-user-domain';
  var WIDGET_SETTING_UPDATE_URL =
    'https://ada.skynettechnologies.us/api/widget-setting-update-platform';
  var WIDGET_SETTINGS_URL = 'https://ada.skynettechnologies.us/api/widget-settings';

  // Same notice + link the plone/plone modules show above the settings
  // form (see the plone module's aioa_accessibility.js insertNoticeBanner).
  var PRO_TRIAL_URL = 'https://ada.skynettechnologies.us/trial-subscription';

  var MAX_REGISTER_ATTEMPTS = 3;
  var LOCAL_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0'];

  var PENDING_KEY = 'aioa_sync_pending_v1';
  var PENDING_TTL_MS = 2 * 60 * 1000;

  // ---------------------------------------------------------------- helpers

  function storageGet(store, key) {
    try { return store.getItem(key); } catch (e) { return null; }
  }
  function storageSet(store, key, value) {
    try { store.setItem(key, value); } catch (e) { /* private mode etc. */ }
  }
  function storageRemove(store, key) {
    try { store.removeItem(key); } catch (e) { /* ignore */ }
  }

  /*
   * The key Skynet stores a site's settings under: "https://" + hostname,
   * no port, no matter what scheme/port the page is served on. Same rule
   * as aioa_utils.get_canonical_domain() on the Python side.
   */
  function canonicalDomain() {
    return 'https://' + window.location.hostname;
  }

  function getForm() {
    var probe = document.getElementById('form-widgets-aioa_color') ||
      document.getElementById('form-widgets-aioa_place');
    return probe ? probe.closest('form') : null;
  }

  // ------------------------------------------------------- form-value access

  function field(name) {
    return document.getElementById('form-widgets-' + name);
  }

  function textValue(name, fallback) {
    var el = field(name);
    var value = el ? String(el.value || '').trim() : '';
    if (!value) {
      // Radio-button rendering of a Choice field.
      var radio = document.querySelector('input[name="form.widgets.' + name + ':list"]:checked');
      value = radio ? String(radio.value || '').trim() : '';
    }
    return value || fallback;
  }

  function boolValue(name) {
    var el = document.getElementById('form-widgets-' + name + '-0');
    return !!(el && el.checked);
  }

  function intValue(name, fallback) {
    var el = field(name);
    var n = el ? parseInt(el.value, 10) : NaN;
    return isNaN(n) ? fallback : n;
  }

  /*
   * Same payload as the plone module's _aioaSyncWidgetSettings().
   */
  function buildPayload() {
    var precise = boolValue('enable_widget_icon_position');
    var customSize = boolValue('enable_icon_custom_size');

    var payload = {
      u: canonicalDomain(),
      widget_color_code: textValue('aioa_color', '420083').replace(/^#/, ''),
      is_widget_custom_position: precise ? 1 : 0,
      is_widget_custom_size: customSize ? 1 : 0,
      widget_icon_type: textValue('aioa_icon_type', 'aioa-icon-type-1'),
      widget_size: textValue('aioa_size', 'regular') === 'oversize' ? 1 : 0
    };

    if (!precise) {
      payload.widget_position_top = null;
      payload.widget_position_right = null;
      payload.widget_position_bottom = null;
      payload.widget_position_left = null;
      payload.widget_position = textValue('aioa_place', 'bottom_right');
    } else {
      var pos = { top: null, right: null, bottom: null, left: null };
      var right = intValue('to_the_right_px', 20);
      var bottom = intValue('to_the_bottom_px', 20);

      if (textValue('to_the_right', 'to_the_left') === 'to_the_left') {
        pos.left = right;
      } else {
        pos.right = right;
      }
      if (textValue('to_the_bottom', 'to_the_bottom') === 'to_the_top') {
        pos.top = bottom;
      } else {
        pos.bottom = bottom;
      }
      payload.widget_position_top = pos.top;
      payload.widget_position_right = pos.right;
      payload.widget_position_bottom = pos.bottom;
      payload.widget_position_left = pos.left;
      payload.widget_position = '';
    }

    if (!customSize) {
      payload.widget_icon_size = textValue('aioa_icon_size', 'aioa-default-icon');
      payload.widget_icon_size_custom = 0;
    } else {
      payload.widget_icon_size = '';
      payload.widget_icon_size_custom = intValue('aioa_size_value', 50);
    }

    return payload;
  }

  // ------------------------------------------------------------ user feedback

  function notify(message, kind) {
    var form = getForm();
    if (!form) { return; }

    var old = document.getElementById('aioa-sync-message');
    if (old) { old.remove(); }

    var box = document.createElement('div');
    box.id = 'aioa-sync-message';
    box.className = 'portalMessage alert alert-' + kind + ' ' + kind;
    box.setAttribute('role', kind === 'warning' ? 'alert' : 'status');
    box.textContent = message;
    form.insertBefore(box, form.firstChild);
  }

  // ------------------------------------------------- add-user-domain (plone #1)

  async function detectNonEu() {
    // Same approach as the plone module: default to non-EU (1) unless the
    // IP lookup explicitly says EU.
    try {
      var resp = await fetch('https://ipapi.co/json/');
      if (resp.ok) {
        var data = await resp.json();
        return data.in_eu ? 0 : 1;
      }
    } catch (err) {
      console.warn('AIOA: EU detection failed, defaulting to non-EU', err);
    }
    return 1;
  }

  function utf8ToBase64(str) {
    return btoa(unescape(encodeURIComponent(str)));
  }

  /*
   * CDN selection is no longer a manual "Serve widget from the non-EU CDN"
   * checkbox on the settings form (see IAllInOneAccessibilitySetting.
   * no_required_eu, form.mode 'hidden') -- a manual toggle could drift out
   * of sync with what add-user-domain actually registered for this domain
   * with Skynet, and a mismatch there is exactly what produced widget
   * script/rendering errors. Instead this writes the same EU/non-EU
   * detection add-user-domain uses into the hidden field's own input, every
   * time the form loads, so whatever gets saved always matches Skynet's
   * own registration for this domain.
   */
  function setNoRequiredEuField(noRequiredEu) {
    // z3c.form's 'hidden' mode renders a Bool field as
    // <input type="hidden" id="form-widgets-no_required_eu" ...>, carrying
    // the value that will be POSTed back on Save.
    var hidden = document.getElementById('form-widgets-no_required_eu');
    if (hidden) {
      hidden.value = noRequiredEu ? 'true' : 'false';
      return;
    }
    // Defensive fallback in case the widget is ever rendered as a visible
    // checkbox again (e.g. form.mode reverted).
    var checkbox = document.getElementById('form-widgets-no_required_eu-0');
    if (checkbox) {
      checkbox.checked = !!noRequiredEu;
    }
  }

  async function registerDomain(noRequiredEu) {
    var domain = canonicalDomain();
    var hostname = window.location.hostname;
    var registeredKey = 'aioa_domain_registered_v2_' + domain;
    var attemptsKey = 'aioa_domain_register_attempts_v2_' + domain;

    if (LOCAL_HOSTS.indexOf(hostname) !== -1) {
      return; // dev/local instance: nothing Skynet can register
    }
    if (storageGet(window.localStorage, registeredKey)) {
      return; // already confirmed registered from this browser
    }
    var attempts = parseInt(storageGet(window.localStorage, attemptsKey) || '0', 10);
    if (attempts >= MAX_REGISTER_ATTEMPTS) {
      return; // gave up quietly after a few failed page loads
    }

    // Field-for-field the same as the plone module, "platform" aside.
    // "website" must be base64-encoded.
    var payload = new URLSearchParams({
      name: hostname,
      email: 'no-reply@' + hostname,
      company_name: '',
      website: utf8ToBase64(domain),
      package_type: 'basic',
      start_date: new Date().toISOString(),
      end_date: '',
      price: '',
      discount_price: '0',
      platform: 'Plone',
      api_key: '',
      is_trial_period: '',
      is_free_widget: '1',
      bill_address: '',
      country: '',
      state: '',
      city: '',
      post_code: '',
      transaction_id: '',
      subscr_id: '',
      payment_source: '',
      no_required_eu: String(noRequiredEu)
    });

    try {
      var response = await fetch(ADD_USER_DOMAIN_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: payload.toString()
      });
      if (response.ok) {
        storageSet(window.localStorage, registeredKey, '1');
        storageRemove(window.localStorage, attemptsKey);
      } else {
        storageSet(window.localStorage, attemptsKey, String(attempts + 1));
        // Skynet answers a domain it already knows with a bare 500, so a
        // failure here is not necessarily a problem -- warn, don't alarm.
        console.warn(
          'AIOA: add-user-domain responded', response.status,
          '(attempt ' + (attempts + 1) + '/' + MAX_REGISTER_ATTEMPTS + ')'
        );
      }
    } catch (err) {
      storageSet(window.localStorage, attemptsKey, String(attempts + 1));
      // Usually a missing CORS header on Skynet's error path.
      console.warn(
        'AIOA: add-user-domain call failed', err,
        '(attempt ' + (attempts + 1) + '/' + MAX_REGISTER_ATTEMPTS + ')'
      );
    }
  }

  function resetRegistration() {
    var domain = canonicalDomain();
    storageRemove(window.localStorage, 'aioa_domain_registered_v2_' + domain);
    storageRemove(window.localStorage, 'aioa_domain_register_attempts_v2_' + domain);
  }

  // ------------------------------------- widget-setting-update-platform (plone #2)

  async function syncWidgetSettings() {
    var payload = buildPayload();
    console.log('AIOA: sending widget-setting-update-platform', payload);

    try {
      var response = await fetch(WIDGET_SETTING_UPDATE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      var bodyText = await response.text().catch(function () { return '<unreadable body>'; });
      console.log('AIOA: widget-setting-update-platform response', response.status, bodyText);

      if (response.ok) {
        notify('Widget settings saved Successfully ', 'success');
      } else if (response.status === 429) {
        notify(
          'Widget settings were saved, but Skynet is rate-limiting requests ' +
          '(HTTP 429). Wait a few minutes, then press Save again.',
          'warning'
        );
      } else {
        notify(
          'Widget settings were saved, but syncing them to Skynet failed (HTTP ' +
          response.status + '). Check the browser console for details.',
          'warning'
        );
      }
      return response.ok;
    } catch (err) {
      // Most likely a CORS or network problem -- see the Network tab.
      console.error('AIOA: widget-setting-update-platform call failed', err);
      notify(
        'Widget settings were saved, but the sync request could not reach ' +
        'Skynet. Check the browser console for details.',
        'warning'
      );
      return false;
    }
  }

  // ------------------------------------------------------- widget-settings

  /*
   * Fetches this site's current widget configuration from Skynet (the
   * same "ADA" backend add-user-domain and widget-setting-update-platform
   * talk to). Used for two things: saving the widget token into the
   * hidden aioa_token field (applyWidgetToken), and -- mirroring the
   * plone module's fetchApiResponse()/populateSettings() -- writing
   * the current position/color/icon/size values into the form so
   * changes made directly on the Skynet/ADA dashboard show up here too,
   * not just changes made from this form. See applyDashboardSettings().
   *
   * Same request shape as the plone module's fetchApiResponse(): POST,
   * JSON body {"website_url": <host>}. A plain GET with ?u=...&platform=
   * (the previous approach here) came back as an HTML error page rather
   * than JSON -- this endpoint apparently only accepts POST.
   *
   * Like the plone module, the real payload is nested under "Data";
   * unwrap it here so callers work with the same flat field names
   * (widget_color_code, widget_position, etc.) plone's populateSettings()
   * uses. Some deployments may answer with a flat body instead, so fall
   * back to the raw JSON if "Data" isn't present.
   */
  async function fetchWidgetSettings() {
    try {
      var response = await fetch(WIDGET_SETTINGS_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ website_url: window.location.host })
      });
      if (!response.ok) {
        console.warn('AIOA: widget-settings responded', response.status);
        return null;
      }
      var json = await response.json();
      if (json && json.Data && Object.keys(json.Data).length > 0) {
        return json.Data;
      }
      return json || null;
    } catch (err) {
      console.warn('AIOA: widget-settings call failed', err);
      return null;
    }
  }

  function truthy01(value) {
    return value === true || value === 1 || value === '1';
  }

  /*
   * Writes Skynet's current widget configuration into the form fields --
   * the Plone equivalent of the plone module's populateSettings(). data
   * may be null (widget-settings failed, or came back empty); then this
   * is a no-op, same as plone's "Invalid API response" branch.
   */
  function applyDashboardSettings(data) {
    if (!data) { return; }
    var form = getForm();
    if (!form) { return; }

    function setValue(name, value) {
      if (value === undefined || value === null || value === '') { return; }
      var el = document.getElementById('form-widgets-' + name);
      if (el) { el.value = value; }
    }

    function setChecked(name, checked) {
      var el = document.getElementById('form-widgets-' + name + '-0');
      if (!el) { return; }
      el.checked = !!checked;
      // Deliberately NOT a dispatched 'change' event. custom.js's own
      // checkbox listener treats any 'change' -- including one fired
      // programmatically here -- as the person clicking the checkbox,
      // and responds by resetting the offset/size fields to their
      // schema defaults when the box ends up unchecked. That is correct
      // for a real click, but not here: this only needs to keep the
      // show/hide state in sync with whatever value was just written,
      // so it calls custom.js's visibility update directly (see below)
      // instead of going through 'change'.
    }

    if (typeof data.widget_color_code === 'string' && data.widget_color_code) {
      setValue('aioa_color', data.widget_color_code.trim().replace(/^#/, ''));
    }

    // buildPayload() above sends widget_size as 0/1; accept that, the
    // schema's own 'regular'/'oversize' tokens, or nothing back at all.
    if (data.widget_size === 1 || data.widget_size === '1') {
      setValue('aioa_size', 'oversize');
    } else if (data.widget_size === 0 || data.widget_size === '0') {
      setValue('aioa_size', 'regular');
    } else if (data.widget_size === 'oversize' || data.widget_size === 'regular') {
      setValue('aioa_size', data.widget_size);
    }

    setValue('aioa_icon_type', data.widget_icon_type);

    var customPosition = truthy01(data.is_widget_custom_position);
    var customSize = truthy01(data.is_widget_custom_size);

    setChecked('enable_widget_icon_position', customPosition);
    setChecked('enable_icon_custom_size', customSize);

    if (customPosition) {
      if (data.widget_position_right != null && data.widget_position_right !== '') {
        setValue('to_the_right_px', data.widget_position_right);
        setValue('to_the_right', 'to_the_right');
      } else if (data.widget_position_left != null && data.widget_position_left !== '') {
        setValue('to_the_right_px', data.widget_position_left);
        setValue('to_the_right', 'to_the_left');
      }
      if (data.widget_position_bottom != null && data.widget_position_bottom !== '') {
        setValue('to_the_bottom_px', data.widget_position_bottom);
        setValue('to_the_bottom', 'to_the_bottom');
      } else if (data.widget_position_top != null && data.widget_position_top !== '') {
        setValue('to_the_bottom_px', data.widget_position_top);
        setValue('to_the_bottom', 'to_the_top');
      }
    } else {
      setValue('aioa_place', data.widget_position);
    }

    if (customSize) {
      setValue('aioa_size_value', data.widget_icon_size_custom);
    } else {
      setValue('aioa_icon_size', data.widget_icon_size);
    }

    // Rebuild the icon-type / icon-size visual pickers (custom.js) so
    // they highlight whatever value was just written into the
    // underlying <select>s, instead of whatever was selected on load.
    if (typeof window.enhanceIconTypeSelector === 'function') {
      window.enhanceIconTypeSelector();
    }

    // Show/hide the right group of fields for the checkbox states just
    // set above -- the non-destructive counterpart of the 'change' event
    // setChecked() no longer dispatches (see its comment).
    if (typeof window.AIOA_updateVisibility === 'function') {
      window.AIOA_updateVisibility();
    }
  }

  function escapeHtml(value) {
    var div = document.createElement('div');
    div.textContent = String(value == null ? '' : value);
    return div.innerHTML;
  }

  function escapeAttr(value) {
    // Safe to use inside a double-quoted HTML attribute: escapeHtml already
    // turns '&', '<', '>' into entities; '"' is the one it leaves alone.
    return escapeHtml(value).replace(/"/g, '&quot;');
  }

  /*
   * Static upgrade notice at the very top of the form -- the Plone
   * equivalent of the plone module's insertNoticeBanner(): a fixed
   * message pointing editors at the paid Pro widget, plus a note that
   * front-end changes are not instant. Unlike the account panel below
   * it, this does not depend on any Skynet API call, so it is inserted
   * immediately on load and stays even if widget-settings fails.
   */
  function insertUpgradeNotice() {
    var form = getForm();
    if (!form) { return null; }

    var existing = document.getElementById('aioa-upgrade-notice');
    if (existing) { return existing; }

    var notice = document.createElement('div');
    notice.id = 'aioa-upgrade-notice';
    notice.className = 'aioa-upgrade-notice';
    notice.innerHTML =
      '<p class="aioa-upgrade-notice-message">' +
      '<strong>NOTE:</strong> Currently, All in One Accessibility is dedicated to ' +
      'enhancing accessibility specifically for websites and online stores. ' +
      'Please upgrade to the full version of ' +
      '<a href="' + escapeAttr(PRO_TRIAL_URL) + '" target="_blank" rel="noopener noreferrer">' +
      'All in One Accessibility Pro with 10 days free trial</a>.' +
      '</p>' +
      '<p class="aioa-upgrade-notice-cache-note">' +
      'It may take a few seconds for changes to appear on your website. If you ' +
      'don\u2019t see the changes, try clearing your browser cache or checking in ' +
      'a private browsing window.' +
      '</p>';

    form.insertBefore(notice, form.firstChild);
    return notice;
  }

  /*
   * Applies this site's widget token (from Skynet's widget-settings) to
   * the hidden aioa_token field so it gets saved with the rest of the
   * form -- the only part of the old account panel that is still needed.
   * The plan/Upgrade-Plan/Start-Free-Trial panel itself has been removed;
   * the static notice from insertUpgradeNotice() covers that messaging.
   * data may be null (widget-settings failed/unreachable) -- then this
   * is a no-op.
   */
  function applyWidgetToken(data) {
    var token = data && (data.token || data.widget_token || data.aioa_token);
    if (!token) { return; }
    var tokenField = document.getElementById('form-widgets-aioa_token');
    if (tokenField) { tokenField.value = token; }
  }

  // ----------------------------------------------------- "Save was clicked"

  function hasFormErrors() {
    return !!document.querySelector(
      '.fieldErrorBox, .invalid-feedback, .field.error, .portalMessage.error, .alert-danger'
    );
  }

  function armPendingSync() {
    var form = getForm();
    if (!form) { return; }
    form.addEventListener('submit', function (event) {
      var submitter = event.submitter;
      if (submitter && submitter.name === 'form.buttons.cancel') { return; }
      // "submit" only fires once browser validation has passed.
      storageSet(window.sessionStorage, PENDING_KEY, String(Date.now()));
    });
  }

  function consumePendingSync() {
    var raw = storageGet(window.sessionStorage, PENDING_KEY);
    if (!raw) { return false; }
    storageRemove(window.sessionStorage, PENDING_KEY);

    var age = Date.now() - parseInt(raw, 10);
    if (isNaN(age) || age < 0 || age > PENDING_TTL_MS) { return false; }
    return !hasFormErrors();
  }

  async function init() {
    if (!getForm()) { return; }
    armPendingSync();

    // Shown immediately, independent of any Skynet API call -- same as
    // the plone module's banner.
    insertUpgradeNotice();

    var syncNow = consumePendingSync();

    // CDN selection: detect once per load and write straight into the
    // hidden no_required_eu field so it is always what gets saved --
    // there is no visible/manual choice for it any more.
    var noRequiredEu = await detectNonEu();
    setNoRequiredEuField(noRequiredEu);

    await registerDomain(noRequiredEu);

    // If this load is the redirect right after Save, push the values
    // that were just saved to Skynet *before* pulling widget-settings
    // back down below -- otherwise the read-back would show the
    // dashboard's pre-save state and appear to silently undo the save.
    if (syncNow) {
      await syncWidgetSettings();
    }

    // Pull this site's current widget configuration from Skynet: apply
    // the token (applyWidgetToken) and the position/color/icon/size
    // values (applyDashboardSettings), so changes made directly on the
    // ADA dashboard show up here too. Best-effort -- both handle
    // data === null if the call failed outright.
    //
    // Skipped on dev/local hosts, same as registerDomain() above: Skynet
    // never has a real registration for "localhost", so a widget-settings
    // read for it comes back empty/unrelated -- applying that would wipe
    // out whatever was just saved (e.g. the position field reverting to
    // blank on every reload).
    if (LOCAL_HOSTS.indexOf(window.location.hostname) === -1) {
      var widgetSettings = await fetchWidgetSettings();
      applyWidgetToken(widgetSettings);

      // Not applied on the reload right after Save (syncNow): Zope just
      // handed back the values that were actually persisted a moment
      // ago, which are already correct and authoritative -- there is
      // nothing to reconcile. Pulling widget-settings back down here
      // instead risks a stale read: syncWidgetSettings() above just
      // pushed this save to Skynet, but Skynet may not have finished
      // processing it by the time this read fires (no guaranteed
      // read-after-write consistency on their side), so is_widget_
      // custom_position and the position fields can still come back as
      // whatever they were *before* this save -- overwriting the
      // freshly-saved, correct values with old ones. Dashboard-made
      // changes are still picked up on every *other* load of this form.
      if (!syncNow) {
        applyDashboardSettings(widgetSettings);
      }
    }
  }

  // Handy from the browser console while testing: AIOA_SKYNET.sync()
  window.AIOA_SKYNET = {
    buildPayload: buildPayload,
    registerDomain: registerDomain,
    resetRegistration: resetRegistration,
    fetchWidgetSettings: fetchWidgetSettings,
    sync: syncWidgetSettings
  };

  if (document.readyState !== 'loading') {
    init();
  } else {
    document.addEventListener('DOMContentLoaded', init);
  }
})();
