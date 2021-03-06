from  page.productList_Page import  ProductList_Page
from selenium import webdriver
# 散标详情页
class productInfo_page(ProductList_Page):
    #定位器  # 剩余金额
    remainMoney_loc='xpath=>/html/body/div[3]/div[2]/div[2]/div/div/p[1]/span'
    #右上角登录 用来判断是否是登录状态
    isLogin_loc='xpath=>/html/body/div[1]/div/div[2]/div[3]/span/a[1]'
    #输入框左侧减号按钮
    leftBtn_loc='class=>reduce-j'
    # 金额输入框
    moneyInput_loc='xpath=>//*[@id="form"]/input[2]'
    # 输入框右侧侧减号按钮
    rightBtn_loc='class=>add-j'
    # 立即加入那妞
    submitBtn_loc='class=>btn-j'
    #项目详情
    projectInfo_loc='xpath=>/html/body/div[3]/div[4]/ul/li[1]'
    #借款人信息
    borrowerInfo_loc='xpath=>/html/body/div[3]/div[4]/ul/li[2]'
    # 出借记录
    lendRecord_loc='xpath=>/html/body/div[3]/div[4]/ul/li[3]'
    #输入框下的提示信息
    msg='xpath=>/html/body/div[3]/div[2]/div[2]/div/div/p[3]/span'


    # 检查字段
    expect_title='四方化缘详情'
    def __init__(self, driver):
        super(productInfo_page, self).__init__(driver)

    #获取剩余金额
    def getRemain_Money(self):
        money = self.get_text(self.remainMoney_loc)
        money = money[0:len(money) - 3]
        if ',' in money:
            money=money.replace(',','')
        return  int(money)
    # 输入投资金额
    def inputInvest_Money(self,money):


        remain_money = self.getRemain_Money()
        #判断是否大于所剩金额
        if int(money) > remain_money:
            self.input(self.moneyInput_loc, money)
            #判断如果存在提示信息，则输入金额等于所剩金额
            if self.element_IsExit(self.msg):
                mymoney = str(remain_money)
                self.F5()
                self.input(self.moneyInput_loc, mymoney)
            else:
                raise Exception
        #是否小于100
        elif int(money)<100:
            #判断如果存在提示信息，则输入金额等于所剩金额
            if self.element_IsExit(self.msg):
                mymoney = str(remain_money)
                self.input(self.moneyInput_loc, mymoney)
            else:
                raise Exception
        elif int(money)%100 !=0:
            #判断如果存在提示信息，则输入金额等于所剩金额
            if self.element_IsExit(self.msg):
                mymoney = str(remain_money)
                self.input(self.moneyInput_loc, mymoney)

            else:
                raise Exception
        else:
            self.input(self.moneyInput_loc,money)

    #点击立即加入按钮 如果没登录，则输入账号，密码，金额
    def clickBuyBtn(self,account,passwd,money):
        if self.element_IsExit(self.isLogin_loc):
            self.inputInvest_Money(money)
            self.click(self.submitBtn_loc)
            self.input_account(account)
            self.input_passwd(passwd)
            self.click_LoginSubmit(self.expect_title)
            self.inputInvest_Money(money)
            self.click(self.submitBtn_loc)

        else:
            self.inputInvest_Money(money)
            self.click(self.submitBtn_loc)

    # 查看项目详情 借款人信息 出借记录 1,2,3
    def viewProjectInfo(self,type):
        if type ==1:
            self.click(self.projectInfo_loc)
        elif type==2:
            self.click(self.borrowerInfo_loc)
        else:
            self.click(self.lendRecord_loc)




if __name__ == '__main__':
    url = 'https://pc.shaxiaoseng.com:4433/Sanbiao/details/id/6284.html'
    #url='https://www.shaxiaoseng.com/Sanbiao/details/id/3691.html'

    driver = webdriver.Firefox()
    page = productInfo_page(driver)
    page.open(url)



    account='13511111105'
    passwd='111111'
    money=300
    page.clickBuyBtn(account,passwd,money)
    #page.viewProjectInfo(2)

