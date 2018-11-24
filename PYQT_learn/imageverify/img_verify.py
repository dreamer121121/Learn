# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'img_verify.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
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
        self.pushButton_3.clicked.connect(self.faceAudit)
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

    def userCensordefined(self):  # 用户自定义图像审核
        self.textBrowser.clear()
        result = client.imageCensorUserDefined(self.img)
        # 解析返回结果
        display = ''
        if result['conclusion'] == '合规':
            display += result['conclusion'] + '\n'
        else:
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
        options = ['ocr', 'webimage', 'politician', 'antiporn', 'terror', 'disgust', 'watermark', 'public']
        result = client.imageCensorComb(self.img, options)['result']
        print(result)
        display = ''

        # OCR识别
        display = '文字识别结果：' + '\n'
        display += '\n'
        print(display)
        # 色情识别
        display += '色情识别结果：' + '\n'
        content = result['antiporn']

        if content['result'][2]['probability'] > 0.999:
            content['result'][2]['probability'] = 1
        if content['result'][2]['probability'] < 0.001:
            content['result'][2]['probability'] = 0.00

        display += content['conclusion']+','+'置信度：'+str(content['result'][2]['probability'])[0:3]+'\n'
        display += '\n'
        print(display)
        #暴恐识别
        display += '暴恐识别结果:'+'\n'
        i = 0
        max = 0
        max_score = 0
        length = len(result['terror']['result_fine'])
        for i in range(length):
            if result['terror']['result_fine'][i]['score'] > max_score:
                max_score = result['terror']['result_fine'][i]['score']
                max = i

        choice = result['terror']['result_fine'][max]
        display += choice['name']+', '+'置信度：'+str(choice['score'])[0:3]+'\n'
        display += '\n'
        print(display)
        #政治敏感人物
        display += '政治敏感人物识别结果：'+'\n'
        if not result['politician']['result']:
            display += '\n'
        else:
            content = result['politician']['result'][0]['stars'][0]
            display += content['name']+' 置信度：'+str(content['probability'])[0:3]+'\n'
            display += '\n'
        print(display)
        #广告检测结果
        display += '广告检测结果：'+'\n'
        if not result['watermark']['result']:
            display += ''+'\n'
        else:
            content = result['watermark']['result'][0]
            display += content['type']+'， 置信度：'+str(content['probability'])+'\n'
            display += '\n'
        print(display)
        #恶心图像识别
        display += '恶心图像识别结果：' + '\n'
        if result['disgust']['result'] < 0.001:
            result['disgust']['result'] = 0.00
        display += '恶心程度:'+str(result['disgust']['result'])+'\n'
        display += '\n'
        print(display)
        #图像质量检测结果
        display += '图像质量检测结果:'+'\n'
        display += '\n'
        print(display)
        self.textBrowser.append(display)

    def faceAudit(self):
        self.textBrowser.clear()
        result = client.faceAudit(self.img)['result'][0]
        print(result)
        display=''
        if result['res_code'] == 1:
           display += '识别结果1：不通过'+'\n'
           display += '图片中不包含人脸'+'\n'
        else:
            display += '识别结果0：通过'+'\n'
        display += '\n'
        print(display)

        # 人脸检测结果
        display += '人脸检测结果：' + '\n'
        content = result['data']['face']['result']
        if not content:
            display += '\n'
        else:
            display += '年龄估算：' + str(content[0]['age'])
            if content[0]['gender'] == 'male':
                content[0]['gender'] = '男'
            else:
                content[0]['gender'] = '女'
            display += '性别：' + content[0]['gender']+'\n'
            display += '\n'

        #文字识别结果
        display += '文字识别结果：'+'\n'
        content = result['data']['ocr']['words_result']
        if content == []:
            display += '\n'
        for each in content:
            display += each['words']+'\n'

        #色情识别结果

        display += '色情识别结果：' + '\n'
        content = result['data']['antiporn']
        if content['result'][2]['probability'] > 0.999:
            content['result'][2]['probability'] = 1
        if content['result'][2]['probability'] < 0.001:
            content['result'][2]['probability'] = 0.00

        display += content['conclusion'] + ',' + '置信度：' + str(content['result'][2]['probability'])[0:3] + '\n'
        display += '\n'
        print(display)

        # 暴恐识别
        display += '暴恐识别结果:' + '\n'
        i = 0
        max = 0
        max_score = 0
        content=result['data']['terror']['result_fine']
        length = len(content)
        print(length)
        for i in range(length):
            if content[i]['score'] > max_score:
                max_score = content[i]['score']
                max = i

        choice = content[max]
        display += choice['name'] + ', ' + '置信度：' + str(choice['score'])[0:3] + '\n'
        display += '\n'
        print(display)

        #公众人物识别结果
        display += '公众人物识别结果：'+'\n'
        content = result['data']['public']['result']
        if not content:
            display += '\n'
        else:
            display += content[0]['stars'][0]['name']+' ,置信度：'
            display += str(content[0]['stars'][0]['probability'])[0:3]+'\n'
        self.textBrowser.append(display)













if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
