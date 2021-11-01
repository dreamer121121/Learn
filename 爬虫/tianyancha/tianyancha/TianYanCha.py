# coding = utf-8
import os
import urllib.request
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from multiprocessing import Pool


class TianYanCha(object):
	"""docstring for TianYanCha"""
	def __init__(self, sucPath, failedPath):
		super(TianYanCha, self).__init__()
		'''初始化查询结果的存储文件'''

		chrom_options = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(chrome_options=chrom_options)

		self.url = "https://www.tianyancha.com/"
		self.username = '13051462891'
		self.password = 'hu013579'
		self.login()

		print("======login succeed and begin search=====")
		self.fileSuc = open(sucPath, 'a')
		self.fileFailed = open(failedPath, 'a+')
		#self.getCompanyByName("北京创业光荣信息科技有限责任公司")

		self.flag = True
		self.setOutput()

	def login(self):
		self.driver.get(self.url)
		# 模拟登陆

		loginLink = WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_xpath('//a[text()="登录/注册"]'))
		loginLink.click()

		login_by_pwd = WebDriverWait(self.driver, 30).until(lambda x: x.find_element_by_xpath('//div[text()="密码登录"]'))
		login_by_pwd.click()

		username = self.driver.find_element_by_id('mobile')
		username.send_keys(self.username)

		password = self.driver.find_element_by_id("password")
		password.send_keys(self.password)

		login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="登录"]')))

		print(login_button.text)
		time.sleep(30)

	def setOutput(self):
		f = open('compny_list.txt', 'r')
		data = f.readlines()
		f.close()

		self.fileFailed.seek(0)
		fail_data = self.fileFailed.readlines()
		start = int(fail_data[-1].split(' ')[-1]) if fail_data else 0
		print('resume: ', start)

		for index in range(start, len(data)):
			name = data[index]
			try:
				name = name.replace('\n', "")
				self.getCompanyByName(name)
				time.sleep(random.randint(2, 10))
			except Exception as e:
				print("---error---", e)
				self.fileFailed.write(name+' '+str(index)+'\n')
				self.fileFailed.flush()
				import sys
				sys.exit(0)

		self.fileSuc.write("========Finish all ========")
		self.fileSuc.flush()

	def postprocess(self, time, company, before, after):
		before = before.replace(' ', '')
		after = after.replace(' ', '')
		self.fileSuc.write(time+','+company+','+before+','+after)
		self.fileSuc.write('\r')
		self.fileSuc.flush()

	def getinfo(self, company):
		changeinfo = self.driver.find_element_by_id("_container_changeinfo")
		tbody = changeinfo.find_element_by_tag_name("tbody")
		tr_list = tbody.find_elements_by_tag_name("tr")
		for tr in tr_list:
			td_list = tr.find_elements_by_tag_name("td")
			change_time = td_list[1].text
			change_item = td_list[2].find_element_by_tag_name("div").text
			if change_item == "住所":
				before = td_list[3].find_element_by_tag_name("p").text
				after = td_list[4].find_element_by_tag_name("p").text
				print("time: ", change_time)
				print("before: ", before)
				print("after: ", after)
				self.postprocess(change_time, company, before, after)

	def getCompanyByName(self, company):
		"""
		get infor for one company
		"""
		print("---company----", company)
		url = 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % urllib.parse.quote(company)
		print('---url---', url)
		self.driver.get(url)
		self.driver.implicitly_wait(10)
		spans = self.driver.find_elements_by_css_selector('div[class=\"result-list sv-search-container\"]')
		print('---company list---', len(spans))

		if len(spans) > 0:
			self.flag = True
			href_list = self.driver.find_elements_by_css_selector('a[class=\"name  \"]')
			if len(href_list) > 0:
				for href in href_list:
					if href.find_element_by_tag_name("em").text == company:
						url = href.get_attribute('href')

						# 进入公司页面
						self.driver.get(url)
						self.driver.implicitly_wait(10)

						#获取总共变更信息条数
						theader = self.driver.find_element_by_id("nav-main-changeCount")
						nums = theader.find_element_by_css_selector('span[class=\"data-count\"]').text
						print('Total change info nums: ', nums)
						pages = (int(nums) // 10) + 1 if ((int(nums)%10) != 0) else (int(nums) // 10)
						print("Total Pages: ", pages)

						for page in range(1, pages+1):
							print("current page: ", page)
							if page != 1:
								#需要跳页
								print('----跳页---')
								# Link_father = changeinfo.find_element_by_css_selector('ul[class=\"pagination\"]')
								# Link = Link_father.find_element_by_xpath('//a[text()=\"'+str(page)+'\"]')
								# print('---link.text---', Link.text)
								time.sleep(3)
								# js = 'document.getElementById(\"_container_changeinfo\").getElementsByClassName(\"pagination\")[0]' \
								# 	 '.getElementsByClassName(\"num \")['+str(page-2)+'].click();' \
								nextpage = page if page != 2 else 1
								js = 'document.getElementById(\"_container_changeinfo\").getElementsByClassName(\"pagination\")[0]' \
								 	 '.getElementsByTagName(\"li\")['+str(nextpage)+'].getElementsByTagName(\"a\")[0].click();' \
								#启示：采用selinum获取元素进行click操作还需要进一步解决问题(被其他元素覆盖的问题)，目前看直接采用js语法获取元素进行点击操作Bug会较少

								self.driver.execute_script(js)
								time.sleep(3) #这里很重要:若翻页还没结束，就进入到getinfo程序，会导致拿不到DOM，此处还可以进行优化

							#获取当前这一页的变更信息
							self.getinfo(company)
							time.sleep(random.randint(1, 3))
					else:
						continue
					break
			else:
				print('======end========')
		else:
			self.flag = False
			if not self.flag:
				print("=====> 人工验证 ")
				self.getCompanyByName(company)
				time.sleep(5)

	def __del__(self):
			print('dle phantomjs')
			self.fileSuc.close()
			self.fileFailed.close()
			self.driver.quit()


def main():
	# f = open('suc.txt','w')
	# f.close()
	# f = open('fail.txt','w')
	# f.close()

	query = TianYanCha('./suc.txt', './fail.txt')
	#query.getCompanyByName('北京希嘉万维科技有限公司')


if __name__ == '__main__':
	main()
