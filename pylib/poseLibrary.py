#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
My Pose Library v0.1
Data            : August 11, 2018
last modified   : August 11, 2018
Author          : shimono-a
"""
import sys
sys.dont_write_bytecode = True

from maya import OpenMayaUI as omui
from vendors.Qt import QtCore, QtGui, QtWidgets

try:
    import shiboken2 as shiboken
except:
    import shiboken

try:
    from poselibrary_ui.pyside2 import poselibrary_window
except ImportError:
    from poselibrary_ui.pyside import poselibrary_window

class MainWindow(QtWidgets.QMainWindow, poselibrary_window.Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

def maya_main_window():
    maya_mainwindow_ptr = omui.MQtUtil.mainWindow()

    return shiboken.wrapInstance(long(maya_mainwindow_ptr), QtWidgets.QMainWindow)

def main(*args):
    dialog = MainWindow(maya_main_window())
    dialog.show()

main()
