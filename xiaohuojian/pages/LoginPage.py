from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.PhoneloginPage import PhoneloginPage


class LoginPage(BasePage):
    #版本号
    _tv_version = (By.ID, "cn.codemao.android.kids.lite:id/tv_version")
    #手机登录按钮
    _phone_button=(By.XPATH,"//*[@resource-id='cn.codemao.android.kids.lite:id/action_bar_root']//*[@class='android.widget.ImageView' and @instance='5']")
    #微信登录按钮
    _wechat_button=(By.XPATH,"//*[@resource-id='cn.codemao.android.kids.lite:id/action_bar_root']//*[@class='android.widget.ImageView' and @instance='6']")
    #微信扫码登录按钮
    _QRwechat_button=(By.XPATH,"//*[@resource-id='cn.codemao.android.kids.lite:id/action_bar_root']//*[@class='android.widget.ImageView' and @instance='7']")


    #进入到手机登录
    def gotoPhoneloginPage(self):

        self.find(self._phone_button)
        self.find(self._phone_button).click()
        return PhoneloginPage()

    #微信登录
    def loginByWechat(self):
        #todo:click
        return self

    #微信扫码登录
    def loginByQRwechat(self):
        #todo:click
        return self

