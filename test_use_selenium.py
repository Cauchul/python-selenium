import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\work\python-selenium\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# 打开淘宝页面
driver.get(r'https://www.taobao.com')
time.sleep(1)

# 打开百度搜索首页
driver.get("https://www.baidu.com")
time.sleep(1)
# 浏览器截图
# driver.get_screenshot_as_file(r'D:\work\output\截图.png')

try:
    # 刷新页面
    driver.refresh()
    print('刷新页面')
except Exception as e:
    print('刷新失败')

# 后退到百度页面
driver.back()
time.sleep(2)

# 前进到淘宝页面
driver.forward()
time.sleep(2)

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

# test git email
