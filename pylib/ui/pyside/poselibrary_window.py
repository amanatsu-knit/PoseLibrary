# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Git\PoseLibrary\pylib\ui\poseLibrary_window.ui'
#
# Created: Thu Aug 16 10:46:25 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 14pt \"MS Sans Serif\";")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget_folderList = QtGui.QTreeWidget(self.splitter)
        self.treeWidget_folderList.setStyleSheet("")
        self.treeWidget_folderList.setAlternatingRowColors(True)
        self.treeWidget_folderList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget_folderList.setHeaderHidden(True)
        self.treeWidget_folderList.setObjectName("treeWidget_folderList")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_folderList)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_folderList)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.scrollArea_pose = QtGui.QScrollArea(self.splitter)
        self.scrollArea_pose.setWidgetResizable(True)
        self.scrollArea_pose.setObjectName("scrollArea_pose")
        self.scrollAreaWidget_pose = QtGui.QWidget()
        self.scrollAreaWidget_pose.setGeometry(QtCore.QRect(0, 0, 341, 580))
        self.scrollAreaWidget_pose.setObjectName("scrollAreaWidget_pose")
        self.gridLayout_poseList = QtGui.QGridLayout(self.scrollAreaWidget_pose)
        self.gridLayout_poseList.setObjectName("gridLayout_poseList")
        self.pushButton_11 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_poseList.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_poseList.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_poseList.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_poseList.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_poseList.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_poseList.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_poseList.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_poseList.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_poseList.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_poseList.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_poseList.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_poseList.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_poseList.addWidget(self.pushButton_13, 4, 0, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_poseList.addWidget(self.pushButton_14, 4, 1, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.scrollAreaWidget_pose)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_poseList.addWidget(self.pushButton_15, 4, 2, 1, 1)
        self.scrollArea_pose.setWidget(self.scrollAreaWidget_pose)
        self.groupBox_pose = QtGui.QGroupBox(self.splitter)
        self.groupBox_pose.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox_pose.setObjectName("groupBox_pose")
        self.verticalLayout_pose = QtGui.QVBoxLayout(self.groupBox_pose)
        self.verticalLayout_pose.setSpacing(10)
        self.verticalLayout_pose.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_pose.setObjectName("verticalLayout_pose")
        self.groupBox_snapShot = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_snapShot.setObjectName("groupBox_snapShot")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_snapShot)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_snapShot = QtGui.QPushButton(self.groupBox_snapShot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_snapShot.sizePolicy().hasHeightForWidth())
        self.button_snapShot.setSizePolicy(sizePolicy)
        self.button_snapShot.setMinimumSize(QtCore.QSize(150, 150))
        self.button_snapShot.setObjectName("button_snapShot")
        self.horizontalLayout.addWidget(self.button_snapShot)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_pose.addWidget(self.groupBox_snapShot)
        self.groupBox_poseLabel = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_poseLabel.setObjectName("groupBox_poseLabel")
        self.horizontalLayout_poseLabel = QtGui.QHBoxLayout(self.groupBox_poseLabel)
        self.horizontalLayout_poseLabel.setSpacing(5)
        self.horizontalLayout_poseLabel.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_poseLabel.setObjectName("horizontalLayout_poseLabel")
        self.label_poseLabel = QtGui.QLabel(self.groupBox_poseLabel)
        self.label_poseLabel.setObjectName("label_poseLabel")
        self.horizontalLayout_poseLabel.addWidget(self.label_poseLabel)
        self.lineEdit_poseLabel = QtGui.QLineEdit(self.groupBox_poseLabel)
        self.lineEdit_poseLabel.setObjectName("lineEdit_poseLabel")
        self.horizontalLayout_poseLabel.addWidget(self.lineEdit_poseLabel)
        self.verticalLayout_pose.addWidget(self.groupBox_poseLabel)
        self.textEdit_history = QtGui.QTextEdit(self.groupBox_pose)
        self.textEdit_history.setReadOnly(True)
        self.textEdit_history.setObjectName("textEdit_history")
        self.verticalLayout_pose.addWidget(self.textEdit_history)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_pose.addItem(spacerItem2)
        self.groupBox_blend = QtGui.QGroupBox(self.groupBox_pose)
        self.groupBox_blend.setObjectName("groupBox_blend")
        self.horizontalLayout_blend = QtGui.QHBoxLayout(self.groupBox_blend)
        self.horizontalLayout_blend.setSpacing(5)
        self.horizontalLayout_blend.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_blend.setObjectName("horizontalLayout_blend")
        self.slider_poseBlend = QtGui.QSlider(self.groupBox_blend)
        self.slider_poseBlend.setOrientation(QtCore.Qt.Horizontal)
        self.slider_poseBlend.setObjectName("slider_poseBlend")
        self.horizontalLayout_blend.addWidget(self.slider_poseBlend)
        self.button_blendValue = QtGui.QPushButton(self.groupBox_blend)
        self.button_blendValue.setMinimumSize(QtCore.QSize(50, 20))
        self.button_blendValue.setMaximumSize(QtCore.QSize(50, 20))
        self.button_blendValue.setStyleSheet("font: 12pt \"MS Sans Serif\";")
        self.button_blendValue.setObjectName("button_blendValue")
        self.horizontalLayout_blend.addWidget(self.button_blendValue)
        self.verticalLayout_pose.addWidget(self.groupBox_blend)
        self.button_save = QtGui.QPushButton(self.groupBox_pose)
        self.button_save.setObjectName("button_save")
        self.verticalLayout_pose.addWidget(self.button_save)
        self.horizontalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_create_folder = QtGui.QAction(MainWindow)
        self.action_create_folder.setObjectName("action_create_folder")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget_folderList.isSortingEnabled()
        self.treeWidget_folderList.setSortingEnabled(False)
        self.treeWidget_folderList.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "02", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_folderList.setSortingEnabled(__sortingEnabled)
        self.groupBox_pose.setTitle(QtGui.QApplication.translate("MainWindow", "Pose", None, QtGui.QApplication.UnicodeUTF8))
        self.button_snapShot.setText(QtGui.QApplication.translate("MainWindow", "Icon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_poseLabel.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.button_blendValue.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_create_folder.setText(QtGui.QApplication.translate("MainWindow", "Create Folder", None, QtGui.QApplication.UnicodeUTF8))

