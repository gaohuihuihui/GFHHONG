from driver.AndroidClient import AndroidClient
from pages.CoursesPage import CoursesPage
from pages.WorksPage import WorksPage


#用户登录状态下的首页

class HomePage(object):

    def __init__(self):
        AndroidClient.install_app()


    def gotoCourses(self):
        #todo:click

        return CoursesPage()

    def gotoHighCourse(self):
        #todo:click
        return CoursesPage()

    #登录状态下进入到自由创作页面
    def gotoWorks(self):
        # 调用全局的driver对象使用webdriver api来定位元素，操作app
        AndroidClient.driver.find_element_by_id("cn.codemao.android.kids.lite:id/works")
        AndroidClient.driver.find_element_by_id("cn.codemao.android.kids.lite:id/works").click()
        # todo:click
        return WorksPage()