"""
Let see about the following methods from 'UiScrollable' class
1. setAsVerticalList()
2. scrollToBeginning(int maxSwipes)
3. scrollToEnd(int maxSwipes)
"""

import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import InvalidArgumentException, TimeoutException, InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.androidsample.generalstore',
    'appActivity': 'com.androidsample.generalstore.MainActivity'
}

url = 'http://127.0.0.1:4723/wd/hub'

options = AppiumOptions()
options.load_capabilities(caps)
driver = webdriver.Remote(url, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[InvalidArgumentException, TimeoutException, InvalidSelectorException])

print("Clicking dropdown .....")
driver.find_element(by=AppiumBy.ID, value='com.androidsample.generalstore:id/spinnerCountry').click()
status = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                    '//android.widget.TextView[@resource-id="android:id/text1" and @text="American Samoa"]'))).is_displayed()
print('Are you clicked the Drop down?', '\n', '-->', status)

# Number of times to attempt scrolling
scroll_attempts = 10
found = False

for i in range(scroll_attempts):
    try:
        # Scroll to the desired element
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            value='new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(2)')

        # Check if the target element is visible after the scroll
        element = wait.until(EC.presence_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.TextView[@resource-id="android:id/text1" and @text="Germany"]'
        )))

        if element.is_displayed():
            found = True
            print(f"Element found after {i + 1} scroll attempts.")
            break

    except TimeoutException:
        print(f"Element not found in attempt {i + 1}. Scrolling again...")

if not found:
    print("Element not found after maximum scroll attempts.")
else:
    # Click on the element if found
    element.click()

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(2)')
time.sleep(2)
txt = driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/text1" and @index="7"]').get_attribute('text')
print('---->', txt)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(2)')
time.sleep(2)
txt1= driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="android:id/text1" and @index="7"]').get_attribute('text')
print('----->', txt1)
# Perform further actions if needed
print('Scrolling is done')
time.sleep(5)

driver.quit()
