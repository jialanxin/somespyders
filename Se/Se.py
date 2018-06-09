import os
os.makedirs('./img/',exist_ok=True)
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://weibo.com/login.php")
driver.find_element_by_id("loginname").click()
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("13375282639")
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("5200693SYo")
driver.find_element_by_xpath("//div[@id='pl_login_form']/div/div[3]/div[6]/a/span").click()
driver.find_element_by_xpath("//div[@id='v6_pl_rightmod_myinfo']/div/div/div[2]/ul/li[3]/a/strong").click()
driver.find_element_by_xpath("//div[@id='Pl_Official_MyProfileFeed__20']/div/div[2]/div[2]/div/ul/li[4]/a/span/span/span/em[2]").click()
driver.find_element_by_xpath("//div[@id='plc_top']/div/div/div[3]/div[2]/div[2]/a/em").click()
driver.find_element_by_link_text(u"退出").click()
driver.close()