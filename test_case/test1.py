from page.SBConfirmBuy_Page import sbConfimBuy_page
from page.loginPage import LoginPage
import unittest
from base.Base_Log import myLog
from base.Base_Operation import operation_Element
from selenium import webdriver
from utils import operate_file
#import HTMLTestRunner

class TestOne(unittest.TestCase):
    def setUp(self):
        #self.driver=webdriver.Firefox()
        self.logTest = myLog.getLog("fireFox")
        driver = webdriver.Firefox()
        self.page = operation_Element(driver)
    def test_Login_1(self):
        f = operate_file('D:/my_python/Sxs_Web/test_data/login.yaml')
        result = f.open()
        print(result)
        test_case = result['testcase']
        test_info = result['testinfo']
        check = result['check'][0]
        self.page.open('https://www.shaxiaoseng.com/User/login.html')
        self.page.operate(self.logTest, test_info, test_case, check)
        # page = LoginPage(self.driver)
        # page.open('https://pc.shaxiaoseng.com:4433/User/login.html')
        # print(page.get_title())
        # account = '13521137793'
        # passwd = '1111112'
        # page.input_account(account)
        # page.input_passwd(passwd)
        # page.click_LoginSubmit('沙小僧-取金路上 小沙为您保驾护航')



    def test_Tender(self):
        f = operate_file('D:/my_python/Sxs_Web/test_data/invest.yaml')
        result = f.open()
        print(result)
        test_case = result['testcase']
        test_info = result['testinfo']
        check = result['check'][0]
        self.page.open('https://www.shaxiaoseng.com/Product/index.html')
        self.page.operate(self.logTest, test_info, test_case, check)
    #     page = sbConfimBuy_page(self.driver)
    #     page.open('https://pc.shaxiaoseng.com:4433/Product/index.html')
    #     #self.page.click_HomeLoginBtn('13511111105','111111')
    #     page.pick_element('FY180427926163')
        #self.page.click

    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例，加入到测试容器中
    test.addTest(TestOne("test_Login_1"))
    test.addTest(TestOne("test_Tender"))
    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    runner.run(test)

    #定义个报告存放的路径，支持相对路径
    # file_path = "D:\\result.html"
    # with open(file_path,'wb') as f:
    #     # 定义测试报告
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u"百度搜索测试报告", description=u"用例执行情况")
    #     runner.run(test)
