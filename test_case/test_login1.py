import sys
sys.path.append('D:/Python/web/Sxs_Web')
import base_element
import dd_utils
import unittest
import time
from selenium import webdriver

class LoginTest(unittest.TestCase):
	"""docstring for LoginTest"""
	@classmethod
	def setUp(self):
		self.driver = base_element.DD_element("ff")

	def test_case1(self):
		self.driver.open('https://pc.shaxiaoseng.com:4433')
		self.driver.click("link_text=>登录")
		operate_file = dd_utils.operate_file('test_data/login.yaml')
		data = operate_file.open()
		self.driver.type(dd_utils.ob_element(data,0),'15900000035')
		self.driver.type(dd_utils.ob_element(data,1), '123456')
		self.driver.click(dd_utils.ob_element(data,2))
		try:
			self.assertIn(dd_utils.ob_valite(data), self.driver.get_title())
			print('登录成功')
			operate_file = dd_utils.operate_file('test_data/test_tender1.yaml')
			data = operate_file.open()
			self.driver.click(dd_utils.ob_element(data,0))
			self.driver.click(dd_utils.ob_element(data,1))
			self.driver.click(dd_utils.ob_element(data,2))
			self.driver.click(dd_utils.ob_element(data, 5))
			self.driver.click(dd_utils.ob_element(data, 6))
			time.sleep(4)
		except AssertionError:
			print('登录失败')


	# def test_case2(self):
	# 	self.driver.open('https://www.shaxiaoseng.com')
	# 	print(self.driver.get_title())
	# 	operate_file = dd_utils.operate_file('test_data/test_tender1.yaml')
	# 	data = operate_file.open()
	# 	self.driver.click(dd_utils.ob_element(data,0))
	# 	self.driver.click(dd_utils.ob_element(data,1))
	# 	self.driver.click(dd_utils.ob_element(data,2))


	def tearDown(self): 
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
		





# driver = base_element.DD_element("ff")
# driver.open('https://www.shaxiaoseng.com')
# print(driver.get_title())
# driver.click("link_text=>登录")
# operate_file = dd_utils.operate_file('test_data/login.yaml')
# data = operate_file.open()
# print(data)
# driver.type(dd_utils.ob_element(data,0),'13521137793')
# driver.type(dd_utils.ob_element(data,1), '111111')
# driver.click(dd_utils.ob_element(data,2))

# print(driver.get_url())
# #

# print(driver.get_title())