import productInfo_Page

# 散标确认购买页
class sbConfimBuy_page(productInfo_Page.productInfo_page):
    confirmBuyBtn_loc='id=>buy-btn'
    sbInfo_loc='id=>/html/body/div[3]/div/div[2]/h2/i/a/span'
    agreeBtn_loc='/html/body/div[3]/div/div[2]/div/div[9]/img'


    def __init__(self, browser):
        super(sbConfimBuy_page, self).__init__(browser)

    #点击确认支付按钮
    def click_ConfirmBtn(self):
        self.click(self.confirmBuyBtn_loc)
        print(self.get_url())

if __name__ == '__main__':
    url='https://pc.shaxiaoseng.com:4433/Sanbiao/details/id/6236.html'
    page = sbConfimBuy_page('ff')
    page.open(url)
    page.getRemain_Money()
    page.inputInvest_Money(100)
    page.clickBuyBtn()
    page.click_ConfirmBtn()


