# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Thesis_v2\Code\gui\preview_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreviewDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevPushButton = QtWidgets.QPushButton(Dialog)
        self.prevPushButton.setObjectName("prevPushButton")
        self.horizontalLayout.addWidget(self.prevPushButton)
        self.nextPushButton = QtWidgets.QPushButton(Dialog)
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout.addWidget(self.nextPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.prevPushButton.setText(_translate("Dialog", "Previous"))
        self.nextPushButton.setText(_translate("Dialog", "Next"))
