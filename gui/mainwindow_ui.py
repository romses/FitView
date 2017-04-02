# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setMidLineWidth(5)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setOpaqueResize(False)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.metadataFrame = QtWidgets.QWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metadataFrame.sizePolicy().hasHeightForWidth())
        self.metadataFrame.setSizePolicy(sizePolicy)
        self.metadataFrame.setMinimumSize(QtCore.QSize(250, 250))
        self.metadataFrame.setObjectName("metadataFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.metadataFrame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.metadataStackedWidget = QtWidgets.QStackedWidget(self.metadataFrame)
        self.metadataStackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.metadataStackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.metadataStackedWidget.setObjectName("metadataStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.metadataStackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.metadataStackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.metadataStackedWidget)
        self.graph = QtWidgets.QFrame(self.splitter_2)
        self.graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph.setObjectName("graph")
        self.horizontalLayout.addWidget(self.splitter_2)
        self.all_events_table = QtWidgets.QTableWidget(self.splitter)
        self.all_events_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.all_events_table.setAlternatingRowColors(True)
        self.all_events_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.all_events_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.all_events_table.setObjectName("all_events_table")
        self.all_events_table.setColumnCount(5)
        self.all_events_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.all_events_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_events_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_events_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_events_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.all_events_table.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTest = QtWidgets.QMenu(self.menuBar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/img/No.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Logbook = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/img/folder_file_open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Logbook.setIcon(icon1)
        self.actionOpen_Logbook.setObjectName("actionOpen_Logbook")
        self.actionNew_Logbook = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/img/file_blanc_star.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Logbook.setIcon(icon2)
        self.actionNew_Logbook.setObjectName("actionNew_Logbook")
        self.actionImport_File = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/img/database_import.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_File.setIcon(icon3)
        self.actionImport_File.setObjectName("actionImport_File")
        self.actionSync_with_Garmin = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/menu/img/import-export.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSync_with_Garmin.setIcon(icon4)
        self.actionSync_with_Garmin.setObjectName("actionSync_with_Garmin")
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew_Logbook)
        self.toolBar.addAction(self.actionOpen_Logbook)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport_File)
        self.toolBar.addAction(self.actionSync_with_Garmin)
        self.toolBar.addSeparator()
        self.menuTest.addAction(self.actionNew_Logbook)
        self.menuTest.addAction(self.actionOpen_Logbook)
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.actionExit)
        self.menuBar.addAction(self.menuTest.menuAction())

        self.retranslateUi(MainWindow)
        self.metadataStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FitView"))
        item = self.all_events_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event Date"))
        item = self.all_events_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Event Name"))
        item = self.all_events_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Event Type"))
        item = self.all_events_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Event Subtype"))
        item = self.all_events_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "RowID"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuTest.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionOpen_Logbook.setText(_translate("MainWindow", "Open Logbook"))
        self.actionOpen_Logbook.setToolTip(_translate("MainWindow", "Open Logbook"))
        self.actionOpen_Logbook.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew_Logbook.setText(_translate("MainWindow", "New Logbook"))
        self.actionNew_Logbook.setToolTip(_translate("MainWindow", "New Logbook"))
        self.actionNew_Logbook.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionImport_File.setText(_translate("MainWindow", "Import File"))
        self.actionImport_File.setToolTip(_translate("MainWindow", "Import File"))
        self.actionImport_File.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSync_with_Garmin.setText(_translate("MainWindow", "Sync with Garmin"))
        self.actionSync_with_Garmin.setToolTip(_translate("MainWindow", "Sync with Garmin"))

import icons_rc
