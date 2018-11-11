# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_form(object):
    def setupUi(self, form):

        self.widget = widget
        form.setObjectName("form")
        form.resize(890, 558)
        self.graphicsView = QtWidgets.QGraphicsView(form)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 321, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(QtCore.QRect(350, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(form)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 350, 321, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 310, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(form)
        self.graphicsView_2.setGeometry(QtCore.QRect(490, 20, 321, 281))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_3 = QtWidgets.QPushButton(form)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(form)
        self.label_3.setGeometry(QtCore.QRect(500, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(form)
        self.textBrowser_2.setGeometry(QtCore.QRect(490, 350, 321, 191))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(form)
        self.textBrowser_3.setGeometry(QtCore.QRect(340, 100, 141, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(form)
        self.pushButton_2.clicked.connect(self.show_img(1))
        self.pushButton_3.clicked.connect(self.show_img(2))
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "人脸识别演示程序"))
        self.pushButton.setText(_translate("form", "人脸对比"))
        self.label.setText(_translate("form", "比对结果"))
        self.label_2.setText(_translate("form", "人脸检测结果"))
        self.pushButton_2.setText(_translate("form", "载入图像"))
        self.pushButton_3.setText(_translate("form", "载入图像"))
        self.label_3.setText(_translate("form", "人脸检测结果"))

    def show_img(self, i):
        file_path, _ = QFileDialog.getOpenFileName(self.widget, "选择图片", r"C:\Users\jack xia\Desktop\Demo\测试头像")
        img = QImage()
        img.load(file_path)  # 载入图片
        self.img=img.scaled(self.graphicsView.width(), self.graphicsView.height())
        if i == 1:
            self.LoadImage()
        else:
            self.LoadImage2()

    def LoadImage(self):
        self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img)) # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)

    def LoadImage2(self):
        self.graphicsView_2.scene = QGraphicsScene()  # 创建一个图片元素的对象
        self.graphicsView_2.scene.addPixmap(QPixmap().fromImage(self.img)) # 将加载后的图片传递给scene对象
        self.graphicsView_2.setScene(self.graphicsView_2.scene)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
