from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
time.sleep(2)

browser.switch_to.frame('iframeResult')

# 开始位置
source = browser.find_element(By.CSS_SELECTOR, "#draggable")  # 按照id属性来定位元素

# 结束位置
target = browser.find_element(By.CSS_SELECTOR, "#droppable")

# 执行元素的拖放操作
actions = ActionChains(browser)
actions.drag_and_drop(source, target)  # 执行拖拽
actions.perform()
# 拖拽
time.sleep(2)

# 关闭浏览器
browser.close()
