from page.Home_Page import  Home_Page

class rechare_Page(Home_Page):
    # 充值页面
    quickRecharge_loc='xpath=>/html/body/div[4]/div[1]' #快捷充值按钮
    netRecharge_loc='xpath=>/html/body/div[4]/div[2]' #网银充值
    rechargeMoney_loc='id=>money' # 充值金额
    immediatelyRechargeBtn_loc='class=>cz-btn1' #立即充值按钮


    def __init__(self, driver):
        super(rechare_Page, self).__init__(driver)

    #充值页面操作
    def input_RechargeMoney(self,money):
        self.input(self.rechargeMoney_loc,money)


