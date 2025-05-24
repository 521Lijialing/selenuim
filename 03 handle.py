# -*- coding: UTF-8 -*- #
"""
@filename:03 handle.py
@author:JunLeon
@time:2025-05-08
"""
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from xlwings.mac_dict import elements

def gogogo():
    options = webdriver.EdgeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(30)
    return driver
# driver = webdriver.Edge(executable_path='/path/to/msedgedriver')
# 打开一个网站
driver = gogogo()

driver.get("https://www.baidu.com")

# 定位到上传按钮
upload = driver.find_element(By.XPATH,'//*[@id="uploader"]/div[1]/div[1]/input')
# 要上传的文件的绝对路径
upload.send_keys(r'D:/test.png')
# 元素隐性等待，若加载完毕，则继续执行，否则等待
driver.implicitly_wait(10)

# 切换标签页
# 获取全部标签页句柄
handles= driver.window_handles
# 关闭之前的标签页
driver.close()
# 通过句柄切换标签页
driver.switch_to.window(handles[1])
# 获取当前标签特句柄
handle = driver.current_window_handles

time.sleep(5)
driver.quit()