# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


# 定义动作函数
def open_file_directory():
    download_path = QtWidgets.QFileDialog.getExistingDirectory(directory=r"C:\Users\outao\Desktop\PYQT_learn")
    return download_path


