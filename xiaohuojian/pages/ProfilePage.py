from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


#个人信息页面
class ProfilePage(BasePage):

    _back_button=(By.ID,"cn.codemao.android.kids.lite:id/btnBack")#后退按钮
    _person_information=(By.ID,"cn.codemao.android.kids.lite:id/rb_person_information")#个人信息tab
    _about_us=(By.ID,"cn.codemao.android.kids.lite:id/rb_about_us")
    _exit_login_button=(By.XPATH,"//*[@class='android.widget.ImageView' and @instance='2']") #退出登录按钮
    _tv_user_agreement=(By.ID,"cn.codemao.android.kids.lite:id/tv_user_agreement") #《用户服务协议》
    _tv_privacy_protocol=(By.ID,"cn.codemao.android.kids.lite:id/tv_privacy_protocol")


    def defalut(self):
        self.find(self._person_information)
        self.find(self._person_information).click()
        return self

    def exitLogin(self):
        pass

    def gotoAbout(self):
        self.find(self._about_us)
        self.find(self._about_us).click()
        return self
    def back(self):
        pass






