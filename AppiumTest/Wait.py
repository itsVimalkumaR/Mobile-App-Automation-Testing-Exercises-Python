import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, InvalidElementStateException

# Desired capabilities
caps = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',  # Change to your device name if using a real device
    'appPackage': 'com.android.settings',
    'appActivity': 'com.android.settings.Settings'
    # 'noReset': True,
    # 'fullReset': False
}

# Appium server URL
url = 'http://127.0.0.1:4723/wd/hub'

# Create a new session
options = AppiumOptions()
options.load_capabilities(caps)
driver = webdriver.Remote(url, options=options.load_capabilities(caps))

# Set implicit wait time
driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to be found

# Navigate to the appropriate screen (assuming it involves some steps)
el = driver.find_element(by=AppiumBy.XPATH,
                         value="""//android.view.ViewGroup[@resource-id="com.android.settings:id/search_action_bar"]""")
el.click()
# Example steps:
driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.XPATH,
                    value="""//android.widget.EditText[@resource-id="com.google.android.settings.intelligence:id/open_search_view_edit_text"]""").send_keys(
    "Battery")

# Click the element
time.sleep(5)
driver.implicitly_wait(10)
driver.find_element(by=AppiumBy.XPATH,
                    value="""//android.support.v7.widget.RecyclerView[@resource-id="com.google.android.settings.intelligence:id/list_results"]/android.widget.LinearLayout[2]/android.widget.LinearLayout""").click()

# Validate the element should be visible and element text
driver.implicitly_wait(10)  # implicit wait
txtStatus = driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/collapsing_toolbar").is_displayed()
assert txtStatus == True

# Wait for the element and get its text
wait = WebDriverWait(driver, 10)  # Explicit Wait
element = wait.until(
    EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Battery']")))

# Get the attribute value from the element
txt = element.get_attribute('contentDescription')
print(f"Actual text: {txt}")

# Assert the attribute value
assert txt == "Battery", f"Expected text to be 'Battery' but got '{txt}'"

# Close the session
driver.quit()


"""
            *** Constructor, takes a WebDriver instance and timeout in seconds. ****
Types Of Wait:- 

# implicit wait
driver.implicitly_wait(10)

# Explicit Wait
wait = WebDriverWait(driver, 10)
 
# Fluent Wait
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=ElementNotVisibleException)
"""
