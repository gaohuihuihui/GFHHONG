from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):

    @classmethod
    def install_app(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "X6GNU17913105925"
        caps["appPackage"] = "cn.codemao.android.kids.lite"
        caps["appActivity"] = ".activity.FirstActivity"
        caps["autoGrantPermissions"] = True
        # caps["noRset"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        # 点击同意用户协议，进入应用
        el1 = cls.driver.find_element_by_id("iv_logout_sure")
        el1.click()
        return cls.driver
    @classmethod
    def restart_app(cls)->WebDriver:
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "X6GNU17913105925"
        caps["appPackage"] = "cn.codemao.android.kids.lite"
        caps["appActivity"] = ".activity.FirstActivity"
        caps["autoGrantPermissions"] = True
        caps["noRset"] = True
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
