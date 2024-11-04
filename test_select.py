from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

# url = r'file:///D:\work\python-selenium\html\demo.html'
url = r'D:\work\python-selenium\html\demo.html'

browser = webdriver.Chrome()

browser.get(url)
time.sleep(2)

# 获取下来列表对应的标签
select_tag = browser.find_element(By.NAME, "帅哥")

# 根据索引选择
Select(select_tag).select_by_index("2")
time.sleep(2)
# 根据value值选择
Select(select_tag).select_by_value("草儿")
time.sleep(2)
# 根据文本值选择
Select(select_tag).select_by_visible_text("才哥")
time.sleep(2)

# 关闭浏览器
browser.close()

