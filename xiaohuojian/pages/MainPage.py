from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.ProfilePage import ProfilePage
from pages.WorksPage import WorksPage


class MainPage(BasePage):

    _courses_button=(By.ID,"cn.codemao.android.kids.lite:id/course") #课程按钮
    _works_button = (By.ID, "cn.codemao.android.kids.lite:id/works") #作品按钮
    _login_button = (By.ID, "cn.codemao.android.kids.lite:id/ivLoginBg") #登录按钮
    _profile_button=(By.ID,"cn.codemao.android.kids.lite:id/login") #进入到个人中心
    _courses_package_1=(By.XPATH,"//*[@resource-id='cn.codemao.android.kids.lite:id/ivCoursePackage' and @instance='1']")
    _courses_package_2=(By.XPATH,"//*[@resource-id='cn.codemao.android.kids.lite:id/ivCoursePackage' and @instance='2']")

    #默认定位在课程包页面
    def default(self):
        self.find(self._courses_button)
        self.find(self._courses_button).click()
        return self

    #未登录状态下进入到登录页面
    def gotoLogin(self):

        self.find(self._login_button)
        self.find(self._login_button).click()
        return LoginPage()

    #进入到自由创作页面
    def gotoWorks(self):
        self.find(self._works_button)
        self.find(self._works_button).click()
        return WorksPage()

    #登录状态下进入到个人中心页面
    def gotoProfile(self):
        self.find(self._profile_button)
        self.find(self._profile_button).click()
        return ProfilePage()

    #判断是否登录
    def isLogin(self):
        pass







