#
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Firefox()
driver.get('https://pc.shaxiaoseng.com:4433/Product/index.html')

s=driver.find_elements(By.CLASS_NAME,'list_c_l_1')
for i in s:
    print (type(i))
print(s)