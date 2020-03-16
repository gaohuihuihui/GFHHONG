from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from driver.AndroidClient import AndroidClient
import yaml


class BasePage(object):
    driver:WebDriver
    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self,kv) ->WebElement :
        #todo：处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self,text) ->WebElement :

        return self.find((By.XPATH,"//*[@text='%s']" %text))

    def loadsteps(self,po_path,key,**kwargs):
        file=open(po_path,"r") #创建文件
        po_data=yaml.load(file) #加载文件
        pomethod=po_data[key]
        print(pomethod)
        for step in pomethod:
            action= step['action']
            element:WebElement=self.driver.find_element(by=step['by'],value=step['locator'])
            #todo:定位失败，多数是因为弹框，try catch后进入一个弹框处理 元素的智能化等待
            if action=="click":
                element.click()
            elif action=="sendkeys":
                text=str(step['text'])
                for k,v in kwargs.items():
                    text=text.replace("$%s" %k,v)
                print("update new text: %s" % text)
                element.send_keys(text)
            else:
                print(("UNKNOW ERROR %s") %step)








