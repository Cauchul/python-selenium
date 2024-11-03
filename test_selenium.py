import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\work\python-selenium\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 打开百度搜索首页
driver.get("https://www.baidu.com")

# 找到搜索框元素并输入关键词
search_box = driver.find_element(By.ID, "kw")
search_box.send_keys("Python Selenium")

# 找到并点击搜索按钮
search_button = driver.find_element(By.ID, "su")
search_button.click()

# 等待几秒钟以查看结果
time.sleep(5)

# 关闭浏览器
driver.quit()
