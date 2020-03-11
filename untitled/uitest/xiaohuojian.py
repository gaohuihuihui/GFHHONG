# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "77c011f4"
caps["appPackage"] = "cn.codemao.android.kids.lite"
caps["appActivity"] = ".activity.FirstActivity"
caps["noRset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)
el1 = driver.find_element_by_id("cn.codemao.android.kids.lite:id/iv_logout_sure")
el1.click()



#driver.quit()