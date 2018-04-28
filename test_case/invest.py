import SBConfirmBuy_Page
from selenium import webdriver

def invest_SB(dealNo,account,passwd,money,xinWangPasswd):
    driver = webdriver.Firefox()
    page = SBConfirmBuy_Page.sbConfimBuy_page(driver)
    page.open('https://pc.shaxiaoseng.com:4433/Product/index.html')
    dealNo = dealNo +'期'
    #找到所投资的标的，并进入标的详情页
    page.pick_element(dealNo)
    page.clickBuyBtn(account,passwd,money)
    page.click_ConfirmBuyBtn(xinWangPasswd)

if __name__ == '__main__':
    dealNo='CY18041397151'
    account='13511111105'
    passwd='111111'
    xinWangPd='111111'
    money='100'
    invest_SB(dealNo,account,passwd,money,xinWangPd)

