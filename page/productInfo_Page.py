from selenium import webdriver
import  Base_Page
class productInfo_page(Base_Page.Action):
    globals()
    def __init__(self, selenium_driver, base_url, pagetitle):
        super(productInfo_page, self).__init__(selenium_driver, base_url, pagetitle)

