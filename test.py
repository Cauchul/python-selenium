import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = r'D:\work\python-selenium\chromedriver-win64\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.baidu.com')  # 打开网页

## 打开百度，获取标签内容
res_text = driver.find_element(By.XPATH, '//*[@id="s-top-left"]/a[1]').text
print(f'获取到得text为：{res_text}')

element = driver.find_element(By.NAME, 'wd')
element.send_keys('好看得电影推荐')
sub = driver.find_element(By.XPATH, '//*[@id="su"]')
sub.click()
time.sleep(1)
#  滑动页面到底
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

ActionChains(driver).send_keys(Keys.END).perform()

time.sleep(2)

driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

driver.find_element(By.ID, 'submitBTN').click()
time.sleep(10)

# driver.back()
# time.sleep(1)
# element = driver.find_element(By.NAME, 'wd')
# element.clear()
# element.send_keys('csdn')
# time.sleep(1)
# sub = driver.find_element(By.XPATH, '//*[@id="su"]')
# sub.click()
#
# driver.execute_script('window.open()')
# print(driver.window_handles)
#
# driver.switch_to.window(driver.window_handles[1])
# driver.get('http://www.taobao.com')
# time.sleep(1)
# driver.get('http://www.zhihu.com')
# time.sleep(1)
#
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)

driver.close()
