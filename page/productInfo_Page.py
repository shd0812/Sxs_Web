from selenium import webdriver
import  Base_Page
import  loginPage

# 散标详情页
class productInfo_page(loginPage.LoginPage):
    #定位器
    remainMoney_loc='xpath=>/html/body/div[3]/div[2]/div[2]/div/div/p[1]/span'
    isLogin_loc='xpath=>/html/body/div[3]/div[2]/div[2]/div/div/p[2]/a'
    leftBtn_loc='class=>reduce-j'
    moneyInput_loc='class=>money-j'
    rightBtn_loc='class=>add-j'
    submitBtn_loc='class=>btn-j'
    def __init__(self, browser):
        super(productInfo_page, self).__init__(browser)
    #判断是否登录
    def isLogin(self):
        login = self.get_text(self.isLogin_loc)
        if login :
            #print('111')
            return  False
        else:
            #print('2222')
            return  True
    #获取剩余金额
    def getRemain_Money(self):
        money = self.get_text(self.remainMoney_loc)

        return  money
    # 输入投资金额 如果不输入则默认输入剩余最大的金额
    def inputInvest_Money(self,money):
        self.input(self.moneyInput_loc,money)

    def clickBtn(self):
        if self.isLogin():
            print('哈哈哈')
            self.click(self.submitBtn_loc)

        else:
            self.click(self.submitBtn_loc)
            print('嘿嘿嘿')
            account='13511111105'
            passwd='111111'
            self.input_account(account)
            print('嘿嘿嘿111')
            self.input_passwd(passwd)
            print('嘿嘿嘿222')
            self.click_LoginSubmit()
            print('嘿嘿嘿333')
            self.inputInvest_Money(100)
            self.click(self.submitBtn_loc)




if __name__ == '__main__':
    url = 'https://pc.shaxiaoseng.com:4433/Sanbiao/details/id/6236.html'


    page = productInfo_page('ff')
    page.open(url)
    page.getRemain_Money()
    page.inputInvest_Money(100)
    page.clickBtn()

