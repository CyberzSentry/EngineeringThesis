# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Thesis_v2\Code\gui\first_version_final.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(636, 433)
        self.window = window
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outPathLineEdit = QtWidgets.QLineEdit(self.tab)
        self.outPathLineEdit.setObjectName("outPathLineEdit")
        self.gridLayout_2.addWidget(self.outPathLineEdit, 2, 2, 1, 1)
        self.inPathLabel = QtWidgets.QLabel(self.tab)
        self.inPathLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inPathLabel.setObjectName("inPathLabel")
        self.gridLayout_2.addWidget(self.inPathLabel, 0, 0, 1, 1)
        self.outPathLabel = QtWidgets.QLabel(self.tab)
        self.outPathLabel.setObjectName("outPathLabel")
        self.gridLayout_2.addWidget(self.outPathLabel, 2, 0, 1, 1)
        self.dictPathPushButton = QtWidgets.QPushButton(self.tab)
        self.dictPathPushButton.setObjectName("dictPathPushButton")
        self.dictPathPushButton.clicked.connect(self.dictPathPushButtonEvent)
        self.gridLayout_2.addWidget(self.dictPathPushButton, 3, 3, 1, 1)
        self.dictPathLabel = QtWidgets.QLabel(self.tab)
        self.dictPathLabel.setObjectName("dictPathLabel")
        self.gridLayout_2.addWidget(self.dictPathLabel, 3, 0, 1, 1)
        self.dictPathLineEdit = QtWidgets.QLineEdit(self.tab)
        self.dictPathLineEdit.setObjectName("dictPathLineEdit")
        self.gridLayout_2.addWidget(self.dictPathLineEdit, 3, 2, 1, 1)
        self.outPathPushButton = QtWidgets.QPushButton(self.tab)
        self.outPathPushButton.setObjectName("outPathPushButton")
        self.outPathPushButton.clicked.connect(self.outPathPushButtonEvent)
        self.gridLayout_2.addWidget(self.outPathPushButton, 2, 3, 1, 1)
        self.inPathPushButton = QtWidgets.QPushButton(self.tab)
        self.inPathPushButton.setObjectName("inPathPushButton")
        self.inPathPushButton.clicked.connect(self.inPathPushButtonEvent)
        self.gridLayout_2.addWidget(self.inPathPushButton, 0, 3, 1, 1)
        self.inPathLineEdit = QtWidgets.QLineEdit(self.tab)
        self.inPathLineEdit.setObjectName("inPathLineEdit")
        self.gridLayout_2.addWidget(self.inPathLineEdit, 0, 2, 1, 1)
        self.outputLabel = QtWidgets.QLabel(self.tab)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outputLabel.setTextFormat(QtCore.Qt.PlainText)
        self.outputLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout_2.addWidget(self.outputLabel, 5, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startPushButton = QtWidgets.QPushButton(self.tab)
        self.startPushButton.setStyleSheet("background-color: green")
        self.startPushButton.setObjectName("startPushButton")
        self.startPushButton.clicked.connect(self.startPushButtonEvent)
        self.verticalLayout.addWidget(self.startPushButton)
        self.stopPushButton = QtWidgets.QPushButton(self.tab)
        self.stopPushButton.setStyleSheet("background-color: red")
        self.stopPushButton.setObjectName("stopPushButton")
        self.stopPushButton.clicked.connect(self.stopPushButtonEvent)
        self.verticalLayout.addWidget(self.stopPushButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 5, 3, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.domainsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.domainsCheckBox.setObjectName("domainsCheckBox")
        self.gridLayout_5.addWidget(self.domainsCheckBox, 1, 1, 1, 1)
        self.dictCheckBox = QtWidgets.QCheckBox(self.tab)
        self.dictCheckBox.setObjectName("dictCheckBox")
        self.gridLayout_5.addWidget(self.dictCheckBox, 2, 2, 1, 1)
        self.ip_v4CheckBox = QtWidgets.QCheckBox(self.tab)
        self.ip_v4CheckBox.setObjectName("ip_v4CheckBox")
        self.gridLayout_5.addWidget(self.ip_v4CheckBox, 0, 0, 1, 1)
        self.idNoCheckBox = QtWidgets.QCheckBox(self.tab)
        self.idNoCheckBox.setObjectName("idNoCheckBox")
        self.gridLayout_5.addWidget(self.idNoCheckBox, 0, 3, 1, 1)
        self.emailsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.emailsCheckBox.setObjectName("emailsCheckBox")
        self.gridLayout_5.addWidget(self.emailsCheckBox, 1, 2, 1, 1)
        self.passwdsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.passwdsCheckBox.setObjectName("passwdsCheckBox")
        self.gridLayout_5.addWidget(self.passwdsCheckBox, 1, 3, 1, 1)
        self.loginsCheckBox = QtWidgets.QCheckBox(self.tab)
        self.loginsCheckBox.setObjectName("loginsCheckBox")
        self.gridLayout_5.addWidget(self.loginsCheckBox, 2, 0, 1, 1)
        self.additionalCheckBox = QtWidgets.QCheckBox(self.tab)
        self.additionalCheckBox.setObjectName("additionalCheckBox")
        self.gridLayout_5.addWidget(self.additionalCheckBox, 2, 3, 1, 1)
        self.socialSecNoCheckBox = QtWidgets.QCheckBox(self.tab)
        self.socialSecNoCheckBox.setObjectName("socialSecNoCheckBox")
        self.gridLayout_5.addWidget(self.socialSecNoCheckBox, 0, 2, 1, 1)
        self.macCheckButton = QtWidgets.QCheckBox(self.tab)
        self.macCheckButton.setObjectName("macCheckButton")
        self.gridLayout_5.addWidget(self.macCheckButton, 1, 0, 1, 1)
        self.ip_v6CheckBox = QtWidgets.QCheckBox(self.tab)
        self.ip_v6CheckBox.setObjectName("ip_v6CheckBox")
        self.gridLayout_5.addWidget(self.ip_v6CheckBox, 0, 1, 1, 1)
        self.phoneNoCheckBox = QtWidgets.QCheckBox(self.tab)
        self.phoneNoCheckBox.setObjectName("phoneNoCheckBox")
        self.gridLayout_5.addWidget(self.phoneNoCheckBox, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 4, 0, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.columnView = QtWidgets.QColumnView(self.tab_2)
        self.columnView.setObjectName("columnView")
        self.gridLayout_3.addWidget(self.columnView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "SDSE"))
        self.inPathLabel.setText(_translate("window", "Input path:"))
        self.outPathLabel.setText(_translate("window", "Output path:"))
        self.dictPathPushButton.setText(_translate("window", "Browse"))
        self.dictPathLabel.setText(_translate("window", "Dictionary path:"))
        self.outPathPushButton.setText(_translate("window", "Browse"))
        self.inPathPushButton.setText(_translate("window", "Browse"))
        self.outputLabel.setText(_translate("window", "Output"))
        self.startPushButton.setText(_translate("window", "Start"))
        self.stopPushButton.setText(_translate("window", "Stop"))
        self.domainsCheckBox.setText(_translate("window", "Domains"))
        self.dictCheckBox.setText(_translate("window", "Dictionary"))
        self.ip_v4CheckBox.setText(_translate("window", "IP v4"))
        self.idNoCheckBox.setText(_translate("window", "ID no"))
        self.emailsCheckBox.setText(_translate("window", "Emails"))
        self.passwdsCheckBox.setText(_translate("window", "Passwords"))
        self.loginsCheckBox.setText(_translate("window", "Logins"))
        self.additionalCheckBox.setText(_translate("window", "Additional"))
        self.socialSecNoCheckBox.setText(_translate("window", "Social Sec no"))
        self.macCheckButton.setText(_translate("window", "MAC"))
        self.ip_v6CheckBox.setText(_translate("window", "IP v6"))
        self.phoneNoCheckBox.setText(_translate("window", "Phone no."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("window", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("window", "Results"))
        self.menuFile.setTitle(_translate("window", "File"))

    def inPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select input')[0]
        self.inPathLineEdit.setText(fileName)

    def outPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select input')[0]
        self.outPathLineEdit.setText(fileName)

    def dictPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select input')[0]
        self.dictPathLineEdit.setText(fileName)

    def startPushButtonEvent(self):
        pass

    def stopPushButtonEvent(self):
        pass

    def displayException(self, x):
        print("-"*15,"EXCEPTION","-"*15)
        print(type(x))
        print(x)
        print(traceback.format_exc())

    def setDebugValues(self):
        self.inPathLineEdit.setText("C:/Projects/ThesisTestData/facebook/facebookDump_50000.json")
        self.outPathLineEdit.setText("C:/Projects/ThesisTestData/results")
        self.dictPathLineEdit.setText("")

    def loadDebugOutput(self):
        outputModel = QtGui.QStandardItemModel()
        outputModel.setHorizontalHeaderLabels(['Column1', 'Column2', 'Column3'])
        for x in range(5):
            group = QtGui.QStandardItem("Group: " + str(x))
            group.setEditable(False)
            for y in range(6):
                child = QtGui.QStandardItem("Child: " + str(y))
                child.setEditable(False)
                for z in range(3):
                    subChild = QtGui.QStandardItem("Sub_child: " + str(z))
                    subChild.setEditable(False) 
                    
                    child.appendRow(subChild)
                group.appendRow(child)
            outputModel.appendRow(group)


        outputModel.itemChanged.connect(self.testEvent2)
        self.columnView.setModel(outputModel)
        self.columnView.clicked.connect(self.testEvent)

    def loadOutput(self):
        pass

    def testEvent(self, index):
        print("Test event occured ", index.row(), " ", index.column())

    def testEvent2(self, item):
        print("Test event 2")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    ui.setDebugValues()
    ui.loadDebugOutput()
    window.show()
    sys.exit(app.exec_())
