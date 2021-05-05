# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'physim_guiRrxfKj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.listView = QListView(self.groupBox)
        self.listView.setObjectName(u"listView")

        self.gridLayout_3.addWidget(self.listView, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.groupBox_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_2, 1, 2, 1, 1)

        self.horizontalSlider_3 = QSlider(self.groupBox_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.horizontalSlider_3, 2, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.toolBox = QToolBox(self.groupBox_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 347, 206))
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.horizontalSlider_4 = QSlider(self.page)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_4, 0, 2, 1, 1)

        self.horizontalSlider_6 = QSlider(self.page)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_6, 2, 2, 1, 1)

        self.horizontalSlider_5 = QSlider(self.page)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.horizontalSlider_5, 1, 2, 1, 1)

        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_5.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_5.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.toolBox.addItem(self.page, u"position")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 347, 206))
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_6.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.horizontalSlider_8 = QSlider(self.page_2)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_8, 0, 2, 1, 1)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_6.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.horizontalSlider_7 = QSlider(self.page_2)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_7, 1, 2, 1, 1)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_6.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.horizontalSlider_9 = QSlider(self.page_2)
        self.horizontalSlider_9.setObjectName(u"horizontalSlider_9")
        self.horizontalSlider_9.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_9, 2, 2, 1, 1)

        self.toolBox.addItem(self.page_2, u"velocity")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.page_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_7.addWidget(self.lineEdit_9, 0, 1, 1, 1)

        self.horizontalSlider_11 = QSlider(self.page_3)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider_11, 0, 2, 1, 1)

        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.page_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_7.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.horizontalSlider_10 = QSlider(self.page_3)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        self.horizontalSlider_10.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider_10, 1, 2, 1, 1)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.page_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_7.addWidget(self.lineEdit_10, 2, 1, 1, 1)

        self.horizontalSlider_12 = QSlider(self.page_3)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider_12, 2, 2, 1, 1)

        self.toolBox.addItem(self.page_3, u"acceleration")

        self.gridLayout_4.addWidget(self.toolBox, 0, 0, 1, 5)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.toolBox_2 = QToolBox(self.groupBox_3)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 196, 268))
        self.gridLayout_9 = QGridLayout(self.page_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_9.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.page_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_9.addWidget(self.label_14, 1, 0, 1, 1)

        self.horizontalSlider_13 = QSlider(self.page_4)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.horizontalSlider_13, 0, 2, 1, 1)

        self.horizontalSlider_14 = QSlider(self.page_4)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.horizontalSlider_14, 2, 2, 1, 1)

        self.horizontalSlider_15 = QSlider(self.page_4)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.horizontalSlider_15, 1, 2, 1, 1)

        self.label_15 = QLabel(self.page_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_9.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.page_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_9.addWidget(self.lineEdit_12, 0, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.page_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_9.addWidget(self.lineEdit_13, 1, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.page_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_9.addWidget(self.lineEdit_14, 2, 1, 1, 1)

        self.toolBox_2.addItem(self.page_4, u"position")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 347, 308))
        self.gridLayout_11 = QGridLayout(self.page_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_11.addWidget(self.label_16, 0, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.page_5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_11.addWidget(self.lineEdit_15, 0, 1, 1, 1)

        self.horizontalSlider_16 = QSlider(self.page_5)
        self.horizontalSlider_16.setObjectName(u"horizontalSlider_16")
        self.horizontalSlider_16.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSlider_16, 0, 2, 1, 1)

        self.label_17 = QLabel(self.page_5)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.page_5)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_11.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.horizontalSlider_17 = QSlider(self.page_5)
        self.horizontalSlider_17.setObjectName(u"horizontalSlider_17")
        self.horizontalSlider_17.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSlider_17, 1, 2, 1, 1)

        self.label_18 = QLabel(self.page_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 2, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.page_5)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_11.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.horizontalSlider_18 = QSlider(self.page_5)
        self.horizontalSlider_18.setObjectName(u"horizontalSlider_18")
        self.horizontalSlider_18.setOrientation(Qt.Horizontal)

        self.gridLayout_11.addWidget(self.horizontalSlider_18, 2, 2, 1, 1)

        self.toolBox_2.addItem(self.page_5, u"velocity")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 347, 268))
        self.gridLayout_12 = QGridLayout(self.page_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_19 = QLabel(self.page_8)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_12.addWidget(self.label_19, 0, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.page_8)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_12.addWidget(self.lineEdit_18, 0, 1, 1, 1)

        self.horizontalSlider_19 = QSlider(self.page_8)
        self.horizontalSlider_19.setObjectName(u"horizontalSlider_19")
        self.horizontalSlider_19.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.horizontalSlider_19, 0, 2, 1, 1)

        self.label_20 = QLabel(self.page_8)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_12.addWidget(self.label_20, 1, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.page_8)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_12.addWidget(self.lineEdit_19, 1, 1, 1, 1)

        self.horizontalSlider_20 = QSlider(self.page_8)
        self.horizontalSlider_20.setObjectName(u"horizontalSlider_20")
        self.horizontalSlider_20.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.horizontalSlider_20, 1, 2, 1, 1)

        self.label_21 = QLabel(self.page_8)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 2, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.page_8)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.gridLayout_12.addWidget(self.lineEdit_20, 2, 1, 1, 1)

        self.horizontalSlider_21 = QSlider(self.page_8)
        self.horizontalSlider_21.setObjectName(u"horizontalSlider_21")
        self.horizontalSlider_21.setOrientation(Qt.Horizontal)

        self.gridLayout_12.addWidget(self.horizontalSlider_21, 2, 2, 1, 1)

        self.toolBox_2.addItem(self.page_8, u"acceleration")

        self.gridLayout_13.addWidget(self.toolBox_2, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_10.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_10.addWidget(self.pushButton_6, 4, 0, 1, 1)

        self.listView_2 = QListView(self.groupBox_4)
        self.listView_2.setObjectName(u"listView_2")

        self.gridLayout_10.addWidget(self.listView_2, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_10.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.toolBox_3 = QToolBox(self.groupBox_4)
        self.toolBox_3.setObjectName(u"toolBox_3")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 478, 148))
        self.gridLayout_14 = QGridLayout(self.page_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_5 = QGroupBox(self.page_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_15 = QGridLayout(self.groupBox_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_15.addWidget(self.label_23, 0, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox_5)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.gridLayout_15.addWidget(self.lineEdit_23, 0, 1, 1, 1)

        self.horizontalSlider_22 = QSlider(self.groupBox_5)
        self.horizontalSlider_22.setObjectName(u"horizontalSlider_22")
        self.horizontalSlider_22.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_22, 0, 2, 1, 1)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_15.addWidget(self.label_22, 1, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox_5)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.gridLayout_15.addWidget(self.lineEdit_22, 1, 1, 1, 1)

        self.horizontalSlider_23 = QSlider(self.groupBox_5)
        self.horizontalSlider_23.setObjectName(u"horizontalSlider_23")
        self.horizontalSlider_23.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_23, 1, 2, 1, 1)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_15.addWidget(self.label_24, 2, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.groupBox_5)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.gridLayout_15.addWidget(self.lineEdit_21, 2, 1, 1, 1)

        self.horizontalSlider_24 = QSlider(self.groupBox_5)
        self.horizontalSlider_24.setObjectName(u"horizontalSlider_24")
        self.horizontalSlider_24.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_24, 2, 2, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_26 = QLabel(self.groupBox_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_16.addWidget(self.label_26, 0, 0, 1, 1)

        self.lineEdit_26 = QLineEdit(self.groupBox_6)
        self.lineEdit_26.setObjectName(u"lineEdit_26")

        self.gridLayout_16.addWidget(self.lineEdit_26, 0, 1, 1, 1)

        self.horizontalSlider_25 = QSlider(self.groupBox_6)
        self.horizontalSlider_25.setObjectName(u"horizontalSlider_25")
        self.horizontalSlider_25.setOrientation(Qt.Horizontal)

        self.gridLayout_16.addWidget(self.horizontalSlider_25, 0, 2, 1, 1)

        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_16.addWidget(self.label_25, 1, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.groupBox_6)
        self.lineEdit_25.setObjectName(u"lineEdit_25")

        self.gridLayout_16.addWidget(self.lineEdit_25, 1, 1, 1, 1)

        self.horizontalSlider_26 = QSlider(self.groupBox_6)
        self.horizontalSlider_26.setObjectName(u"horizontalSlider_26")
        self.horizontalSlider_26.setOrientation(Qt.Horizontal)

        self.gridLayout_16.addWidget(self.horizontalSlider_26, 1, 2, 1, 1)

        self.label_27 = QLabel(self.groupBox_6)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_16.addWidget(self.label_27, 2, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.groupBox_6)
        self.lineEdit_24.setObjectName(u"lineEdit_24")

        self.gridLayout_16.addWidget(self.lineEdit_24, 2, 1, 1, 1)

        self.horizontalSlider_27 = QSlider(self.groupBox_6)
        self.horizontalSlider_27.setObjectName(u"horizontalSlider_27")
        self.horizontalSlider_27.setOrientation(Qt.Horizontal)

        self.gridLayout_16.addWidget(self.horizontalSlider_27, 2, 2, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.toolBox_3.addItem(self.page_6, u"position")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 327, 108))
        self.gridLayout_17 = QGridLayout(self.page_7)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_29 = QLabel(self.page_7)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_17.addWidget(self.label_29, 0, 0, 1, 1)

        self.lineEdit_29 = QLineEdit(self.page_7)
        self.lineEdit_29.setObjectName(u"lineEdit_29")

        self.gridLayout_17.addWidget(self.lineEdit_29, 0, 1, 1, 1)

        self.horizontalSlider_28 = QSlider(self.page_7)
        self.horizontalSlider_28.setObjectName(u"horizontalSlider_28")
        self.horizontalSlider_28.setOrientation(Qt.Horizontal)

        self.gridLayout_17.addWidget(self.horizontalSlider_28, 0, 2, 1, 1)

        self.label_28 = QLabel(self.page_7)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_17.addWidget(self.label_28, 1, 0, 1, 1)

        self.lineEdit_28 = QLineEdit(self.page_7)
        self.lineEdit_28.setObjectName(u"lineEdit_28")

        self.gridLayout_17.addWidget(self.lineEdit_28, 1, 1, 1, 1)

        self.horizontalSlider_29 = QSlider(self.page_7)
        self.horizontalSlider_29.setObjectName(u"horizontalSlider_29")
        self.horizontalSlider_29.setOrientation(Qt.Horizontal)

        self.gridLayout_17.addWidget(self.horizontalSlider_29, 1, 2, 1, 1)

        self.label_30 = QLabel(self.page_7)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_17.addWidget(self.label_30, 2, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.page_7)
        self.lineEdit_27.setObjectName(u"lineEdit_27")

        self.gridLayout_17.addWidget(self.lineEdit_27, 2, 1, 1, 1)

        self.horizontalSlider_30 = QSlider(self.page_7)
        self.horizontalSlider_30.setObjectName(u"horizontalSlider_30")
        self.horizontalSlider_30.setOrientation(Qt.Horizontal)

        self.gridLayout_17.addWidget(self.horizontalSlider_30, 2, 2, 1, 1)

        self.toolBox_3.addItem(self.page_7, u"magnitute and direction")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_18 = QGridLayout(self.page_9)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.radioButton_2 = QRadioButton(self.page_9)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_18.addWidget(self.radioButton_2, 3, 0, 1, 1)

        self.radioButton = QRadioButton(self.page_9)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)

        self.gridLayout_18.addWidget(self.radioButton, 2, 0, 1, 1)

        self.toolBox_3.addItem(self.page_9, u"type")
        self.radioButton_2.raise_()
        self.radioButton.raise_()

        self.gridLayout_10.addWidget(self.toolBox_3, 5, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 5)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_19 = QGridLayout(self.groupBox_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.run_pause = QPushButton(self.groupBox_7)
        self.run_pause.setObjectName(u"run_pause")

        self.gridLayout_19.addWidget(self.run_pause, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")

        self.gridLayout_19.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSlider = QSlider(self.groupBox_7)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_19.addWidget(self.horizontalSlider, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"particle list", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"remove particle", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"add particle", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"clear list", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"particle controls", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"mass:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"charge:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"position", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"velocity", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"acceleration", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"electrical interaction between particles", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"particle", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"position", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"velocity", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"acceleration", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"fildes", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"add fields", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"clear list", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"remove field", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"starting point", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"ending point", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"position", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Z:", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"magnitute and direction", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"magnetic field", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"electric field", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_9), QCoreApplication.translate("MainWindow", u"type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"electro-magnetic effect of fields on a particle", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"simulation controls", None))
        self.run_pause.setText(QCoreApplication.translate("MainWindow", u"run", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"frame rate:", None))
    # retranslateUi

