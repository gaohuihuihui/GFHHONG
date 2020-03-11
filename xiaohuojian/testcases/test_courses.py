from pages.HomePage import HomePage


#前提：用户在登录状态下才能进入课程列表页面

class TestCourses(object):
    def test_package_name(self):
        home=HomePage()
        home.gotoCourses()
