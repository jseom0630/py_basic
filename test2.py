from appium.webdriver.common.mobileby import MobileBy as AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver
from capa import driver
import time

# desired_cap = {
#     "platformName": "Android",
#     "platformVersion": "13",
#     "deviceName": "jseom0630",
#     "automationName": "uiautomator2",
#     "appPackage": "com.marvrus.whosmvp",
#     "appActivity": "com.marvrus.whosmvp.MainActivity"
# }

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

driver.implicitly_wait(10)

el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button")
el1.click()

time.sleep(10)


# "로그인" 버튼의 bounds 값
bounds = [48, 1992, 1032, 2148]

# TouchAction 클래스를 사용하여 "로그인" 버튼을 클릭
x = (bounds[0] + bounds[2]) / 2
y = (bounds[1] + bounds[3]) / 2
action = TouchAction(driver)
action.tap(x=x, y=y).perform()
# el2 = driver.find_element_by_xpath("//android.widget.Button[contains(@text, '로그인 하기')]")
# el2.click()

driver.implicitly_wait(10)

el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText")
el3.click()
driver.implicitly_wait(10)

el3.send_keys("jseom")
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.EditText")
el4.click()
el4.send_keys("aaaaaa1!")
driver.implicitly_wait(10)

el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.Button")
el5.click()


time.sleep(3)
driver.quit()
