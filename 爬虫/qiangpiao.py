#author: "xian"
#date: 2018/6/9
#使用selenium是不保存登录信息的（cookies）
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #期望的条件
from selenium.webdriver.common.by import By


class Qiangpiao(object):
      #初始化函数
     def __init__(self):
         self.login_url = 'https://kyfw.12306.cn/otn/login/init'
         self.initmy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
         self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
         self.confirmPassenger = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
         self.driver = webdriver.Chrome() #驱动chrome浏览器进行操作

     def wait_input(self):
          self.from_station = input('出发地：')
          self.to_station = input('目的地：')
          #时间格式一定要对应
          self.depart_time = input('出发时间：')
          #名字一定要存在于常用联系人中间
          self.passengers = input('乘客姓名：（如有多个乘客使用英文逗号分割）').split(',')
          self.trains = input('车次：（如有多个车次使用英文逗号分割）').split(',') #结果[G234，...]

      #_login只想在类中调用
     def _login(self):
          self.driver.get(self.login_url) #打开登录界面
          #显示等待（解释：你与心上人约会，以对方来或不来为等待条件即事件是否发生为条件）
          #隐示等待（解释：你与心上人约会，以等待时间为条件）
          WebDriverWait(self.driver,1000).until(EC.url_to_be(self.initmy_url))
          print('恭喜您，您已登录成功了！')


     def _order_ticket(self):
          #1、跳转到查余票的界面
          self.driver.get(self.search_url)
          #2、等待出发地是否输入正确
          WebDriverWait(self.driver ,1000).until(EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station))
          #3、等待目的地是都输入正确
          WebDriverWait(self.driver, 1000).until(EC.text_to_be_present_in_element_value((By.ID,"toStationText"),self.to_station))
          #4、等待出发日期是否输入正确
          WebDriverWait(self.driver, 1000).until(EC.text_to_be_present_in_element_value((By.ID,"train_date"),self.depart_time))
          #5、等待查询按钮是否可用
          WebDriverWait(self.driver, 1000).until(EC.element_to_be_clickable((By.ID, "query_ticket")))
          #6、如果可以点击找到查询按钮执行点击事件
          searchBotton = self.driver.find_element_by_id("query_ticket")
          searchBotton.click()
          #7、点击查询按钮之后等待车票信息页面被加载完成
          WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH,".//tbody[@id = 'queryLeftTable']/tr")))
          #8、找到所有没有datatrain属性的tr标签
          tr_list = self.driver.find_elements_by_xpath(".//tbody[@id ='queryLeftTable']/tr[not(@datatran)]")
          #9、遍历所有满足条件的tr标签
          for tr in tr_list:
              train_number = tr.find_element_by_class_name('number').text
              if train_number in self.trains:
                  left_ticket = tr.find_element_by_xpath('.//td[3]').text #找到第四个td标签下的文本
                  if left_ticket == '有' or left_ticket.isdigit: #判断输入的车次是否在列表中
                      orderBotton = tr.find_element_by_class_name('btn72')
                      orderBotton.click()

                      #等待是否来到乘客确认页面
                      WebDriverWait(self.driver, 1000).until(EC.url_to_be(self.confirmPassenger))
                      #等待所有的乘客信息被加载完毕
                      WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.XPATH,".//ul[@id = 'normal_passenger_id']/li")))
                      #获取所有的乘客信息
                      passanger_labels = self.driver.find_elements_by_xpath(".//ul[@id = 'normal_passenger_id']/li/label")
                      for passanger_label in passanger_labels: #遍历所有的label标签
                          name = passanger_label.text
                          if name in self.passengers:#判断名字是否与之前输入的名字重合
                              passanger_label.click() #执行点击操作

                              #获取提交订单的按钮
                              submitBotton = self.driver.find_element_by_id('submitOrder_id')
                              submitBotton.click()
                              #显示等待确人订单对话框是否出现
                              WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME,'dhtmlx_wins_body_outer')))
                              #显示等待确认按钮是否加载出现，出现后执行点击操作
                              WebDriverWait(self.driver, 1000).until(EC.presence_of_element_located((By.ID,'qr_submit_id')))
                              ConBotton = self.driver.find_element_by_id('qr_submit_id')
                              ConBotton.click()
                              while ConBotton:
                                  ConBotton.click()
                                  ConBotton = self.driver.find_element_by_id('qr_submit_id')

                              return
     def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()

if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()