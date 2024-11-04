from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get(r'https://www.baidu.com')
time.sleep(1)

# 定位到要右击的元素，这里选的新闻链接
right_click = browser.find_element(By.LINK_TEXT, 'hao123')

# 执行鼠标右键操作
ActionChains(browser).context_click(right_click).perform()
time.sleep(1)

# 关闭浏览器
browser.close()
