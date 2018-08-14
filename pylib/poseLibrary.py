#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
My Pose Library v0.1
Data            : August 11, 2018
last modified   : August 11, 2018
Author          : shimono-a
"""

import sys
from maya import OpenMayaUI as omui

from Qt import QtCore, QtGui, QtWidgets

try:
    import shiboken2 as shiboken
except:
    import shiboken

try:
    from ui.PySide2 import poseLibrary_ui_pyside2 as poseLibrary_ui
except ImportError:
    from ui.PySide import poseLibrary_ui_pyside as poseLibrary_ui


class MainWindow(QtWidgets.QMainWindow, poseLibrary_ui.Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


def maya_main_window():
    maya_mainwindow_ptr = omui.MQtUtil.mainWindow()

    return shiboken.wrapInstance(long(maya_mainwindow_ptr), QtWidgets.QMainWindow)


def main(*args):
    dialog = MainWindow(maya_main_window())
    dialog.show()
