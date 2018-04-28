import productInfo_Page
import assert_util
from selenium import webdriver
# 散标确认购买页
class sbConfimBuy_page(productInfo_Page.productInfo_page):
    # 确认支付按钮
    confirmBuyBtn_loc='id=>buy-btn'
    # 标的详情
    sbInfo_loc='id=>/html/body/div[3]/div/div[2]/h2/i/a/span'
    # 阅读协议按钮
    agreeBtn_loc='/html/body/div[3]/div/div[2]/div/div[9]/img'
    # 购买成功后结果页面
    # 查看出借记录 跳转到散标记录页
    lookBorrowList_loc='class=>btn'
    # 继续出借按钮
    continueBtn_loc='class=>notes'
    #新网页面元素
    xinWangPassword_loc='id=>password'
    xinWangBtn_loc='id=>nextButton'

    def __init__(self, driver):
        super(sbConfimBuy_page, self).__init__(driver)

    #点击确认支付按钮  交易密码
    def click_ConfirmBuyBtn(self,password):
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
    driver =webdriver.Firefox()
    page = sbConfimBuy_page(driver)
    page.open(url)
    page.clickBuyBtn('13511111105','111111',100)
    page.click_ConfirmBuyBtn('111111')


