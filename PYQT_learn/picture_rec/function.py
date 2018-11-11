
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from aip import AipImageClassify

APP_ID = '14757979'
API_KEY = 'SGYvICm0gko3gKtoWN1tvPhf'
SECRET_KEY = 'FllhDBjTgItoOVfmGP9Ewb7bbvoGmNsT'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def open_file(self):
    file_path, _ = QFileDialog.getOpenFileName(self.widget, "选择图片", r"C:\Users\jack xia\Desktop\Demo\测试图像")
    img = QImage()
    img.load(file_path)  # 载入图片
    self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
    self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
    self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
    self.graphicsView.setScene(self.graphicsView.scene)


    def rec_cai(self):  # 调用百度API
        with open(self.file_path, 'rb') as f:
            image = f.read()
        result = client.dishDetect(image)['result']  # 调用API
        display = ''
        for r in result:
            display += '菜品名称：' + r['name'] + '\n'
            display += '卡路里：' + r['calorie'] + '\n'
            display += '置信度：' + r['probability'] + '\n'
            display += '\n'
        self.textBrowser.append(display)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())