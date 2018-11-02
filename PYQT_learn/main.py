# -*- coding:utf-8 -*-
import sys
from first_gui import Ui_widget
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # 窗口初始化
    ui = Ui_widget()  # 类的实例化
    ui.setupUi(MainWindow)  # 调用first_gui的方法
    MainWindow.show()  # 展示窗口
    sys.exit(app.exec_())
