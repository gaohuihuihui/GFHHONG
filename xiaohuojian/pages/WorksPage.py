from pages.BasePage import BasePage
from pages.CreatPage import CreatPage


class WorksPage(BasePage):
    def default(self):
        return self

    def gotoCreatPage(self):
        #todo:
        return CreatPage()
