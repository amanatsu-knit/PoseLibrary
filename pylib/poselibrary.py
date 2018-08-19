#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Pose Library v0.1
Data            : August 11, 2018
last modified   : August 11, 2018
Author          : shimono-a
"""
import sys

import os
from maya import OpenMayaUI as omui

from pylib.vendor.Qt import QtCore, QtWidgets

try:
    from shiboken import wrapInstance
except ImportError:
    from shiboken2 import wrapInstance

try:
    from pylib.ui.pyside2 import poselibrary_window

    reload(poselibrary_window)
except ImportError:
    from pylib.ui.pyside import poselibrary_window

    reload(poselibrary_window)

sys.dont_write_bytecode = True


class ASPoseLibrary(QtWidgets.QMainWindow, QtWidgets.QListView, poselibrary_window.Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super(ASPoseLibrary, self).__init__(parent)
        self.setupUi(self)

        """Global variables"""
        self.libraryDirectory = 'Users/ATSUSHI/works/06_git/PoseLibrary/Pose'
        self.folderMenu = QtWidgets.QMenu(self)

        """Call functions"""
        self.uiConfigure()
        self.loadFolderToTreeWidget()

    def uiConfigure(self):
        self.setWindowTitle('Pose Library v0.1')

        """Folder menu"""
        self.folderMenu.addAction('Create Folder')
        self.folderMenu.triggered.connect(self.createFolder)

        """Custom context Menu"""
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.onFolderContextMenu)

    def onFolderContextMenu(self, point):
        self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(point))

    """Load Exists Folder structure to QTreeWidget (treeWidget_folderList)"""

    def loadFolderToTreeWidget(self):
        directory_list = self.getFolderStructre(self.libraryDirectory)
        for each_directory in directory_list:
            print each_directory

    def getFolderStructre(self, path):
        directory_list = {}
        for root, dirs, files in os.walk(path):
            folder_list = root.split(os.sep)
            folders = directory_list
            for eachFolder in folder_list:
                folders = folders.setdefault(eachFolder, {})

        return directory_list

    def createFolder(self):
        folder_name, ok = QtWidgets.QInputDialog.getText(self, 'Folder Name', 'Enter the folder name :',
                                                         QtWidgets.QLineEdit.Normal)
        if ok:
            os.makedirs('%s/%s' % (self.libraryDirectory, folder_name))


def mayaMainWindow():
    maya_mainwindow_ptr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(maya_mainwindow_ptr), QtWidgets.QMainWindow)


def main(*args):
    dialog = ASPoseLibrary(mayaMainWindow())
    dialog.show()


main()
