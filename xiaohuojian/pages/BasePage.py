from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from driver.AndroidClient import AndroidClient


class BasePage(object):
    driver:WebDriver
    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self,kv) ->WebElement :
        #todo：处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self,text) ->WebElement :

        return self.find((By.XPATH,"//*[@text='%s']" %text))



