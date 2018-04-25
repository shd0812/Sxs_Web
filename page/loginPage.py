import Base_Page

class LoginPage(Base_Page.Action):

	#定位器
	account_loc= 'id=>tel' #账户位置
	passwd_loc='id=>password'   # 密码

	eye_loc=''      #密码显示按钮
	loginBtn_loc='id=>login' #登录按钮

	
	def __init__(self, browser):
		super(LoginPage, self).__init__(browser)
	

	#Action 输入账号
	def input_account(self,account):
		self.input(self.account_loc,account)
	# 输入密码
	def input_passwd(self,passwd):
		self.input(self.passwd_loc,passwd)
	#点击登录按钮
	def click_LoginSubmit(self,expect_title):
		print('1111111',self.loginBtn_loc)
		self.click(self.loginBtn_loc)
		title = self.get_title()
		if title == expect_title:
			pass
		else:
			raise Exception


if __name__ == '__main__':
	url = 'https://www.shaxiaoseng.com/User/login.html'
	title ='登录'
	account='13521137793'
	passwd='111111'

	login = LoginPage('ff')
	login.open(url)
	login.input_account(account)
	login.input_passwd(passwd)
