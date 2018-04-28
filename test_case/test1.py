import SBConfirmBuy_Page
import loginPage
import unittest
from selenium import webdriver
import HTMLTestRunner

class TestOne(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()



    def test_Login_1(self):
        page = loginPage.LoginPage(self.driver)
        page.open('https://pc.shaxiaoseng.com:4433/User/login.html')
        print(page.get_title())
        account = '13521137793'
        passwd = '1111112'
        page.input_account(account)
        page.input_passwd(passwd)
        page.click_LoginSubmit('沙小僧-取金路上 1小沙为您保驾护航')



    def test_Tender(self):
        page = SBConfirmBuy_Page.sbConfimBuy_page(self.driver)
        page.open('https://pc.shaxiaoseng.com:4433/Product/index.html')
        #self.page.click_HomeLoginBtn('13511111105','111111')
        page.pick_element('FY180427926163')
        #self.page.click

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例，加入到测试容器中
    test.addTest(TestOne("test_Login_1"))
    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    runner.run(test)

    #定义个报告存放的路径，支持相对路径
    # file_path = "D:\\result.html"
    # with open(file_path,'wb') as f:
    #     # 定义测试报告
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u"百度搜索测试报告", description=u"用例执行情况")
    #     runner.run(test)
