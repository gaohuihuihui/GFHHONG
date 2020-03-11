# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "X6GNU17913105925"
caps["appPackage"] = "cn.codemao.android.kids.lite"
caps["appActivity"] = ".activity.FirstActivity"
caps["autoGrantPermissions"]=True
caps["noRset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)
#同意隐私协议
el1=driver.find_element_by_id("cn.codemao.android.kids.lite:id/iv_logout_sure")
#driver.implicitly_wait(10)
el1.click()
#点击登录按钮
login=driver.find_element_by_id("cn.codemao.android.kids.lite:id/ivLoginBg")
login.click()



driver.quit()