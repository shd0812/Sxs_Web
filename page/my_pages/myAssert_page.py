from page.Home_Page import  Home_Page
import utils
from selenium import webdriver

class myAssert_page(Home_Page):
    #元素定位
     #左侧导航
    deposit_loc=''#存管按钮
    ca_loc='' #ca按钮
    car_loc='' #绑卡按钮

    myAssert_loc='' #我的资产
    siFang_loc='' #四方化缘记录
    zhaiQuan_loc='' #债权出让记录
    fundsFlow_loc='' #资金流水记录
    personalData_loc='' #个人资料
    myRedPack_loc='' #我的红包
    inviteCash_loc='' #邀请返现

    #我的资产页面
    totalAssert_loc='' #总资产
    rechargeRecord_loc='' #充值记录
    withdrawRecord_loc=''#提现记录
    #availableBalance_str='可用余额'#可用金额
    #freeze_loc='冻结金额'#冻结金额
    rechargeBtn_loc='class=>recharge'#充值按钮
    withdrawBtn_loc='class=>withdraw'#提现按钮



    # 提现页面


    def __init__(self, driver):
        super(myAssert_page, self).__init__(driver)

    #获取可用金额 和冻结金额 p_title 可以是可用余额 或者冻结金额
    def myAssertGet_element(self,p_title):
        pList=self.get_element('class=>sum').find_elements_by_tag_name('p')
        for element in pList:
            p=element.text
            if p_title in p:
                print(p)
                return utils.extractNum(p)
            else:
                pass

    def myAssertClick_RechargeBtn(self):
        self.jump_page(self.rechargeBtn_loc,'充值')
        #self.open_new_window(self.quickRecharge_loc)
        #page = recharge.reCharge_Page('ff')




    def myAssertClick_WithdrawBtn(self):
        self.jump_page(self.withdrawBtn_loc,'提现')



if __name__=='__main__':
    driver =webdriver.Firefox()
    page=myAssert_page(driver)
    page.open('https://www.shaxiaoseng.com/User/my')
    page.input_account('13521137793')
    page.input_passwd('111111')
    page.click_LoginSubmit('我的账户_我的资产_沙小僧官网')
    page.myAssertClick_RechargeBtn()