from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# Desired capabilities
caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',  # Change to your device name if using a real device
    'appPackage': 'com.android.settings',
    'appActivity': 'com.android.settings.Settings',
    'noReset': True,
    'fullReset': False
}

# Appium server URL
url = 'http://127.0.0.1:4723/wd/hub'

options = AppiumOptions()
options.load_capabilities(caps)

# Create a new session
print("Creating Appium driver...")
driver = webdriver.Remote(url, options=options)

# Wait for the app to load
print("Waiting for the app to load...")
time.sleep(5)

# Find an element and perform an action
print("Finding element...")
el = driver.find_element(by=AppiumBy.ID, value='com.android.settings:id/search_action_bar')
print("Clicking element...")
el.click()

print("Quitting driver...")
driver.quit()
