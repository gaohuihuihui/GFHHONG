from pages.App import App


class TestYaml(object):

    def setup(self):
        self.home=App.main().gotoLogin()
    # def setup(self):
    #     pass
    def test_main(self):
        self.home.gotoPhoneloginPage()








