# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1046, 339)
        self.title = QtWidgets.QTextEdit(Form)
        self.title.setGeometry(QtCore.QRect(0, 269, 104, 31))
        self.title.setObjectName("title")
        self.degree = QtWidgets.QSpinBox(Form)
        self.degree.setGeometry(QtCore.QRect(110, 270, 131, 31))
        self.degree.setMaximum(10)
        self.degree.setObjectName("degree")
        self.cost = QtWidgets.QSpinBox(Form)
        self.cost.setGeometry(QtCore.QRect(640, 270, 91, 31))
        self.cost.setMaximum(99999)
        self.cost.setObjectName("cost")
        self.description = QtWidgets.QTextEdit(Form)
        self.description.setGeometry(QtCore.QRect(380, 270, 251, 31))
        self.description.setObjectName("description")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(640, 249, 101, 17))
        self.label_5.setObjectName("label_5")
        self.result = QtWidgets.QTableWidget(Form)
        self.result.setGeometry(QtCore.QRect(0, 9, 1041, 192))
        self.result.setObjectName("result")
        self.result.setColumnCount(0)
        self.result.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 249, 121, 17))
        self.label_3.setObjectName("label_3")
        self.volume = QtWidgets.QSpinBox(Form)
        self.volume.setGeometry(QtCore.QRect(740, 270, 171, 31))
        self.volume.setMaximum(99999)
        self.volume.setObjectName("volume")
        self.core = QtWidgets.QComboBox(Form)
        self.core.setGeometry(QtCore.QRect(250, 270, 121, 31))
        self.core.setObjectName("core")
        self.core.addItem("")
        self.core.addItem("")
        self.updateBtn = QtWidgets.QPushButton(Form)
        self.updateBtn.setGeometry(QtCore.QRect(0, 209, 1041, 25))
        self.updateBtn.setObjectName("updateBtn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 249, 131, 17))
        self.label_2.setObjectName("label_2")
        self.appendBtn = QtWidgets.QPushButton(Form)
        self.appendBtn.setGeometry(QtCore.QRect(920, 270, 121, 31))
        self.appendBtn.setObjectName("appendBtn")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(380, 249, 251, 17))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(740, 249, 181, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 250, 71, 17))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Цена (руб/кг)"))
        self.label_3.setText(_translate("Form", "Кофе в зернах?"))
        self.core.setItemText(0, _translate("Form", "Да"))
        self.core.setItemText(1, _translate("Form", "Нет"))
        self.updateBtn.setText(_translate("Form", "Применить"))
        self.label_2.setText(_translate("Form", "Степень обжарки:"))
        self.appendBtn.setText(_translate("Form", "Добавить"))
        self.label_4.setText(_translate("Form", "Опишите вкус в нескольких словах"))
        self.label_6.setText(_translate("Form", "Объем упаковки(грамм)"))
        self.label_7.setText(_translate("Form", "Название"))
