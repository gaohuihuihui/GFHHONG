
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "X6GNU17913105925"
caps["appPackage"] = "cn.codemao.android.kids.lite"
caps["appActivity"] = ".activity.FirstActivity"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]")
#el2nd_element=driver.find_element_by_id()
el1.click()
#driver.fi_by_accessibility_id()
driver.quit()