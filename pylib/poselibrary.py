#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Pose Library v0.1
Data            : August 11, 2018
last modified   : August 11, 2018
Author          : shimono-a
"""
import sys

sys.dont_write_bytecode = True

from maya import OpenMayaUI as omui
from vendor.Qt import QtCore, QtGui, QtWidgets

try:
    import shiboken2 as shiboken
except:
    import shiboken

try:
    from pylib.ui.pyside2 import poselibrary_window
except ImportError:
    from pylib.ui.pyside import poselibrary_window


class PoseLibrary(QtWidgets.QMainWindow, poselibrary_window.Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(PoseLibrary, self).__init__(parent)
        self.setupUi(self)

        """Global variables"""
        self.libraryDirectiry = 'D:/work/Maya/PoseLibrary'

        """Call functions"""
        self.uiConfigure()

    def uiConfigure(self):
        self.setWindowTitle('Pose Library v0.1')

        """Folder menu"""
        self.folderMenu = QtGui.QMenu(self)
        self.folderMenu.addAction(self.action_createFolder)

        """Custom context Menu"""
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.onFolderContextMenu)

    def onFolderContexMenu(self, point):
        self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(point))


def maya_main_window():
    maya_mainwindow_ptr = omui.MQtUtil.mainWindow()

    return shiboken.wrapInstance(long(maya_mainwindow_ptr), QtWidgets.QMainWindow)


def main(*args):
    dialog = PoseLibrary(maya_main_window())
    dialog.show()


main()
