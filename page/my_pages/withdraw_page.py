from page.Home_Page import Home_Page

class withdraw_Page(Home_Page):
    # 提现页面
    avaliableMoney_loc='xpath=>/html/body/div[3]/div/span' #可用余额
    withdrawList_loc='xpath=>/html/body/div[4]/a' #提现记录
    withdrawMoney_loc='id=>money' # 提现金额输入框
    allWithdrawMoney_loc='class=>take-all' #全部提现按钮
    realMoney_loc='xpath=>//*[@id="form_one"]/div[4]/span[2]' #实际到账金额
    feel_loc='xpath=>//*[@id="form_one"]/div[5]/span[2]' #提现手续费
    confirmWithdrawBtn_loc='class=>cz-btn1' #确认提现按钮


    def __init__(self, driver):
        super(withdraw_Page, self).__init__(driver)