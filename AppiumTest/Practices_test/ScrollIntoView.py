import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, WebDriverException

caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',  # Change to your device name if using a real device
    'appPackage': 'com.androidsample.generalstore',
    'appActivity': 'com.androidsample.generalstore.MainActivity'
}
url = 'http://127.0.0.1:4723/wd/hub'

options = AppiumOptions()
options.load_capabilities(caps)

# Create a new session
print("Creating Appium driver...")
driver = webdriver.Remote(url, options=options)

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, InvalidSelectorException,
                                                                       WebDriverException])  # Explicit Wait

toolbarTitleText = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.androidsample.generalstore:id/toolbar_title")').text
assert toolbarTitleText == "General Store"
print('toolbarTitleText: ', toolbarTitleText)

driver.implicitly_wait(5)
el = wait.until(EC.presence_of_element_located(
    (AppiumBy.XPATH, '//android.widget.TextView[@text="Select the country where you want to shop"]')))
lblTxt_Status = el.is_displayed()
assert lblTxt_Status == True

# AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Select the country where you want to shop")'

# Dropdown option selection
wait.until(EC.presence_of_element_located(
    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Spinner")'))).click()
time.sleep(5)
driver.implicitly_wait(5)

# Selected option is displayed or not
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("India"))')))
Scroll_Status = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           'new UiSelector().resourceId("android:id/text1")'))).is_displayed()
assert Scroll_Status == True
print('Scroll is Done')

wait.until(EC.presence_of_element_located(
    (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/text1' and @text='India']"))).click()
print('Dropdown value selected')

time.sleep(5)
SelectedOpt_value = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().resourceId("android:id/text1")'))).text
assert SelectedOpt_value == "India"

time.sleep(5)

driver.quit()
print('Successfully Done')
