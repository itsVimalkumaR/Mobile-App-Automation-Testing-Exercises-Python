import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

# Capabilities
caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'uiautomator2',
    'appPackage': 'com.google.android.dialer',
    'appActivity': 'com.android.dialer.main.impl.MainActivity'
}

url = 'http://127.0.0.1:4723/wd/hub'

# Create a new session
print("Creating Appium driver...")
options = AppiumOptions()
options.load_capabilities(caps)
driver = webdriver.Remote(url, options=options)

# Wait for the app to load
print("Waiting for the app to load...")
time.sleep(5)

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[NoSuchElementException, TimeoutException, WebDriverException])

# Wait for the Contacts tab and click it
contacts_tab = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                          '//android.widget.TextView[@resource-id="com.google.android.dialer:id/navigation_bar_item_small_label_view" and @text="Contacts"]')))
contacts_tab.click()
print('Navigated to the Contact tab')

# Find the contact element and perform the tap action using TouchAction
el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.TextView[@resource-id="com.google.android.dialer:id/contact_name" and @text="Vimalkumar"]')))
actions = TouchAction(driver)
actions.tap(el).perform()
print('Clicked the person contact')
time.sleep(5)

# Perform the tap action using TouchAction on Navigate to go back
goBack_icon = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')))
actions.tap(goBack_icon).perform()
print('Go back to the contact page')

# Perform the long_press action using TouchAction on the person
el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                 '//android.widget.TextView[@resource-id="com.google.android.dialer:id/contact_name" and @text="Vimalkumar"]')))
actions.long_press(el1).release().perform()  # No indexing here
time.sleep(5)
print('Long pressed the person contact')

# Optionally, release resources
driver.quit()

"""
    # Define touch input
touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    # Create an action chain
actions = ActionBuilder(driver, touch_input)
    # Perform the long press
actions.pointer_action.move_to(el1).pointer_down().pause(2).pointer_up().perform()
print('Long pressed the person contact')
======================================================================================
    # Define touch input
touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
    # Create an action chain with ActionBuilder
actions = ActionBuilder(driver, touch_input)
    # Define the touch action (move to element, press, pause, release)
actions.pointer_action.move_to(el1).pointer_down().pause(2).pointer_up()
    # Perform the action
actions.perform()
print('Long pressed the person contact')
======================================================================================
# Perform the tap with a duration to simulate long press
driver.tap([(el1.location['x'], el1.location['y'])], 2000)  # Duration in milliseconds
======================================================================================
# Perform the long press with a specified duration
actions.press(el1).wait(2000).release().perform()  # Duration in milliseconds
print('Long pressed the person contact')
======================================================================================
# print('Simulated long press by tap')
driver.execute_script("mobile: longClickGesture", {'elementId': el1.id, 'duration': 2000})
print('Long pressed using JavaScript executor')
======================================================================================
    # Define the positions to tap (you need to set these coordinates)
positions = [(100, 200)]  # Example coordinates, replace with actual values
    # Perform the tap action using PointerInput
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
for pos in positions:
    x = pos[0]
    y = pos[1]
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(duration / 1000.0)  # Use duration as a float
    actions.w3c_actions.pointer_action.release()
actions.perform()
======================================================================================
    # Define the positions to tap (you need to set these coordinates)
positions = [(100, 200)]  # Example coordinates, replace with actual values
    # Perform the tap action using PointerInput
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
for pos in positions:
    x = pos[0]
    y = pos[1]
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    if duration:
        actions.w3c_actions.pointer_action.pause(duration / 1000)
    else:
        actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
actions.perform()
======================================================================================
# Perform long press action using W3C Actions
actions = ActionBuilder(driver)
pointer = PointerInput(PointerInput.TOUCH, "finger")
actions.add_action(pointer.create_pointer_move(duration=0, x=element.rect['x'], y=element.rect['y']))
actions.add_action(pointer.create_pointer_down())
actions.add_action(pointer.create_pause(2))  # 2 seconds pause for long press
actions.add_action(pointer.create_pointer_up())
actions.perform()
"""