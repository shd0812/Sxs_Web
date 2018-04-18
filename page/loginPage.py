import sys
sys.path.append('D:/Python/web/Sxs_Web')
import Base_Page
from selenium import webdriver

class LoginPage(Base_Page.Action):
	
	#定位器
	account_loc= '' #账户位置
	passwd_loc=''   # 密码
	title='登录'    # 本页面title
	eye_loc=''      #密码显示按钮
	loginBtn_loc='' #登录按钮
	
	#Action 输入账号
	def open(self):
		self._open(self.base_url, self.pagetitle)
	
	def input_account(self,account):
		self.type(account_loc,account)
	# 输入密码
	def input_account(self,passwd):
		self.type(passwd_loc,passwd)
	def click_submit(self):
		self.click(loginBtn_loc)
		
		
if __name__ == '__main__':
	url = 'https://www.shaxiaoseng.com'
	title ='登录'
	driver = webdriver.Firefox()
	login = LoginPage(driver,url,title)
	login.open()
	