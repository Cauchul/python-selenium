from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

service = Service(executable_path='D:\work\python-selenium\chromedriver-win64\chromedriver.exe')
browser = webdriver.Chrome(service=service)

# 打开百度
browser.get('http://www.baidu.com')
time.sleep(1)
# 新建一个选项卡
browser.execute_script('window.open()')
print(browser.window_handles)
# 跳转到第二个选项卡并打开知乎
browser.switch_to.window(browser.window_handles[1])
browser.get('http://www.zhihu.com')
# 回到第一个选项卡并打开淘宝（原来的百度页面改为了淘宝）
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get('http://www.taobao.com')
