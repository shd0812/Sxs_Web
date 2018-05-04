from page.Home_Page import  Home_Page

class ProductList_Page(Home_Page):
		
		def __init__(self, browser):
			super(ProductList_Page, self).__init__(browser)

		# 获取产品列表 有用数据 仅四方化缘
		def get_ProductInfo(self, dealNo):
			dlList = self.get_element("stag=>dl")
			for element in dlList:
				try:
					productNumberSpan = element.find_element_by_css_selector("dt span")
					# 判断产品编号
					print(productNumberSpan.text,dealNo)
					if productNumberSpan.text == dealNo:
						remain_MoneyCss=element.find_element_by_css_selector("dd h4")
						# remain_Money 剩余金额
						remain_Money = remain_MoneyCss.find_element_by_class_name('list_c_dd_p2').text
						remain_Money=remain_Money[9:len(remain_Money)]
						# 年华利率
						rate=element.find_element_by_css_selector("dd h2 p").text
						# 项目期限
						month=element.find_element_by_css_selector("dd h3 p").text
						#按钮名字
						sub_Name=element.find_element_by_css_selector("dd h5 a").text
						print(remain_Money,rate,month,sub_Name)
						return rate,month,remain_Money,sub_Name
					else:
						print('请检查标的号是否正确')
				except:
					print('异常')
		

		
if __name__ == '__main__':
	url = 'https://www.shaxiaoseng.com/Product/index.html'
	page = ProductList_Page('ff')
	page.open(url)
	page.get_ProductInfo('XY18042117495期')
			