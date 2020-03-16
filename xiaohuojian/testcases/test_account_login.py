import pytest
from pages.App import App


class TestAccountLogin(object):
    #第一次初始化app进入到登录页面
    @classmethod
    def setup_class(cls):
        cls.loginPage=App.main().gotoLogin().gotoPhoneloginPage()


    #执行下面每一条case都保证从登录页面开始
    def setup_method(self):
        self.account_login_page=self.loginPage.gotoAccountloginPage()

    #测试用例：账号登录：错误的账号密码登录失败
    @pytest.mark.parametrize("account,password",[
        ("15521242762","111111"),
        ("15576889889","123456")
    ])
    def test_login_account(self,account,password):
        #account_login_page=self.loginPage.gotoPhoneloginPage().gotoAccountloginPage()
        self.account_login_page.loginByAccount(account,password)
        assert "155" in self.account_login_page.getAccount()

    #回退页面
    def teardown_method(self):
        self.account_login_page.back()

    @classmethod
    def teardown_class(cls):
        cls.loginPage.driver.quit()





