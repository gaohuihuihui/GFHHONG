from appium import webdriver




class Testkids(object):
    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.driver=cls.init_appium()
    def setup_method(self):
        print("setup method")
        # Testkids.driver=self.restart_appium()

    def test_accouunt_login(self):


        # 点击登录按钮
        login =Testkids.driver.find_element_by_id("ivLoginBg")
        login.click()
        phone_login=Testkids.driver.find_element_by_xpath("//*[@resource-id='cn.codemao.android.kids.lite:id/action_bar_root']//*[@class='android.widget.ImageView' and @instance='5']")
        phone_login.click()
        account_login=Testkids.driver.find_element_by_xpath("//*[@text='账号登录']")
        account_login.click()

        et_phone=Testkids.driver.find_element_by_id("cn.codemao.android.kids.lite:id/et_phone")
        et_phone.send_keys("15521242762")

        et_password=Testkids.driver.find_element_by_id("cn.codemao.android.kids.lite:id/et_password")
        et_password.send_keys("123456")

        iv_login=Testkids.driver.find_element_by_id("cn.codemao.android.kids.lite:id/iv_login")
        iv_login.click()

        Testkids.driver.quit()
    def test_phone_login(self):
        pass
    def test_wechat_login(self):
        pass
    def test_wechatsaoma_login(self):
        pass

    def tearDown(self):
        print("teardown ")
    @classmethod
    def tearDown_class(cls):
        print("teardwon cls")

    @classmethod
    def init_appium(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "X6GNU17913105925"
        caps["appPackage"] = "cn.codemao.android.kids.lite"
        caps["appActivity"] = ".activity.FirstActivity"
        caps["autoGrantPermissions"] = True
        #caps["noRset"] = True
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)

        #点击同意用户协议，进入应用
        el1 = driver.find_element_by_id("iv_logout_sure")
        el1.click()
        return driver
    # @classmethod
    # def restart_appium(cls):
    #     caps = {}
    #     caps["platformName"] = "Android"
    #     caps["deviceName"] = "X6GNU17913105925"
    #     caps["appPackage"] = "cn.codemao.android.kids.lite"
    #     caps["appActivity"] = ".activity.FirstActivity"
    #     caps["autoGrantPermissions"] = True
    #     caps["noRset"] = True
    #     driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    #     driver.implicitly_wait(10)
    #     return driver




