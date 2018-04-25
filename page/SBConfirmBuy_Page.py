import productInfo_Page
import assert_util
# 散标确认购买页
class sbConfimBuy_page(productInfo_Page.productInfo_page):
    confirmBuyBtn_loc='id=>buy-btn'
    sbInfo_loc='id=>/html/body/div[3]/div/div[2]/h2/i/a/span'
    agreeBtn_loc='/html/body/div[3]/div/div[2]/div/div[9]/img'
    lookBorrowList_loc='class=>btn'
    continueBtn_loc='class=>notes'
    #新网页面元素
    xinWangPassword_loc='id=>password'
    xinWangBtn_loc='id=>nextButton'

    def __init__(self, browser):
        super(sbConfimBuy_page, self).__init__(browser)

    #点击确认支付按钮  交易密码
    def click_ConfirmBtn(self,password):
        #切换到新网页面
        self.open_new_window(self.confirmBuyBtn_loc)
        #输入交易密码
        self.input(self.xinWangPassword_loc,password)
        #点击确认按钮
        self.click(self.xinWangBtn_loc)
        assert_util.sleep(5)



    #继续出借按钮
    def click_ContinueBtn(self):
        self.click(self.continueBtn_loc)
    # 查看出借记录
    def click_BorrowList(self):
        self.click(self.borrowerInfo_loc)
if __name__ == '__main__':
    url='https://pc.shaxiaoseng.com:4433/Sanbiao/details/id/6197.html'
    page = sbConfimBuy_page('ff')
    page.open(url)
    page.inputInvest_Money(100)
    page.clickBuyBtn()
    page.click_ConfirmBtn('111111')


