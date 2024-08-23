"""
Let see about the following methods from 'UiScrollable' class
1. setAsHorizontalList()
2. scrollForward(int steps) / scrollForward()
3. scrollBackward(int steps) / scrollBackward()
"""

import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'io.appium.android.apis',
    'appActivity': 'io.appium.android.apis.ApiDemos'
}

url = 'http://127.0.0.1:4723/wd/hub'

options = AppiumOptions().load_capabilities(caps)

driver = webdriver.Remote(url, options=options)
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])

# Find and click "Views"
Views_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Views"]')
assert Views_el.is_displayed()
Views_el.click()

# Navigate to "Gallery" and "1. Photos"
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Gallery').click()
time.sleep(5)
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='1. Photos').click()

# Get the "bounds" attribute of the first image
txt = driver.find_element(AppiumBy.XPATH, value='//android.widget.Gallery[@resource-id="io.appium.android.apis:id/gallery"]/android.widget.ImageView[1]').get_attribute('bounds')
print('First Image bounds ----->', txt)

# Scroll horizontally using UiScrollable
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward()')

# Wait for the element to be present after scrolling
try:
    txt2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@index="1"]'))).get_attribute('bounds')
    print('Bounds after scrolling forward ----->', txt2)
except TimeoutException:
    print("Element not found after scrolling forward")

# Scroll back horizontally
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollBackward()')

# Wait for the element to be present after scrolling back
try:
    txt3 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@index="0"]'))).get_attribute('bounds')
    print('Bounds after scrolling backward ----->', txt3)
except TimeoutException:
    print("Element not found after scrolling backward")

time.sleep(5)
print('Horizontal Scroll is Done')

driver.quit()