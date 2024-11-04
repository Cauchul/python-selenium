from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get(r'https://www.baidu.com')

logo = browser.find_element(By.CLASS_NAME, 'index-logo-src')
# 获取标签的id
print(logo.id)
# 获取标签的位置
print(logo.location)
# 获取标签的标签名
print(logo.tag_name)
# 获取标签的大小
print(logo.size)

# 关闭浏览器
browser.close()
