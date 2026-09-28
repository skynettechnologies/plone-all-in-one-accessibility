
// Base URL for this add-on's own bundled images (icon-type previews, size
// previews). Resolved from custom.js's own <script src>, which is always
// "<site>/++plone++plone.all_in_one_accessibility/custom.js[?v=...]" (see
// AccessibilityCSSViewlet.render()) -- so this works on any site URL/
// subpath without hardcoding one, and needs no server-side value passed
// in. document.currentScript is only valid while this file is first
// executing (a plain synchronous <script src> tag), so it is captured
// here at top level, not inside onReady()/later callbacks where it would
// already be null.
var AIOA_IMG_BASE = (function () {
  var script = document.currentScript ||
    document.querySelector('script[src*="/++plone++plone.all_in_one_accessibility/custom.js"]');
  if (script && script.src) {
    return script.src.replace(/custom\.js(\?.*)?$/, 'img/');
  }
  return '';
})();

function onReady(fn) {
  if (document.readyState !== 'loading') {
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
}

onReady(function () {
  function show(id) {
    const el = document.querySelector(`#${id}`)?.closest('.field');
    if (el) el.style.display = '';
  }

  function hide(id) {
    const el = document.querySelector(`#${id}`)?.closest('.field');
    if (el) el.style.display = 'none';
  }

  function groupFields(pxId, choiceId) {
    const pxField = document.querySelector(`#${pxId}`)?.closest('.field');
    const choiceField = document.querySelector(`#${choiceId}`)?.closest('.field');

    if (pxField && choiceField && !pxField.parentNode.classList.contains('inline-field-row')) {
      const wrapper = document.createElement('div');
      wrapper.className = 'inline-field-row';
      pxField.parentNode.insertBefore(wrapper, pxField);
      wrapper.appendChild(pxField);
      wrapper.appendChild(choiceField);
    }
  }

  // updateVisibility() only controls field visibility. It never changes
  // the configured values, so Custom Position can be disabled/re-enabled
  // without losing the user's last custom offsets and directions.
  function updateVisibility() {
    const enablePos = document.querySelector('#form-widgets-enable_widget_icon_position-0');
    const enableSize = document.querySelector('#form-widgets-enable_icon_custom_size-0');

    if (enablePos && enablePos.checked) {
      show('form-widgets-to_the_right_px');
      show('form-widgets-to_the_right');
      show('form-widgets-to_the_bottom_px');
      show('form-widgets-to_the_bottom');
      hide('form-widgets-aioa_place');
    } else {
      hide('form-widgets-to_the_right_px');
      hide('form-widgets-to_the_right');
      hide('form-widgets-to_the_bottom_px');
      hide('form-widgets-to_the_bottom');
      show('form-widgets-aioa_place');
    }

    if (enableSize && enableSize.checked) {
      show('form-widgets-aioa_size_value');
      hide('form-widgets-aioa_icon_size');
    } else {
      hide('form-widgets-aioa_size_value');
      show('form-widgets-aioa_icon_size');
    }
  }

  function bindEvents() {
    const enablePos = document.querySelector('#form-widgets-enable_widget_icon_position-0');
    const enableSize = document.querySelector('#form-widgets-enable_icon_custom_size-0');

    if (enablePos) {
      enablePos.addEventListener('change', function () {
        // Custom Position is a visibility toggle only. Preserve the
        // user's last configured offsets and directions when it is
        // disabled and later enabled again.
        updateVisibility();
      });
    }
    if (enableSize) {
      enableSize.addEventListener('change', function () {
        // Custom Icon Size is a visibility toggle only. Preserve the
        // user's last exact PX value when the option is disabled and
        // later enabled again; never replace it with the schema default.
        updateVisibility();
      });
    }
  }

  groupFields('form-widgets-to_the_right_px', 'form-widgets-to_the_right');
  groupFields('form-widgets-to_the_bottom_px', 'form-widgets-to_the_bottom');

  // Initial render: only show/hide for the value the form was loaded
  // with (the last-saved value) -- never reset it.
  updateVisibility();
  bindEvents();

  // Exposed so aioa_skynet_sync.js's applyDashboardSettings() can keep
  // the show/hide state in sync with a checkbox value it just set
  // programmatically, WITHOUT going through the checkbox's "change"
  // event -- that event is also how bindEvents() above triggers
  // the checkbox reset handlers, which must only
  // ever fire from a person actually clicking the checkbox. Dispatching
  // a real "change" event from dashboard-sync code used to trigger that
  // same reset (e.g. whenever Skynet's read-back of is_widget_custom_position
  // lagged behind a save and came back false), silently wiping the
  // custom offset/dropdown values right after they were saved.
  window.AIOA_updateVisibility = updateVisibility;
});

// ---------------------- ICON TYPE GRID LOGIC ----------------------

function enhanceIconTypeSelector() {
  const iconField = document.querySelector('#form-widgets-aioa_icon_type');
  if (!iconField) return;

  // Called again by aioa_skynet_sync.js's applyDashboardSettings() after
  // writing a dashboard-fetched value into iconField, to rebuild the grid
  // with the right tile highlighted -- remove any grid from a previous
  // call first so it doesn't just pile up a second one next to it.
  const existingGrid = iconField.parentNode.querySelector('.icon-select-grid');
  if (existingGrid) { existingGrid.remove(); }

  const values = Array.from(iconField.options).map(opt => opt.value);
  const selectedValue = iconField.value;

  const wrapper = document.createElement('div');
  wrapper.className = 'icon-select-grid';

  values.forEach(val => {
    const div = document.createElement('div');
    div.className = 'icon-select-option';
    if (val === selectedValue) div.classList.add('selected');
    div.dataset.value = val;

    const img = document.createElement('img');
    img.src = `${AIOA_IMG_BASE}${val}.svg`;
    img.alt = val;

    div.appendChild(img);
    wrapper.appendChild(div);
  });

  iconField.style.display = 'none';
  iconField.parentNode.appendChild(wrapper);

  wrapper.addEventListener('click', function (e) {
    const option = e.target.closest('.icon-select-option');
    if (!option) return;

    const value = option.dataset.value;
    iconField.value = value;
    iconField.dispatchEvent(new Event('change'));

    wrapper.querySelectorAll('.icon-select-option').forEach(el => el.classList.remove('selected'));
    option.classList.add('selected');

    updateSizePreview(value);
  });

  updateSizePreview(selectedValue);
}

const sizeMap = {
  'aioa-big-icon': 75,
  'aioa-medium-icon': 65,
  'aioa-default-icon': 55,
  'aioa-small-icon': 45,
  'aioa-extra-small-icon': 35,
};

function updateSizePreview(selectedIconType) {
  const sizeField = document.querySelector('#form-widgets-aioa_icon_size');
  if (!sizeField) return;

  const values = Array.from(sizeField.options).map(opt => opt.value);
  const wrapperId = 'aioa-size-icon-grid';
  let wrapper = document.getElementById(wrapperId);

  if (wrapper) wrapper.remove();

  wrapper = document.createElement('div');
  wrapper.id = wrapperId;
  wrapper.className = 'icon-select-grid';

  values.forEach(val => {
    const div = document.createElement('div');
    div.className = 'icon-select-option';
    if (val === sizeField.value) div.classList.add('selected');
    div.dataset.value = val;

    const img = document.createElement('img');
    img.src = `${AIOA_IMG_BASE}${selectedIconType}.svg`;
    img.alt = val;
    img.style.width = `${sizeMap[val]}px`;

    div.appendChild(img);
    wrapper.appendChild(div);
  });

  sizeField.style.display = 'none';
  sizeField.parentNode.appendChild(wrapper);

  wrapper.addEventListener('click', function (e) {
    const option = e.target.closest('.icon-select-option');
    if (!option) return;

    const value = option.dataset.value;
    sizeField.value = value;
    sizeField.dispatchEvent(new Event('change'));

    wrapper.querySelectorAll('.icon-select-option').forEach(el => el.classList.remove('selected'));
    option.classList.add('selected');
  });
}

onReady(() => {
  enhanceIconTypeSelector();
});



