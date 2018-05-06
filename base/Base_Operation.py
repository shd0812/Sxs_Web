import selenium.common.exceptions
from selenium import webdriver
from base.Base_Log import myLog
from base.Base_Page import Action
from utils import operate_file


def getTestData(filename):
    testData=[]
    path=filename
    result_f=operate_file(path)
    result = result_f.open()
    test_case = result['testcase']
    test_info=result['testinfo'][0]
    check = result['check'][0]
    testData.append(test_info)
    testData.append(test_case)
    testData.append(check)
    return testData

class operation_Element(Action):
    def __init__(self,driver):
        super(operation_Element, self).__init__(driver)

    def operate(self,logTest,testInfo,case_dic,check):
        try:
            for case in case_dic:
                info = str(case['info']+'-'+case['operte_type'])
                logTest.buildStartLine(testInfo["id"] + "_" + testInfo["title"] + "_" + info)
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

            return dic
        finally:
            self.check_Points(check, logTest, testInfo)


            #raise Exception
    def check_Points(self,check,logTest,testInfo):
        title=self.get_title()
        if title == check['check_title']:
            logTest.buildEndLine(testInfo["id"] + "_" + testInfo["title"] + "_" + '测试通过')
        else:
            fail_reason={
                'expect':check['check_title'],
                'now':title
            }
            logTest.screenshotERROR(self, testInfo['title'] + '寻找元素超时')
            fail_reason=str(fail_reason)
            logTest.buildEndLine(testInfo["id"] + "_" + testInfo["title"] + "_" + '测试失败'+'_'+'失败原因'+fail_reason)


if __name__ =='__main__':
    result=getTestData('D:/my_python/Sxs_Web/test_data/recharge/recharge.yaml')
    test_case = result[1]
    test_info=result[0]
    check = result[2]
    print(test_info)
    logTest = myLog.getLog("fireFox")
    driver = webdriver.Firefox()
    page = operation_Element(driver)
    page.open(test_info['url'])
    page.operate(logTest,test_info,test_case,check)


