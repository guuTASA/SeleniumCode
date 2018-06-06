from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("kitten")
driver.find_element_by_id("su").click()
sleep(10)

driver.quit()