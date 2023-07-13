# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s plone.all_in_one_accessibility -t test_all_in_one_accessibility_setting.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src plone.all_in_one_accessibility.testing.PLONE_ALL_IN_ONE_ACCESSIBILITY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/plone/all_in_one_accessibility/tests/robot/test_all_in_one_accessibility_setting.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a All in One Accessibility setting
  Given a logged-in site administrator
    and an add All in One Accessibility setting form
   When I type 'My All in One Accessibility setting' into the title field
    and I submit the form
   Then a All in One Accessibility setting with the title 'My All in One Accessibility setting' has been created

Scenario: As a site administrator I can view a All in One Accessibility setting
  Given a logged-in site administrator
    and a All in One Accessibility setting 'My All in One Accessibility setting'
   When I go to the All in One Accessibility setting view
   Then I can see the All in One Accessibility setting title 'My All in One Accessibility setting'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add All in One Accessibility setting form
  Go To  ${PLONE_URL}/++add++All in One Accessibility setting

a All in One Accessibility setting 'My All in One Accessibility setting'
  Create content  type=All in One Accessibility setting  id=my-all_in_one_accessibility_setting  title=My All in One Accessibility setting

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the All in One Accessibility setting view
  Go To  ${PLONE_URL}/my-all_in_one_accessibility_setting
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a All in One Accessibility setting with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the All in One Accessibility setting title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
