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

from pylib.vendor.Qt import QtCore, QtWidgets, QtGui

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
        self.libraryDirectory = 'D:/work/Maya/PoseLibrary/PoseData'
        self.currentDirectory = os.path.abspath(os.path.dirname('__file__'))
        print self.currentDirectory
        self.folderMenu = QtWidgets.QMenu(self)

        """Call functions"""
        self.uiConfigure()
        self.loadFolderStructure(self.libraryDirectory)

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

    def loadFolderStructure(self, path):
        directoryList = self.getFolderStructre(path)
        self.folderPath = path

        self.loadFolderToTreeWidget(directoryList[path], self.treeWidget_folderList, path)

    def loadFolderToTreeWidget(self, directoryList, parent, path):
        for eachDirectory in directoryList:
            if eachDirectory:
                self.folderPath = '%s/%s' % (path, eachDirectory)

                item = QtWidgets.QTreeWidgetItem(parent)
                item.setText(0, eachDirectory)
                item.setToolTip(0, self.folderPath)

                """Connect Icon"""
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('%s/icons/folder.png' % self.currentDirectory), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                #print self.folderPath
                self.loadFolderToTreeWidget(directoryList[eachDirectory], item, self.folderPath)
        self.folderPath = path

    def getFolderStructre(self, path):
        directoryList = {}
        for root, dirs, files in os.walk(path):
            folder_list = root.split(os.sep)
            folders = directoryList
            for eachFolder in folder_list:
                folders = folders.setdefault(eachFolder, {})

        return directoryList

    def createFolder(self):
        folderName, ok = QtWidgets.QInputDialog.getText(self, 'Folder Name', 'Enter the folder name :',
                                                        QtWidgets.QLineEdit.Normal)
        if ok:
            os.makedirs('%s/%s' % (self.libraryDirectory, folderName))


def mayaMainWindow():
    mayaMainwindowPtr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(mayaMainwindowPtr), QtWidgets.QMainWindow)


def main(*args):
    dialog = ASPoseLibrary(mayaMainWindow())
    dialog.show()


main()
