

from pages.App import App


class TestHome(object):
    @classmethod
    def setup_class(cls):
        cls.homepage=App.main()

    def setup_method(self):
        pass

    #测试用例：未登录状态下登录入口跳转
    def test_login_enter(self):
        self.homepage.gotoLogin()

        assert "tv_version" in self.homepage.gotoLogin().driver.find_element_by_id("cn.codemao.android.kids.lite:id/tv_version")

    def teardown(self):
        pass

