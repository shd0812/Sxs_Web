import Base_Page
from selenium import webdriver

class LoginPage(Base_Page.Action):
	#global account_loc,passwd_loc,title_loc,eye_loc,loginBtn_loc
	#定位器
	account_loc= 'id=>tel' #账户位置
	passwd_loc='id=>password'   # 密码

	eye_loc=''      #密码显示按钮
	loginBtn_loc='id=>login' #登录按钮
	
	def __init__(self, selenium_driver,base_url,pagetitle):
		super(LoginPage, self).__init__(selenium_driver, base_url,pagetitle)
	
	def open(self):
		self._open(self.base_url, self.pagetitle)
	#Action 输入账号
	def input_account(self,account):
		self.type(self.account_loc,account)
	# 输入密码
	def input_passwd(self,passwd):
		self.type(self.passwd_loc,passwd)
	#点击登录按钮
	def click_submit(self,target_title):
		self.click(self.loginBtn_loc)
		assert self.on_page(target_title), u"打开开页面失败 "
		
if __name__ == '__main__':
	url = 'https://www.shaxiaoseng.com/User/login.html'
	title ='登录'
	account='13521137793'
	passwd='111111'
	driver = webdriver.Firefox()
	login = LoginPage(driver,url,title)
	login.open()
	login.input_account(account)
	login.input_passwd(passwd)
	login.click_submit('沙小僧-取金路上 小沙为您保驾护航')
	