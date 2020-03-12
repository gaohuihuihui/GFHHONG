from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.CreatPage import CreatPage


class WorksPage(BasePage):

    #add_button=(By.ID,"")

    def default(self):
        return self

    def gotoCreatPage(self):
        #todo:
        return CreatPage()
