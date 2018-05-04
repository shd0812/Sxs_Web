import selenium.common.exceptions
from selenium import webdriver
from base.Base_Log import myLog
from base.Base_Page import Action
from utils import operate_file


class operation_Element(Action):
    def __init__(self,driver):
        super(operation_Element, self).__init__(driver)


    def operate(self,logTest,testInfo,case_dic,check):

        try:
            for case in case_dic:
                info = str(case['info']+'-'+case['operte_type'])
                logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)
                if 'pick_dealNo' == case['operte_type']:
                    self.pick_element(case['deal_no'])
                elif  'click' == case['operte_type']:
                    self.click(case['element_info'])
                elif 'input' == case['operte_type']:
                    self.input(case['element_info'], case['msg'])
                elif 'open_new_window' == case['operte_type']:
                    self.open_new_window(case['element_info'])
                else:
                    print(4444)


        except selenium.common.exceptions.TimeoutException:
            dic={"result": False, "type": '寻找元素超时'}
            logTest.screenshotERROR(self,'寻找元素超时')
            return dic
        finally:
            self.check_Points(check, logTest, test_info)


            #raise Exception
    def check_Points(self,check,logTest,testInfo):
        title=self.get_title()
        if title == check['check_title']:
            logTest.buildEndLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + '测试通过')
        else:
            logTest.buildEndLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + '测试失败')


if __name__ =='__main__':
    f= operate_file('D:\\Python\\Sxs_Web\\test_data\\invest.yaml')
    result = f.open()
    test_case = result['testcase']
    test_info=result['testinfo']
    check = result['check'][0]

    logTest = myLog.getLog("fireFox")
    driver = webdriver.Firefox()
    page = operation_Element(driver)
    page.open('https://pc.shaxiaoseng.com:4433/Product/index.html')
    page.operate(logTest,test_info,test_case,check)


