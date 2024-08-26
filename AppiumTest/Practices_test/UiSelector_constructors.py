import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException

caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',  # Change to your device name if using a real device
    'appPackage': 'com.androidsample.generalstore',
    'appActivity': 'com.androidsample.generalstore.MainActivity'
}
url = 'http://127.0.0.1:4723/wd/hub'

Options = AppiumOptions()
Options.load_capabilities(caps)
driver = webdriver.Remote(url, options=Options)

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, InvalidSelectorException])  # Explicit Wait

toolbarTitleText = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("com.androidsample.generalstore:id/toolbar_title")').text
assert toolbarTitleText == "General Store"
print('toolbarTitleText: ', toolbarTitleText)

driver.implicitly_wait(5)
el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Select the country where you want to shop"]')))
lblTxt_Status = el.is_displayed()
assert lblTxt_Status == True

# AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Select the country where you want to shop")'

# Dropdown option selection
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Spinner")'))).click()
time.sleep(5)
driver.implicitly_wait(5)
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/text1' and @text='Andorra']"))).click()
print('Dropdown value selected')
# Selected option is displayed or not
SelectedOpt_value = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().resourceId("android:id/text1")'))).text
assert SelectedOpt_value == "Andorra"

time.sleep(5)

driver.quit()
print('Successfully Done')