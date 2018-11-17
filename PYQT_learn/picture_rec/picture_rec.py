# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture_rec.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import time
# import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aip import AipImageClassify
import numpy as np
import os



APP_ID = '14757979'
API_KEY = 'SGYvICm0gko3gKtoWN1tvPhf'
SECRET_KEY = 'FllhDBjTgItoOVfmGP9Ewb7bbvoGmNsT'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

class Ui_Form(object):
    def setupUi(self, Form):
        self.options = {}
        self.count=0
        self.index = 0
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(775, 547)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.checkBox.setObjectName("checkBox")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 451, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 50, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 80, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 80, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(480, 110, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(480, 310, 256, 192))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.open_file)
        # self.pushButton.clicked.connect(self.paintEvent)
        self.pushButton_2.clicked.connect(self.rec_cai)
        self.pushButton_3.clicked.connect(self.car_rec)
        self.pushButton_4.clicked.connect(self.logo_rec)
        self.pushButton_5.clicked.connect(self.animal_rec)
        self.pushButton_6.clicked.connect(self.plant)
        self.checkBox.stateChanged.connect(self.changebox)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像识别示例程序"))
        self.pushButton.setText(_translate("Form", "打开图像"))
        self.checkBox.setText(_translate("Form", "检测人脸"))
        self.pushButton_2.setText(_translate("Form", "菜品识别"))
        self.pushButton_3.setText(_translate("Form", "车型识别"))
        self.pushButton_4.setText(_translate("Form", "商标识别"))
        self.pushButton_5.setText(_translate("Form", "动物识别"))
        self.pushButton_6.setText(_translate("Form", "识别植物"))


    def open_file(self):
        self.graphicsView.update()
        QApplication.processEvents()
        file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片", r".\Demo\test")
        print(file_path)
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img=img
        self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)

        #打开图片文件
        with open(file_path, 'rb') as f:
            image = f.read()
            self.textBrowser.clear()


        # print((self.graphicsView.width(),self.graphicsView.height()))
        # img=cv.imread(file_path)
        # x=img.shape[0]
        # y=img.shape[1]
        # print(x,y)
        # scale_x=self.graphicsView.width()/x
        # scale_y=self.graphicsView.height()/y

        self.image = image


        options={}
        options['baike_num']=5
        baike_info=client.advancedGeneral(self.image, options)['result'][0]  # 通用物体识别
        print(baike_info)

        if not baike_info['baike_info']:
            baike_info=baike_info['keyword']
        else:
            baike_info=baike_info['baike_info']['description']

        self.textBrowser_2.clear()
        self.textBrowser_2.append(baike_info)

        coordinate = client.objectDetect(self.image, self.options)['result']  # 主体检测
        print(coordinate)

        if self.count == 1:
            self.demo.close()
            self.count -= 1
        self.demo = Drawing(self.graphicsView, coordinate)
        self.count += 1
        self.demo.show()


    def rec_cai(self):  # 调用百度API
        self.textBrowser.clear()
        result = client.dishDetect(self.image)['result']  # 调用API
        display = ''
        for r in result:
            print("----r-----", r)
            display += '菜品名称：' + r['name'] + '\n'
            display += '卡路里：' + r['calorie'] + '\n'
            display += '置信度：' + r['probability'] + '\n'
            display += '\n'
        self.textBrowser.append(display)


    def car_rec(self):
        self.textBrowser.clear()
        result = client.carDetect(self.image)['result']
        print(result)
        display = ''
        for r in result:
            print("----r-----",r)
            display += '车型：' + r['name'] + '\n'
            display += '年份：' + r['year'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def logo_rec(self):
        self.textBrowser.clear()
        result = client.logoSearch(self.image)['result']
        print(result)
        display = ''
        for r in result:
            display += '商标：' + r['name'] + '\n'
            display += '置信度：' + str(r['probability']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def animal_rec(self):
        self.textBrowser.clear()
        result = client.animalDetect(self.image)['result']
        display = ''
        for r in result:
            display += '动物：' + r['name'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def plant(self):
        self.textBrowser.clear()
        result = client.plantDetect(self.image)['result']
        display = ''
        for r in result:
            display += '动物：' + r['name'] + '\n'
            display += '置信度：' + str(r['score']) + '\n'
            display += '\n'
        self.textBrowser.append(display)

    def changebox(self):
        if self.index == 0:
            self.options['with_face'] = 0
            self.index += 1
        else:
            self.options['with_face'] = 1
            self.index -= 1
        self.open_file()
    # def paintEvent(self,event):
    #     painter = QPainter()
    #     painter.setPen(QColor(166, 66, 250))
    #     painter.begin(self.Form)
    #     self.drawRect(event,painter) # 绘制函数
    #     painter.end()
    #
    # def drawRect(self,event,qp): #设置画笔的颜色
    #     qp.setPen(QColor(168,34,3)) #设置字体
    #     qp.setFont(QFont('SimSun',20)) #绘制文字
    #     qp.drawRect(22,4,958,663)


class Drawing(QLabel):

    def __init__(self, parent, coordinate):  # parent定义的是在哪个父级控件上绘制矩形
        super(Drawing, self).__init__(parent)  # 尚未搞清
        self.left, self.top, self.width, self.height = coordinate['left'], coordinate['top'], coordinate['width'],coordinate['height']
        # self.width=self.width*scale_x
        # self.height =self.height*scale_y
        self.resize(1000, 1000)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)  # 自定义绘制方法
        self.draw(event, painter)
        painter.end()

    def draw(self, event, qp):  # 设置画笔的颜色
        qp.setPen(QColor(168, 34, 3))  # 设置字体
        qp.setFont(QFont('SimSun', 20))  # 绘制文字
        qp.drawRect(self.left, self.top, self.width, self.height)

        # self.left, self.top, self.width, self.height


if __name__ == "__main__":
    # Files = os.listdir(r'C:\Users\Tao xia\Desktop\Demo\test')
    # os.chdir(r'C:\Users\Tao xia\Desktop\Demo\test')
    # for file in Files:
    #     img = cv.imread(file)
    #     img2 = cv.resize(img, (451, 471))
    #     cv.imwrite(file, img2)
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
