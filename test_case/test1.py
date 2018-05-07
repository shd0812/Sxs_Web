from page.SBConfirmBuy_Page import sbConfimBuy_page
from page.loginPage import LoginPage
import unittest
from base.Base_Log import myLog
from base.Base_Operation import operation_Element,getTestData
from selenium import webdriver

#import HTMLTestRunner

class TestOne(unittest.TestCase):
    def setUp(self):
        #self.driver=webdriver.Firefox()
        self.logTest = myLog.getLog("Chrome")
        driver = webdriver.Chrome()
        self.page = operation_Element(driver)
    def test_Login_1(self):
        result = getTestData('D:/Python/Sxs_Web/test_data/login/login.yaml')
        self.page.open(result[0]['url'])
        self.page.operate(self.logTest, result[0], result[1], result[2])




    def test_Tender(self):
        result = getTestData('D:/Python/Sxs_Web/test_data/invest/invest.yaml')
        self.page.open(result[0]['url'])
        self.page.operate(self.logTest, result[0], result[1], result[2])


    def tearDown(self):
        self.page.close()

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
