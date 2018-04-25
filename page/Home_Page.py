import loginPage

class home_Page(loginPage.LoginPage):

    homeLoginBtn_loc='xpath=>/html/body/div[2]/div/div[2]/div[3]/span/a[1]'
    registBtn_loc ='xpath=>/html/body/div[2]/div/div[2]/div[3]/span/a[2]'


    def __init__(self,browser):
        super(home_Page, self).__init__(browser)

    #action
    def click_HomeLoginBtn(self,account,password):
        if self.element_IsExit(self.homeLoginBtn_loc):
            self.click(self.homeLoginBtn_loc)
            self.input_account(account)
            self.input_passwd(password)
            self.click_LoginSubmit('沙小僧-取金路上 小沙为您保驾护航')
        else:
            print('已登录')


if __name__ == '__main__':
    home = home_Page('ff')
    home.open('https://pc.shaxiaoseng.com:4433')
    home.click_HomeLoginBtn('13511111105','111111')