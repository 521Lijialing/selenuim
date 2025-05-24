# -*- coding: UTF-8 -*- #
"""
@filename:05 confirm.py
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

driver = gogogo()
driver.get("file:///D:/PyCharm/Py_Projects/01/.venv/confirm.html")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="open-confirm"]').click()
time.sleep(2)
# 获取弹窗的文本内容
alert_text = driver.switch_to.alert.text
print(alert_text)
time.sleep(2)
# 点击弹窗的取消按钮
driver.switch_to.alert.dismiss()
# 点击弹窗的确定按钮
# driver.switch_to.alert.accept()
time.sleep(2)
driver.quit()
