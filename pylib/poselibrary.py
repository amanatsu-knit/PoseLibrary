#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Pose Library v0.1
Data            : August 11, 2018
last modified   : August 11, 2018
Author          : shimono-a
"""
import os
import sys

from maya import OpenMayaUI as omui
from pylib.vendor.Qt import QtCore, QtGui, QtWidgets

try:
    from shiboken import wrapInstance
except ImportError:
    from shiboken2 import wrapInstance

try:
    from pylib.ui.pyside2 import poselibrary_window
except ImportError:
    from pylib.ui.pyside import poselibrary_window

sys.dont_write_bytecode = True


class ASPoseLibrary(QtWidgets.QMainWindow, QtWidgets.QListView, poselibrary_window.Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(ASPoseLibrary, self).__init__(parent)
        self.setupUi(self)

        """Global variables"""
        self.library_directory = 'D:/work/Maya/PoseLibrary'

        """Call functions"""
        self.ui_configure()

    def ui_configure(self):
        self.setWindowTitle('Pose Library v0.1')

        """Folder menu"""
        self.folderMenu = QtWidgets.QMenu(self)
        self.folderMenu.addAction('Create Folder')
        self.folderMenu.triggered.connect(self.create_folder)

        """Custom context Menu"""
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.on_folder_context_menu)

    def on_folder_context_menu(self, point):
        self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(point))

    def create_folder(self):
        folder_name, ok = QtWidgets.QInputDialog.getText(self, 'Folder Name', 'Enter the folder name :',
                                                         QtWidgets.QLineEdit.Normal)
        if ok:
            os.makedirs('%s/%s' % (self.library_directory, folder_name))


#
# class ListView(QtWidgets.QListView,poselibrary_window.Ui_MainWindow):
#     def __init__(self, *args, **kwargs):
#         super(ListView, self).__init__(*args, **kwargs)
#
#         self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
#         self.treeWidget_folderList.customContextMenuRequested.connect(self.on_folder_context_menu)
#
#     def contextMenu(self, point):
#         self.folderMenu = QtWidgets.QMenu(self)
#
#         for i in range(5):
#             action = QtGui.QAction('Menu%s' % i, self)
#             self.folderMenu.addAction(action)
#
#             self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(point))

def maya_main_window():
    maya_mainwindow_ptr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(maya_mainwindow_ptr), QtWidgets.QMainWindow)


def main(*args):
    dialog = ASPoseLibrary(maya_main_window())
    dialog.show()


main()
