from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from driver.AndroidClient import AndroidClient


class BasePage(object):
    driver:WebDriver

    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self,kv) ->WebElement :

        return self.driver.find_element(*kv)
