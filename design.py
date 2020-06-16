# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.MplWidget.setBaseSize(QtCore.QSize(1000, 1000))
        self.MplWidget.setObjectName("output_field")
        self.verticalLayout_2.addWidget(self.MplWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFX = QtWidgets.QLabel(self.centralwidget)
        self.labelFX.setObjectName("labelFX")
        self.horizontalLayout.addWidget(self.labelFX)
        self.input_function = QtWidgets.QLineEdit(self.centralwidget)
        self.input_function.setObjectName("input_function")
        self.horizontalLayout.addWidget(self.input_function)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelARR = QtWidgets.QLabel(self.centralwidget)
        self.labelARR.setObjectName("labelARR")
        self.horizontalLayout_2.addWidget(self.labelARR)
        self.input_array = QtWidgets.QLineEdit(self.centralwidget)
        self.input_array.setObjectName("input_array")
        self.horizontalLayout_2.addWidget(self.input_array)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.button_print = QtWidgets.QPushButton(self.centralwidget)
        self.button_print.setObjectName("button_print")
        self.verticalLayout.addWidget(self.button_print)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setObjectName("button_clear")
        self.verticalLayout.addWidget(self.button_clear)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFX.setText(_translate("MainWindow", "f(x)="))
        self.labelARR.setText(_translate("MainWindow", "<html><head/><body><p>Массив<br/>значений</p></body></html>"))
        self.button_print.setText(_translate("MainWindow", "Нарисовать график"))
        self.button_clear.setText(_translate("MainWindow", "Отчистить график"))
from mplwidget import MplWidget
