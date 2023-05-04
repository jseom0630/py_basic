from appium.webdriver.common.mobileby import MobileBy as AppiumBy
from appium import webdriver
import time

desired_cap = {
"platformName": "iOS",
"platformVersion": "16.2",
"deviceName": "iPhone 14",
"automationName": "XCUITest",
"app": "com.apple.mobilesafari"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.get('http://www.google.com')

el4 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeOther[@name=\"검색\"]/XCUIElementTypeOther[1]")
el4.click()
el4.send_keys("한국")
el4.click()
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Go")
el5.click()

time.sleep(3)
driver.quit()

