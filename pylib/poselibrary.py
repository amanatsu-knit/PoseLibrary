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
from functools import partial
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
        # self.libraryDirectory = os.path.abspath(os.path.join(self.currentDirectory, '..', 'PoseData'))
        self.tempDirectory = os.path.abspath(os.getenv('TEMP'))
        self.snapshotPath = '%s/MyPose_Snapshot.png' % self.tempDirectory
        self.folderIcon = QtGui.QImage(':/folder-closed.png')
        self.createFolderIcon = QtGui.QImage(':/folder-new.png')
        self.expandIcon = QtGui.QImage(':/expandContainer.png')
        self.collapseIcon = QtGui.QImage(':/collapseContainer.png')
        self.snapshotIcon = QtGui.QImage(':/snapshot.svg')
        self.renameIcon = QtGui.QImage(':/pencilCursor.png')
        self.removeIcon = QtGui.QImage(':/deleteActive.png')
        self.controlDataList = {}
        self.currentMode = 'export'
        self.currentPoseData = ''

        """Call functions"""
        self.uiConfigure()
        self.iconConfigure()
        self.loadFolderStructure(self.libraryDirectory)

    def uiConfigure(self):
        self.setWindowTitle('Pose Library v0.1')
        self.splitter.setSizes([200, 500, 200])
        self.resize(985, 620)

        """Folder menu"""
        self.folderMenu = QtWidgets.QMenu(self)
        self.folderMenu.addAction(self.action_createFolder)
        self.folderMenu.addSeparator()
        self.folderMenu.addAction(self.action_expand)
        self.folderMenu.addAction(self.action_collapse)
        self.folderMenu.addSeparator()
        self.folderMenu.addAction(self.action_rename)
        self.folderMenu.addAction(self.action_remove)

        self.action_createFolder.triggered.connect(self.createFolder)
        self.action_expand.triggered.connect(self.expandFolder)
        self.action_collapse.triggered.connect(self.collapseFolder)
        self.action_rename.triggered.connect(self.renameFolder)
        self.action_remove.triggered.connect(self.removeFolder)

        """Custom context Menu"""
        self.treeWidget_folderList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_folderList.customContextMenuRequested.connect(self.onFolderContextMenu)

        """Snapshot of current pose"""
        self.button_snapShot.clicked.connect(self.takeSnapshot)

        """Save the current pose"""
        self.button_save.clicked.connect(self.savePose)

        """Load Pose to UI"""
        self.treeWidget_folderList.itemClicked.connect(self.loadCurrentFolder)

        """Pose blending"""
        self.button_blendValue.clicked.connect(self.sliderReset)
        self.slider_poseBlend.valueChanged.connect(self.poseSlider)

        """Rename Pose"""
        self.lineEdit_poseLabel.returnPressed.connect(self.renamePose)

        self.switchToExportImport('export')

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
        self.treeWidget_folderList.clear()
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

    """Rename Selected folder"""

    def renameFolder(self):
        selectedItems = self.treeWidget_folderList.selectedItems()
        if selectedItems:
            newName, ok = QtWidgets.QInputDialog.getText(self, 'Folder Name', 'Enter the new name :',
                                                         QtWidgets.QLineEdit.Normal)
            if ok:
                currentFolderPath = str(selectedItems[-1].toolTip(0))
                selectedItems[-1].setText = (0, newName)
                newFolderPath = '%s/%s' % (os.path.dirname(currentFolderPath), str(newName))
                replay = 0
                try:
                    os.chmod(currentFolderPath, 0777)
                    os.rename(currentFolderPath, newFolderPath)
                    replay = 1
                except Exception, result:
                    replay = 0
                    print result
                if replay == 1:
                    selectedItems[-1].setText = (0, newName)
                    selectedItems[-1].setToolTip = (0, newFolderPath)
                # self.loadFolderStructure(self.libraryDirectory)

        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No folder selected\nPlease select the folder',
                                          QtWidgets.QMessageBox.Ok)
            print 'Warning', 'No folder selected\t- Please select the folder'

    """Remove Selected folder"""

    def removeFolder(self):
        selectedItems = self.treeWidget_folderList.selectedItems()
        if selectedItems:
            replay = QtWidgets.QMessageBox.question(self, 'Question', 'Are you sure, you want to remove folder',
                                                    QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if replay == QtWidgets.QMessageBox.Yes:
                for eachItems in selectedItems:
                    folderPath = str(eachItems.ToolTip(0))
                    try:
                        os.chmod(folderPath, 0777)
                        shutil.rmtree(folderPath)
                        print 'Removed\t', folderPath
                    except Exception, result:
                        print result
                self.loadFolderStructure(self.libraryDirectory)
            else:
                QtWidgets.QMessageBox.warning(self, 'Warning', 'No folder selected\nPlease select the folder',
                                              QtWidgets.QMessageBox.Ok)
                print 'Warning', 'No folder selected\t- Please select the folder'

    """Collect all dependent child from parent QTreeWidget Item"""

    def collectChildItems(self, parent):
        for index in range(parent.childCount()):
            currentChild = parent.child(index)
            self.dependentList.append(currentChild)
            self.collectChildItems(currentChild)

    """Take Snapshot of current pose"""

    def takeSnapshot(self):
        if self.currentMode == 'export':
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
            mc.playblast(st=currentFrame, et=currentFrame, fmt='image', cc=True, v=False, orn=False, fp=True,
                         p=100, c='png', quality=100, wh=[512, 512], cf=self.snapshotPath)

            self.loadImageToButton(self.button_snapShot, self.snapshotPath, [150, 150])

    """Load Image to button"""

    def loadImageToButton(self, button, path, size):
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
                    # self.lineEdit_poseLabel.clear()
                    # elf.loadImageToButton(self.button_snapShot, currentPosePath, [150, 150])
                    self.loadCurrentFolder()
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

        """Add Child items with selected QTree Item"""
        self.dependentList = []

        for eachItems in currentItems:
            self.dependentList.append(eachItems)
            self.collectChildItems(eachItems)
        self.removeExistWidget(self.gridLayout_poseList)
        self.loadPoseToLayout(self.dependentList)
        self.switchToExportImport('export')

    """Remove exists widget from Layout"""

    def removeExistWidget(self, layout):
        for index in range(layout.count()):
            if layout.itemAt(index).widget():
                layout.itemAt(index).widget().deleteLater()

    """Load pose to layout"""

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
        for index in range(len(poseList)):
            if index % 3:
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
            toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            toolButton.setMinimumSize(QtCore.QSize(170, 170))
            toolButton.setMaximumSize(QtCore.QSize(170, 170))
            poseIconPath = poseList[index].replace('.pose', '.png')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(poseIconPath), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            toolButton.setIcon(icon),
            toolButton.setIconSize(QtCore.QSize(140, 140))
            self.gridLayout_poseList.addWidget(toolButton, coordinateList[index][0], coordinateList[index][1], 1, 1)

            toolButton.clicked.connect(partial(self.setCurrentPose, poseList[index]))

    """Set the Pose to character"""

    def setCurrentPose(self, posePath):
        readData = open(posePath, 'r')
        dataList = json.load(readData)

        selectionList = mc.ls(sl=True)

        self.controlDataList = {}

        for eachSelection in selectionList:

            currentControl = eachSelection
            if mc.referenceQuery(eachSelection, inr=1):
                referencePath = mc.referenceQuery(eachSelection, f=True)
                nameSpace = mc.file(referencePath, q=True, ns=True)
                currentControl = eachSelection.replace('%s:' % nameSpace, '')

            if currentControl in dataList['control']:
                attributeList = dataList['control'][currentControl]

                for eachAttribute in attributeList:
                    poseValue = attributeList[eachAttribute]
                    currentValue = mc.getAttr('%s.%s' % (eachSelection, eachAttribute))

                    self.controlDataList.setdefault('%s.%s' % (eachSelection, eachAttribute), [currentValue, poseValue])
        currentIconPath = posePath.replace('.pose', '.png')
        self.loadImageToButton(self.button_snapShot, currentIconPath, [150, 150])
        currentPoseLabel = os.path.splitext(os.path.basename(posePath))[0]
        self.lineEdit_poseLabel.setText(currentPoseLabel)

        """Load history"""
        historyData = dataList['history']
        historyList = ['Owner%s: %s' % ('\t'.rjust(5), historyData[0]),
                       'Created%s: %s' % ('\t'.rjust(5), historyData[1]),
                       'Maya version%s: %s' % ('\t'.rjust(5), historyData[2]),
                       'Module Versions%s: %s' % ('\t'.rjust(5), historyData[3])
                       ]
        self.textEdit_history.setText('\n'.join(historyList))
        # self.slider_poseBlend.setValue(100)
        self.poseSlider()
        self.switchToExportImport('import')
        self.currentPoseData = posePath
        print '#Successfully import My Pose'

    def sliderReset(self):
        self.slider_poseBlend.setValue(100)

    def poseSlider(self):
        sliderValue = self.slider_poseBlend.value()
        self.button_blendValue.setText(str(sliderValue))
        self.poseBlending()

    def poseBlending(self):
        if self.controlDataList:
            sliderValue = self.slider_poseBlend.value()

            for eachControl in self.controlDataList:
                currentValue = self.controlDataList[eachControl][0]
                poseValue = self.controlDataList[eachControl][1]

                length = poseValue - currentValue
                percentage = (length * sliderValue) / 100.00
                setValue = currentValue + percentage
                mc.setAttr(eachControl, setValue)

    """Pose Export and import Mode"""

    def switchToExportImport(self, mode):
        self.button_save.hide()
        self.groupBox_blend.hide()
        if mode == 'export':
            self.lineEdit_poseLabel.clear()
            self.textEdit_history.clear()
            self.button_save.show()
            self.loadImageToButton(self.button_snapShot, self.snapshotIcon, [150, 150])
            self.currentMode = 'export'
        if mode == 'import':
            self.groupBox_blend.show()
            self.currentMode = 'import'

    """Rename Pose"""

    def renamePose(self):
        if self.currentMode == 'import':
            if self.currentPoseData:
                newPoseLabel = str(self.lineEdit_poseLabel.text())
                if newPoseLabel:
                    newPosePath = '%s/%s.pose' % (os.path.dirname(self.currentPoseData), newPoseLabel)
                    existsIconPath = self.crrentPoseData.replace('.pose', '.png')
                    newIconPath = newPosePath.replace('.pose', '.png')

                    if os.path.isfile(self.currentPoseData):
                        try:
                            os.chmod(self.currentPoseData, 0777)
                            os.rename(self.currentPoseData, newPosePath)
                        except Exception, result:
                            print result
                        if os.path.isfile(existsIconPath):
                            try:
                                os.chmod(existsIconPath, 0777)
                                os.rename(existsIconPath, newIconPath)
                            except Exception, result:
                                print result
                        self.loadCurrentFolder()


def mayaMainWindow():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()

    return wrapInstance(long(mayaMainWindowPtr), QtWidgets.QMainWindow)


def main(*args):
    dialog = ASPoseLibrary(mayaMainWindow())
    dialog.show()


main()
