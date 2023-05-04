from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "jseom0630",
    "automationName": "uiautomator2",
    "appPackage": "com.marvrus.whosmvp",
    "appActivity": "com.marvrus.whosmvp.MainActivity"
    # "noReset": "True"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)