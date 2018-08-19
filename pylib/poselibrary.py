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
import datetime
import json
import shutil
import maya.cmds as mc
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
        self.tempDirectory = os.path.abspath(os.getenv('TEMP'))
        self.snapshotPath = '%s/MyPose_Snapshot.png' % self.tempDirectory
        self.folderIcon = QtGui.QImage(':/folder-closed.png')
        self.createFolderIcon = QtGui.QImage(':/folder-new.png')
        self.expandIcon = QtGui.QImage(':/expandContainer.png')
        self.collapseIcon = QtGui.QImage(':/collapseContainer.png')
        self.snapshotIcon = QtGui.QImage(':/snapshot.svg')

        """Call functions"""
        self.uiConfigure()
        self.iconConfigure()
        self.loadFolderStructure(self.libraryDirectory)

    def uiConfigure(self):
        self.setWindowTitle('Pose Library v0.1')
        self.splitter.setSizes([200, 500, 200])

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

        """Snapshot of current pose"""
        self.button_snapShot.clicked.connect(self.takeSnapshot)
        self.loadImagetToButton(self.button_snapShot, self.snapshotIcon, [150, 150])

        """Save the current pose"""
        self.button_save.clicked.connect(self.savePose)

        """Load Pose to UI"""
        self.treeWidget_folderList.itemClicked.connect(self.loadCurrentFolder)

    """Connect Icon to Widgets"""

    def iconConfigure(self):
        menuList = self.findChildren(QtWidgets.QAction)
        for index in range(len(menuList)):
            objectName = menuList[index].objectName()
            if objectName:
                currentIcon = objectName.split('_')[1]
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(eval('self.%sIcon' % currentIcon)), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                menuList[index].setIcon(icon)

    """ContextMenu - treeWidget_folderList"""

    def onFolderContextMenu(self, point):
        self.folderMenu.exec_(self.treeWidget_folderList.mapToGlobal(point))

    """Load Exists Folder structure to QTreeWidget (treeWidget_folderList)"""

    def loadFolderStructure(self, path):
        directoryList = self.getFolderStructre(path)
        self.folderPath = path

        self.loadFolderToTreeWidget(directoryList[path], self.treeWidget_folderList, path)

    """Load folder structure to QTreeWidget"""

    def loadFolderToTreeWidget(self, directoryList, parent, path):
        for eachDirectory in directoryList:
            if eachDirectory:
                self.folderPath = '%s/%s' % (path, eachDirectory)

                item = QtWidgets.QTreeWidgetItem(parent)
                item.setText(0, eachDirectory)
                item.setToolTip(0, self.folderPath)

                """Connect Icon"""
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(self.folderIcon), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                # print self.folderPath
                self.loadFolderToTreeWidget(directoryList[eachDirectory], item, self.folderPath)
        self.folderPath = path

    """Collect Folder structure"""

    def getFolderStructre(self, path):
        directoryList = {}
        for root, dirs, files in os.walk(path):
            folder_list = root.split(os.sep)
            folders = directoryList
            for eachFolder in folder_list:
                folders = folders.setdefault(eachFolder, {})

        return directoryList

    """Create New Folder"""

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
                icon.addPixmap(QtGui.QPixmap(self.folderIcon), QtGui.QIcon.Normal,
                               QtGui.QIcon.Off)
                item.setIcon(0, icon)

                if parent is not self.treeWidget_folderList:
                    self.treeWidget_folderList.setItemExpanded(parent, 1)
                    self.treeWidget_folderList.setItemSelected(parent, 0)

                self.treeWidget_folderList.setItemSelected(item, 1)

                os.makedirs('%s/%s' % (currentPath, str(folderName)))

    """Expand the QTreeWidget"""

    def expandFolder(self):
        if self.treeWidget_folderList.selectedItems():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(self.folderIcon), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            currentItem = self.treeWidget_folderList.selectedItems()[-1]
            self.dependentList = [currentItem]
            self.collectChildItems(currentItem)
            for eachDependent in self.dependentList:
                self.treeWidget_folderList.setItemExpanded(eachDependent, 1)
                eachDependent.setIcon(0, icon)
        else:
            self.treeWidget_folderList.expandAll()

    """Collapse the QTreeWidget"""

    def collapseFolder(self):
        currentItem = self.treeWidget_folderList.invisibleRootItem()

        if self.treeWidget_folderList.selectedItems():
            currentItem = self.treeWidget_folderList.selectedItems()[-1]

        self.dependentList = [currentItem]
        self.collectChildItems(currentItem)
        for eachDependent in self.dependentList:
            self.treeWidget_folderList.collapseItem(eachDependent)

    """Collect all dependent child from parent QTreeWidget Item"""

    def collectChildItems(self, parent):
        for index in range(parent.childCount()):
            currentChild = parent.child(index)
            self.dependentList.append(currentChild)
            self.collectChildItems(currentChild)

    """Take Snapshot of current pose"""

    def takeSnapshot(self):
        print 'wip'

        if os.path.isfile(self.snapshotPath):
            try:
                os.chmod(self.snapshotPath, 0777)
                os.remove(self.snapshotPath)
            except Exception, result:
                print result

        modelPanelList = mc.getPanel(type='modelPanel')
        for eachModelPanel in modelPanelList:
            mc.modelEditor(eachModelPanel, e=1, alo=0)
            mc.modelEditor(eachModelPanel, e=1, pm=1)

        currentFrame = mc.currentTime(q=True)
        playBlast = mc.playblast(st=currentFrame, et=currentFrame, fmt='image', cc=True, v=False, orn=False, fp=True,
                                 p=100, c='png', quality=100, wh=[512, 512], cf=self.snapshotPath)

        self.loadImagetToButton(self.button_snapShot, self.snapshotPath, [150, 150])

    """Load Image to button"""

    def loadImagetToButton(self, button, path, size):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        button.setIcon(icon),
        button.setIconSize(QtCore.QSize(size[0], size[1]))

    """Save the current Pose"""

    def savePose(self):

        poseLabel = str(self.lineEdit_poseLabel.text())
        if poseLabel:
            currentItem = self.treeWidget_folderList.selectedItems()
            print currentItem
            if currentItem:
                """Collect Control attribute and attribute attribute values"""
                selectionList = mc.ls(sl=True)

                if selectionList:
                    controlInfoList = {}
                    for eachSelection in selectionList:
                        attributeList = mc.listAttr(eachSelection, k=True, u=True, sn=True)
                        attributeInfoList = {}
                        if attributeList:
                            for eachAttribute in attributeList:
                                attrValue = mc.getAttr('%s.%s' % (eachSelection, eachAttribute))
                                attributeInfoList.setdefault(eachAttribute, attrValue)

                            currentControl = eachSelection
                            """Check the Reference"""
                            if mc.referenceQuery(eachSelection, inr=True):
                                referencePath = mc.referenceQuery(eachSelection, f=True)
                                nameSpace = mc.file(referencePath, q=True, ns=True)
                                currentControl = eachSelection.replace('%s:' % nameSpace, '')

                            controlInfoList.setdefault(currentControl.encode(), attributeInfoList)

                    # print controlInfoList

                    """Data history"""
                    owner = os.getenv('USERNAME')
                    time = datetime.datetime.now().strftime("%A, %B %d, %Y %Y %H:%M %p")
                    mayaVersions = mc.about(q=True, v=True)
                    versions = '0.1'
                    dataList = {'control': controlInfoList, 'history': [owner, time, mayaVersions, versions]}

                    """Write Pose Data"""
                    # dataPath = '%s/%s.pose' % (self.libraryDirectory, poseLabel)
                    currentFolderPath = str(currentItem[-1].toolTip(0))
                    dataPath = '%s/%s.pose' % (currentFolderPath, poseLabel)

                    if os.path.isfile(dataPath):
                        try:
                            os.chmod(dataPath, 0777)
                            os.remove(dataPath)
                        except Exception, result:
                            print result

                    """Write Data"""
                    poseData = open(dataPath, 'w')
                    jsonData = json.dumps(dataList, indent=4)
                    poseData.write(jsonData)
                    poseData.close()

                    print 'Done\t', dataPath

                    """Pose Icon"""
                    currentPoseIcon = self.snapshotPath
                    if not os.path.isfile(currentPoseIcon):
                        currentPoseIcon = '%s/icons/poseTemplate.png' % self.currentDirectory
                    currentPosePath = dataPath.replace('.pose', '.png')
                    if currentPoseIcon == '%s/icons/poseTemplate.png' % self.currentDirectory:
                        try:
                            shutil.copy2(currentPoseIcon, currentPosePath)
                        except Exception, result:
                            print result
                    else:
                        try:
                            shutil.move(currentPoseIcon, currentPosePath)
                        except Exception, result:
                            print result
                    self.lineEdit_poseLabel.clear()
                    self.loadImagetToButton(self.button_snapShot, currentPosePath, [150, 150])
                    print 'Successfully export My Pose Data.'
                else:
                    QtWidgets.QMessageBox.warning(self, 'Warning',
                                                  'No controls selected\nPlease select at least one control',
                                                  QtWidgets.QMessageBox.Ok)
                    print 'No controls selected\t- Please select at least one control'
            else:
                QtWidgets.QMessageBox.warning(self, 'Warning', 'No folder selected\nPlease select the folder',
                                              QtWidgets.QMessageBox.Ok)
                print 'Warning', 'No folder selected\t- Please select the folder'
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No pose selected\nPlease set the name before saving',
                                          QtWidgets.QMessageBox.Ok)
            print 'No pose selected\t- Please set the name before saving'

    """Load Pose to UI"""

    def loadCurrentFolder(self):
        currentItems = self.treeWidget_folderList.selectedItems()
        itemList = []
        for eachItems in currentItems:
            itemList.append(eachItems)
        self.loadPoseToLayout(itemList)

    def loadPoseToLayout(self, itemList):
        poseList = []

        for eachItem in itemList:
            currentPath = str(eachItem.toolTip(0))
            if os.path.isdir(currentPath):
                directoryList = os.listdir(currentPath)
                for eachFile in directoryList:
                    if os.path.isfile('%s/%s' % (currentPath, eachFile)):
                        if eachFile.endswith('.pose'):
                            poseList.append('%s/%s' % (currentPath, eachFile))
        row = -1
        column = 0
        coordinateList = []
        for index in range(10):
            if index % 5:
                column += 1
                coordinateList.append([row, column])
            else:
                row += 1
                column = 0
                coordinateList.append([row, column])

        for index in range(len(poseList)):
            poseLabel = os.path.splitext(os.path.basename(poseList[index]))[0]
            toolButton = QtWidgets.QToolButton(self.scrollAreaWidget_pose)
            toolButton.setObjectName('toolButton_%s' % poseLabel)
            toolButton.setText(poseLabel)
            print  coordinateList[index][0], '\t', coordinateList[index][1]
            self.gridLayout_poseList.addWidget(toolButton, coordinateList[index][0], coordinateList[index][1], 1, 1)


def mayaMainWindow():
    mayaMainwindowPtr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(mayaMainwindowPtr), QtWidgets.QMainWindow)


def main(*args):
    dialog = ASPoseLibrary(mayaMainWindow())
    dialog.show()


main()
