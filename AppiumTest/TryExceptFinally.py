from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# Function to create a new session
def create_driver():
    options = AppiumOptions()
    options.load_capabilities(caps)
    return webdriver.Remote(url, options=options)


try:
    # Create a new session
    print("Creating Appium driver...")
    driver = create_driver()

    # Wait for the app to load
    print("Waiting for the app to load...")
    time.sleep(5)

    # Explicit wait for the element to be present
    print("Waiting for element to be present...")
    wait = WebDriverWait(driver, 20)
    el = wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.android.settings:id/search_action_bar"]')))

    # Find an element and perform an action
    print("Clicking element...")
    el.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the session if it was created
    if 'driver' in locals():
        print("Quitting driver...")
        driver.quit()
