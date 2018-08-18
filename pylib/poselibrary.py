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
        self.currentDirectory = os.path.abspath(os.path.dirname(__file__))
        self.folderIconPath = QtGui.QImage(':/folder-open.png')
        self.createFolderIconPath = QtGui.QImage(':/folder-new.png')
        self.expandIconPath = QtGui.QImage(':/expandContainer.png')
        self.collapseIconPath = QtGui.QImage(':/collapseContainer.png')

        """Call functions"""
        self.uiConfigure()
        self.iconConfigure()
        self.loadFolderStructure(self.libraryDirectory)

    def uiConfigure(self):
        # self.setWindowTitle('Pose Library v0.1')

        """Folder menu"""
        self.folderMenu = QtWidgets.QMenu(self)
        self.folderMenu.addAction(self.action_createFolder)
        self.folderMenu.addSeparator()
        self.folderMenu.addAction(self.action_expand)
        self.folderMenu.addAction(self.action_collapse)

        self.action_createFolder.triggered.connect(self.createFolder)
        self.action_expand.triggered.connect(self.expandFolder)
        self.action_collapse.triggered.connect(self.collapseFolder)

        """Custom context Menu"""
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.onFolderContextMenu)

    """Connect Icon to Widgets"""
    def iconConfigure(self):
        menuList = self.findChildren(QtWidgets.QAction)
        for index in range(len(menuList)):
            objectName = menuList[index].objectName()
            if objectName:
                currentIcon = objectName.split('_')[1]
                self.iconPath = None
                if currentIcon == 'createFolder':
                    self.iconPath = self.createFolderIconPath
                elif currentIcon == 'expand':
                    self.iconPath = self.expandIconPath
                elif currentIcon == 'collapse':
                    self.iconPath = self.collapseIconPath
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.iconPath), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                menuList[index].setIcon(icon)


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
                icon.addPixmap(QtGui.QPixmap(self.folderIconPath), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                # print self.folderPath
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
            parent = self.treeWidget_folderList
            currentPath = self.libraryDirectory
            if self.treeWidget_folderList.selectedItems():
                parent = self.treeWidget_folderList.selectedItems()[-1]
                currentPath = str(parent.toolTip(0))
            if not os.path.isdir('%s/%s' % (currentPath, str(folderName))):
                item = QtWidgets.QTreeWidgetItem(parent)
                item.setText(0, str(folderName))
                item.setToolTip(0, '%s/%s' % (currentPath, str(folderName)))

                """Connect Icon"""
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.folderIconPath), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                if parent != self.treeWidget_folderList:
                    self.treeWidget_folderList.setItemExpanded(parent, 1)
                    self.treeWidget_folderList.setItemSelected(parent, 0)

                self.treeWidget_folderList.setItemSelected(item, 1)

                os.makedirs('%s/%s' % (currentPath, str(folderName)))

    def expandFolder(self):
        if self.treeWidget_folderList.selectedItems():
            currentItem = self.treeWidget_folderList.selectedItems()[-1]
            self.dependentList = [currentItem]
            self.collectChildItems(currentItem)
            for eachDependent in self.dependentList:
                self.treeWidget_folderList.setItemExpanded(eachDependent, 1)
        else:
            self.treeWidget_folderList.expandAll()

    def collapseFolder(self):
        currentItem = self.treeWidget_folderList.invisibleRootItem()

        if self.treeWidget_folderList.selectedItems():
            currentItem = self.treeWidget_folderList.selectedItems()[-1]

        self.dependentList = [currentItem]
        self.collectChildItems(currentItem)
        for eachDependent in self.dependentList:
            self.treeWidget_folderList.collapseItem(eachDependent)

    def collectChildItems(self, parent):
        for index in range(parent.childCount()):
            currentChild = parent.child(index)
            self.dependentList.append(currentChild)
            self.collectChildItems(currentChild)

def mayaMainWindow():
    mayaMainwindowPtr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(mayaMainwindowPtr), QtWidgets.QMainWindow)

def main(*args):
    dialog = ASPoseLibrary(mayaMainWindow())
    dialog.show()


main()
