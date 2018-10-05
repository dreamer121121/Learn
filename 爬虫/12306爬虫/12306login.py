from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from urllib.parse import quote
from bs4 import BeautifulSoup
import time


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 1000)  # 最长等待时间
KEYWORLD='iPad'


def login():
    url = 'https://kyfw.12306.cn/otn/login/init'
    finish_url = 'https://kyfw.12306.cn/otn/index/initMy12306'  # 完成登陆后会自动跳转到这个url
    browser.get(url)
    try:
        # browser.find_element_by_id("J_Quick2Static").click()
        time.sleep(2)
        user_name = browser.find_element_by_id('username')
        password = browser.find_element_by_id('password')
        user_name.clear()
        password.clear()
        user_name.send_keys('xt2761564455')
        password.send_keys('211985xt')
        print("-----请手动输入验证码进行登录验证------")
        wait.until(EC.url_to_be(finish_url))
        print("登录成功可以购票了")
    except:
        print('登录失败')


if __name__ == '__main__':
    login()
