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

# options = AppiumOptions()
# options.load_capabilities(caps)

# Create a new session
print("Creating Appium driver...")
driver = webdriver.Remote(command_executor=url, desired_capabilities=caps)

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
                                                '//android.widget.TextView[@resource-id="com.google.android.dialer:id/contact_name" and @text="Vimal Kumar"]')))
actions = TouchAction(driver)
actions.tap(el).perform()
print('Clicked the person contact')
time.sleep(5)

# Perform the tap action using TouchAction on Navigate to go back
goBack_icon = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Navigate up')))
actions.tap(goBack_icon).perform()
print('Go back to the contact page')

# Perform the long_press action using TouchAction on the person
actions.long_press(el).release().perform()
time.sleep(5)
print('Long pressed the person contact')

# Optionally, release resources
driver.quit()
