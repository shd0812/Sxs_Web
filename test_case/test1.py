import SBConfirmBuy_Page
import unittest
import HTMLTestRunner

class TestOne(unittest.TestCase):
    def setUp(self):
        self.page = SBConfirmBuy_Page.sbConfimBuy_page('ff')


    def test_Login_1(self):
        self.page.open('https://pc.shaxiaoseng.com:4433')
        self.page.click_HomeLoginBtn('13511111105','111111')


    def test_Tender(self):
        self.page.open('https://pc.shaxiaoseng.com:4433/Product/index.html')
        #self.page.click_HomeLoginBtn('13511111105','111111')
        self.page.pick_element('CY18041397151期')
        #self.page.click

    def tearDown(self):
        self.page.close()

if __name__ == "__main__":
    #定义一个测试容器
    test = unittest.TestSuite()
    #将测试用例，加入到测试容器中
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
