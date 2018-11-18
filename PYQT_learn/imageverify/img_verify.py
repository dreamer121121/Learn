# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'img_verify.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
# import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aip import AipImageCensor

""" 你的 APPID AK SK """

APP_ID = '14851187'
API_KEY = 'ldjCzEfKHuB9sBVMAMAO733I'
SECRET_KEY = 'Ebf0B4UGnbT2TDADeuDhLQOHQyiqGT2A'
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)



class Ui_Form(object):
    def setupUi(self, Form):

        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(784, 397)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 50, 401, 331))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 15, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 20, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 20, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(425, 50, 341, 331))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.load_img)
        self.pushButton_2.clicked.connect(self.imageCensorComb)
        # self.pushButton_3.clicked.connect(Form.face_verify)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "载入图像"))
        self.label.setText(_translate("Form", "图像审核结果："))
        self.pushButton_2.setText(_translate("Form", "组合图像审核"))
        self.pushButton_3.setText(_translate("Form", "用户头像审核"))

    def load_img(self):
        file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片", r"C:\Users\jack xia\Desktop\Demo\test")
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img = img
        self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)
        with open(file_path, 'rb') as f:
            image = f.read()
        self.img = image
        self.userCensordefined()  # 调用用户自定义审核接口

    def userCensordefined(self):
        self.textBrowser.clear()
        result = client.imageCensorUserDefined(self.img)
        # 解析返回结果
        print(result)
        display = ''
        display += result['conclusion'] + '\n'
        display += '-' * 20+'\n'
        for content in result['data']:
            display += content['msg'] + '\n'
            if 'stars' in content:
                for public in content['stars']:
                    display += public['name'] + ' ' + '\n'
            if 'words' in content:
                display += content['words']
            display += '\n'
        # 展示
        self.textBrowser.append(display)



    def imageCensorComb(self):
        self.textBrowser.clear()
        options = ['ocr']
        result = client.imageCensorComb(self.img, options)
        print(result)
        # display = '文字识别结果：'+'\n'
        # ocr=result['ocr']




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
