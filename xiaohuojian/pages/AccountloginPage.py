import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions


class AccountloginPage(BasePage):

    #返回按钮
    _back_button=(By.ID,"cn.codemao.android.kids.lite:id/iv_back")
    #账号输入框
    _account_editor=(By.ID,"cn.codemao.android.kids.lite:id/et_phone")
    #密码输入框
    _password_editor=(By.ID,"cn.codemao.android.kids.lite:id/et_password")
    #账号登录按钮
    _account_login_button=(By.ID,"cn.codemao.android.kids.lite:id/iv_login")


    #使用账号密码登录
    def loginByAccount(self,account,password):
        self.find(self._account_editor).send_keys(account)
        self.find(self._password_editor).send_keys(password)
        time.sleep(3) #输入账号密码后按钮不能立即变成可点击状态导致报错
        self.find(self._account_login_button).click()
        return self

    #登录成功后返回首页
    def loginSucessByAccount(self,account,password):
        self.find(self._account_editor).send_keys(account)
        self.find(self._password_editor).send_keys(password)
        #WebDriverWait(self.driver,2).until(expected_conditions.presence_of_element_located())显示等待
        time.sleep(3)  # 输入账号密码后按钮不能立即变成可点击状态导致报错
        self.find(self._account_login_button).click()
        from pages.MainPage import MainPage
        return MainPage()

    #返回toast信息
    def getToastMsg(self):
        #todo:如何获取页面错误提示信息
        pass

    #返回编辑框信息
    def getAccount(self):
        self.driver.implicitly_wait(10)
        #print(self.find(self._account_editor).text)
        return self.find(self._account_editor).text

    #返回上一页面:手机登录页面
    def back(self):
        self.find(self._back_button).click()
        from pages.PhoneloginPage import PhoneloginPage  #延迟导入
        return PhoneloginPage()