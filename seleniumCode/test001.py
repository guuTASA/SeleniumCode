from selenium import webdriver
from time import sleep
import unittest


class RegisterNewUser(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		#self.driver.get("http://www.baidu.com")
		self.driver.get("http://121.41.75.135:8180/wd-pfprod-web/login")

	def test_search_test(self):
		driver = self.driver

		#driver.find_element_by_id("kw").send_keys("kitten")
		#driver.find_element_by_id("su").click()

		driver.find_element_by_id("login-switch").click()
		driver.find_element_by_id("userName").clear()
		driver.find_element_by_id("userName").send_keys("15968177383")
		driver.find_element_by_id("password").clear()
		driver.find_element_by_id("password").send_keys("12345X")
		
	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main(verbosity = 2)





