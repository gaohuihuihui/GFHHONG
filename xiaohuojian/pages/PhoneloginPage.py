from selenium.webdriver.common.by import By
from pages.AccountloginPage import AccountloginPage
from pages.BasePage import BasePage


class PhoneloginPage(BasePage):
    #返回按钮
    _back_button=(By.ID,"cn.codemao.android.kids.lite:id/iv_back")
     #版本号
    _tv_version=(By.ID,"cn.codemao.android.kids.lite:id/tv_version")
    #手机号码编辑框
    _phone_editor=(By.ID,"cn.codemao.android.kids.lite:id/et_phone")
    #验证码输入框
    _code_editor=(By.ID,"cn.codemao.android.kids.lite:id/et_password")
    #获取验证码按钮
    _code_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_get_code")
    #手机登录按钮
    _phone_login_button=(By.ID,"cn.codemao.android.kids.lite:id/tv_bind")
    #账号登录
    _account_button=(By.XPATH,"//*[@text='账号登录']")

    #手机登录
    def loginByPhone(self,phone,code):
        pass


    #进入到账号密码登录页面
    def gotoAccountloginPage(self):

        self.find(self._account_button)
        self.find(self._account_button).click()
        return AccountloginPage()
