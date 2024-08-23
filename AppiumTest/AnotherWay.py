"""
==============================================================================================================================================
                                    Scroll to element
==============================================================================================================================================
Way 1:-
-------
    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Germany"))')))

Way 2:-
------
deviceSize = driver.get_window_size()
print('Device screen resolution :- ', deviceSize)

screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
print('Device Width :- ', screenWidth, '\n' 'Device Height :- ', screenHeight)

startX = screenWidth / 2
endX = screenWidth / 2
print('Beginning X-axis :- ', startX, '\n' 'Ending X-axis :- ', endX)

startY = screenHeight * 8 / 9
endY = screenHeight / 9
print('Beginning Y-axis :- ', startY, '\n' 'Ending Y-axis :- ', endY)

actions = ActionChains(driver)
actions.long_press(None, startX, startY).move_to(None, endX, endY).release().perform()
time.sleep(5)
# actions.long_press(None, endX, endY).move_to(None, startX, startY).release().perform()
"""