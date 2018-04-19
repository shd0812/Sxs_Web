# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import	utils
import time

class Action(object):
	'''
		Pyse framework for the main class, the original
	selenium provided by the method of the two packaging,
	making it easier to use.
	'''

	original_window = None

	def __init__(self, selenium_driver,base_url='https://pc.shaxiaoseng.com:4433',pagetitle='登录'):
		'''
		Run class initialization method, the default is proper
		to drive the Firefox browser. Of course, you can also
		pass parameter for other browser, Chrome browser for the "Chrome",
		the Internet Explorer browser for "internet explorer" or "ie".
		'''
		self.base_url=base_url
		self.pagetitle = pagetitle
		self.driver = selenium_driver
		# if browser == "firefox" or browser == "ff":
			# self.driver = webdriver.Firefox()
		# elif browser == "chrome":
			# self.driver = webdriver.Chrome()
		# elif browser == "internet explorer" or browser == "ie":
			# self.driver = webdriver.Ie()
		# elif browser == "opera":
			# self.driver = webdriver.Opera()
		# elif browser == "chrome_headless":
			# chrome_options = Options()
			# chrome_options.add_argument('--headless')
			# self.driver = webdriver.Chrome(chrome_options=chrome_options)
		# elif browser == 'edge':
			# self.driver = webdriver.Edge()
		# else:
			# raise NameError(
				# "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)

	def element_wait(self, by, value, secs=5):
		'''
		Waiting for an element to display.
		'''
		if by == "id":
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
		elif by == "name":
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
		elif by == "class":
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
		elif by == "link_text":
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
		elif by == "xpath":
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
		elif by == "css": #presence_of_all_elements_located
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
		elif by == "tag": #presence_of_all_elements_located
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.TAG_NAME, value)))
		elif by == "stag": #presence_of_all_elements_located
			WebDriverWait(self.driver, secs, 1).until(EC.presence_of_all_elements_located((By.TAG_NAME, value)))
		else:
			raise NoSuchElementException(
				"Not find element, Please check the syntax error.")

	def get_element(self, css):
		'''
		Judge element positioning way, and returns the element.
		'''
		if "=>" not in css:
			by = "css"
			value = css
			# wait element.
			self.element_wait(by, css)
			
		else:
			by = css.split("=>")[0]
			value = css.split("=>")[1]
			if by == "" or value == "":
				raise NameError(
					"Grammatical errors,reference: 'id=>useranme'.")
			self.element_wait(by, value)
		print(by)
		if by == "id":
			element = self.driver.find_element_by_id(value)
		elif by == "name":
			element = self.driver.find_element_by_name(value)
		elif by == "class":
			element = self.driver.find_element_by_class_name(value)
		elif by == "link_text":
			element = self.driver.find_element_by_link_text(value)
		elif by == "xpath":
			element = self.driver.find_element_by_xpath(value)
		elif by == "css":
			element = self.driver.find_element_by_css_selector(value)
		elif by== "tag":
			print(by)
			element = self.driver.find_element_by_tag_name(value)
		elif by=='stag':
			
			element = self.driver.find_elements_by_tag_name(value)
		else:
			raise NameError(
				"Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
		return element
	
	def _open(self, url, pagetitle):
		self.driver.get(url)
		self.driver.maximize_window()
		#使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
		assert self.on_page(pagetitle), u"打开开页面失败 %s"% url
		
	#使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
	def on_page(self, pagetitle):
		return pagetitle in self.driver.title
	
	def open(self):
		'''
		open url.

		Usage:
		driver.open("https://www.baidu.com")
		'''
		self._open(self.base_url, self.pagetitle)

	def max_window(self):
		'''
		Set browser window maximized.

		Usage:
		driver.max_window()
		'''
		self.driver.maximize_window()
	
	
	def set_window(self, wide, high):
		'''
		Set browser window wide and high.

		Usage:
		driver.set_window(wide,high)
		'''
		self.driver.set_window_size(wide, high)

	def type(self, css, text):
		'''
		Operation input box.

		Usage:
		driver.type("css=>#el","selenium")
		'''
		el = self.get_element(css)
		el.send_keys(text)

	def clear(self, css):
		'''
		Clear the contents of the input box.

		Usage:
		driver.clear("css=>#el")
		'''
		el = self.get_element(css)
		el.clear()

	def click(self, css):
		'''
		It can click any text / image can be clicked
		Connection, check box, radio buttons, and even drop-down box etc..

		Usage:
		driver.click("css=>#el")
		'''
		el = self.get_element(css)
		el.click()

	def right_click(self, css):
		'''
		Right click element.

		Usage:
		driver.right_click("css=>#el")
		'''
		el = self.get_element(css)
		ActionChains(self.driver).context_click(el).perform()

	def move_to_element(self, css):
		'''
		Mouse over the element.

		Usage:
		driver.move_to_element("css=>#el")
		'''
		el = self.get_element(css)
		ActionChains(self.driver).move_to_element(el).perform()

	def double_click(self, css):
		'''
		Double click element.

		Usage:
		driver.double_click("css=>#el")
		'''
		el = self.get_element(css)
		ActionChains(self.driver).double_click(el).perform()

	def drag_and_drop(self, el_css, ta_css):
		'''
		Drags an element a certain distance and then drops it.

		Usage:
		driver.drag_and_drop("css=>#el","css=>#ta")
		'''
		element = self.get_element(el_css)
		target = self.get_element(ta_css)
		ActionChains(self.driver).drag_and_drop(element, target).perform()

	def click_text(self, text):
		'''
		Click the element by the link text

		Usage:
		driver.click_text("新闻")
		'''
		self.driver.find_element_by_partial_link_text(text).click()

	def close(self):
		'''
		Simulates the user clicking the "close" button in the titlebar of a popup
		window or tab.

		Usage:
		driver.close()
		'''
		self.driver.close()

	def quit(self):
		'''
		Quit the driver and close all the windows.

		Usage:
		driver.quit()
		'''
		self.driver.quit()

	def submit(self, css):
		'''
		Submit the specified form.

		Usage:
		driver.submit("css=>#el")
		'''
		el = self.get_element(css)
		el.submit()

	def F5(self):
		'''
		Refresh the current page.

		Usage:
		driver.F5()
		'''
		self.driver.refresh()

	def js(self, script):
		'''
		Execute JavaScript scripts.

		Usage:
		driver.js("window.scrollTo(200,1000);")
		'''
		self.driver.execute_script(script)

	def get_attribute(self, css, attribute):
		'''
		Gets the value of an element attribute.

		Usage:
		driver.get_attribute("css=>#el","type")
		'''
		el = self.get_element(css)
		return el.get_attribute(attribute)

	def get_text(self, css):
		'''
		Get element text information.

		Usage:
		driver.get_text("css=>#el")
		'''
		el = self.get_element(css)
		return el.text

	def get_display(self, css):
		'''
		Gets the element to display,The return result is true or false.

		Usage:
		driver.get_display("css=>#el")
		'''
		el = self.get_element(css)
		return el.is_displayed()

	def get_title(self):
		'''
		Get window title.

		Usage:
		driver.get_title()
		'''
		return self.driver.title
		
		#产品列表专用
	def pick_element(self,dealNo):
		dlList = self.get_element("stag=>dl")
		for element in dlList:
			try: 
				productNumberSpan = element.find_element_by_css_selector("dt span")
				#判断产品编号
				if productNumberSpan.text ==dealNo:
					element.find_element_by_css_selector("dd h5 a").click()
			except  :
				print('异常'  )
			finally:
				print('继续')
	
	def get_url(self):
		'''
		Get the URL address of the current page.

		Usage:
		driver.get_url()
		'''
		return self.driver.current_url

	def get_alert_text(self):
		'''
		Gets the text of the Alert.

		Usage:
		driver.get_alert_text()
		'''
		return self.driver.switch_to.alert.text

	def get_window_img(self, file_path):
		'''
		Get the current window screenshot.

		Usage:
		driver.get_window_img()
		'''
		self.driver.get_screenshot_as_file(file_path)

	def wait(self, secs):
		'''
		Implicitly wait.All elements on the page.

		Usage:
		driver.wait(10)
		'''
		self.driver.implicitly_wait(secs)

	def accept_alert(self):
		'''
		Accept warning box.

		Usage:
		driver.accept_alert()
		'''
		self.driver.switch_to.alert.accept()

	def dismiss_alert(self):
		'''
		Dismisses the alert available.

		Usage:
		driver.dismiss_alert()
		'''
		self.driver.switch_to.alert.dismiss()

	def switch_to_frame(self, css):
		'''
		Switch to the specified frame.

		Usage:
		driver.switch_to_frame("css=>#el")
		'''
		iframe_el = self.get_element(css)
		self.driver.switch_to.frame(iframe_el)

	def switch_to_frame_out(self):
		'''
		Returns the current form machine form at the next higher level.
		Corresponding relationship with switch_to_frame () method.

		Usage:
		driver.switch_to_frame_out()
		'''
		self.driver.switch_to.default_content()

	def open_new_window(self, css):
		'''
		Open the new window and switch the handle to the newly opened window.

		Usage:
		driver.open_new_window("link_text=>注册")
		'''
		original_window = self.driver.current_window_handle
		el = self.get_element(css)
		el.click()
		all_handles = self.driver.window_handles
		for handle in all_handles:
			if handle != original_window:
				self.driver.switch_to.window(handle)

	def get_screenshot(self, file_path):
		'''Saves a screenshot of the current window to a PNG image file.

		Usage:
		driver.get_screenshot('/Screenshots/foo.png')
		'''
		self.driver.get_screenshot_as_file(file_path)

	def select(self, css, value):
		'''
		Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
		then an UnexpectedTagNameException is thrown.

		:Args:
		 - css - element SELECT element to wrap
		 - value - The value to match against

		Usage:
			<select name="NR" id="nr">
				<option value="10" selected="">每页显示10条</option>
				<option value="20">每页显示20条</option>
				<option value="50">每页显示50条</option>
			</select>

			driver.select("#nr", '20')
			driver.select("xpath=>//[@name='NR']", '20')
		'''
		el = self.get_element(css)
		Select(el).select_by_value(value)


if __name__ == '__main__':
	driver =webdriver.Firefox()
	login = Action(driver,'https://www.shaxiaoseng.com/Product/index.html','四方化缘列表_沙小僧官网')
	login.open()
	login.pick_element("XY18041953439期")
	# print(login.get_title())
	# #driver.click("link_text=>登录")
	# operate_file = utils.operate_file('test_data/login.yaml')
	# data = operate_file.open()
	# print(data)
	# login.type(utils.ob_element(data,0),'13521137793')
	# login.type(utils.ob_element(data,1), '111111')
	# login.click(utils.ob_element(data,2))
	
	# print(login.get_url())
	#
	
	