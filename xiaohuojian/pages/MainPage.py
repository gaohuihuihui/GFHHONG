from selenium.webdriver.common.by import By
from driver.AndroidClient import AndroidClient
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.WorksPage import WorksPage


#用户未登录状态下的首页

class MainPage(BasePage):
    # #调用appium启动app
    # def __init__(self):
    #     AndroidClient.install_app()

    #进入到登录页面
    def gotoLogin(self):
        login_button=(By.ID,"cn.codemao.android.kids.lite:id/ivLoginBg")
        self.find(login_button)
        self.find(login_button).click()

        # self.driver.find_element(By.ID,"cn.codemao.android.kids.lite:id/ivLoginBg")
        # self.driver.find_element(By.ID,"cn.codemao.android.kids.lite:id/ivLoginBg").click()

        # self.driver.find_element_by_id("cn.codemao.android.kids.lite:id/ivLoginBg")
        # self.driver.find_element_by_id("cn.codemao.android.kids.lite:id/ivLoginBg").click()
        return LoginPage()


    #未登录态进入到自由创作页面
    def gotoWorks(self):
        works_button=(By.ID,"cn.codemao.android.kids.lite:id/works")
        self.find(works_button)
        self.find(works_button).click()
        #调用全局的driver对象使用webdriver api来定位元素，操作app
        # self.driver.find_element_by_id("cn.codemao.android.kids.lite:id/works")
        # self.driver.find_element_by_id("cn.codemao.android.kids.lite:id/works").click()

        return WorksPage()
