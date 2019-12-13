# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Thesis_v2\Code\gui\first_version_final_v3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from src.core import Core
import traceback
import os

class MySignal(QtCore.QObject):
    updateSignal = QtCore.pyqtSignal()
    finishedSignal = QtCore.pyqtSignal()
    progressBarSignal = QtCore.pyqtSignal()

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
        self.startPushButton.setEnabled(True)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.typeLabel = QtWidgets.QLabel(self.tab_2)
        self.typeLabel.setObjectName("typeLabel")
        self.verticalLayout_2.addWidget(self.typeLabel)
        self.typeListView = QtWidgets.QListView(self.tab_2)
        self.typeListView.setObjectName("typeListView")
        self.verticalLayout_2.addWidget(self.typeListView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resultLabel = QtWidgets.QLabel(self.tab_2)
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout_3.addWidget(self.resultLabel)
        self.resultListView = QtWidgets.QListView(self.tab_2)
        self.resultListView.setObjectName("resultListView")
        self.verticalLayout_3.addWidget(self.resultListView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.occuranceLabel = QtWidgets.QLabel(self.tab_2)
        self.occuranceLabel.setObjectName("occuranceLabel")
        self.verticalLayout_4.addWidget(self.occuranceLabel)
        self.occuranceListView = QtWidgets.QListView(self.tab_2)
        self.occuranceListView.setObjectName("occuranceListView")
        self.verticalLayout_4.addWidget(self.occuranceListView)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
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
        self.actionOpen_output = QtWidgets.QAction(window)
        self.actionOpen_output.setObjectName("actionOpen_output")
        self.actionOpen_output.triggered.connect(self.loadOutputFile)
        self.actionAbout = QtWidgets.QAction(window)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)
        self.menuFile.addAction(self.actionOpen_output)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)

        self.data = {}
        self.signal = MySignal()
        self.signal.updateSignal.connect(self.loadOutput)
        self.signal.finishedSignal.connect(self.loadOutput)
        self.signal.progressBarSignal.connect(self.increaseProgressbar)
        self.core = None
        self.working = False
        self.progressValue = 0
        self.progressBar.setRange(0, 100)

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
        self.typeLabel.setText(_translate("window", "Category:"))
        self.resultLabel.setText(_translate("window", "Results:"))
        self.occuranceLabel.setText(_translate("window", "Occurance:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("window", "Results"))
        self.menuFile.setTitle(_translate("window", "File"))
        self.actionOpen_output.setText(_translate("window", "Open output"))
        self.actionAbout.setText(_translate("window", "About"))

    def loadOutputFile(self):
        outputFilePath = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select output file')[0]
        with open(outputFilePath, 'r') as file:
            self.data = json.load(file)
        self.typeModel = QtCore.QStringListModel(self.data.keys())
        self.typeListView.setModel(self.typeModel)
        self.typeSelectionModel = self.typeListView.selectionModel()
        self.typeSelectionModel.selectionChanged.connect(self.typeSelectionChanged)

    def about(self):
        print("about")
        pass

    def inPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select input')[0]
        if fileName:
            self.inPathLineEdit.setText(fileName)

    def outPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self.window, 'Select output')[0]
        if fileName:
            self.outPathLineEdit.setText(fileName)

    def dictPathPushButtonEvent(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Select input')[0]
        if fileName:
            self.dictPathLineEdit.setText(fileName)

    def progressBarEvent(self):
        self.signal.progressBarSignal.emit()
    
    def updateDataEvent(self):
        # self.signal.sig_no_args.emit()
        pass

    def finishedDataEvent(self):
        self.signal.finishedSignal.emit()

    def startPushButtonEvent(self):
        if self.working == False:

            toCheck = []
            additional = False
            if self.ip_v4CheckBox.isChecked():
                toCheck.append("ip_v4")
            if self.ip_v6CheckBox.isChecked():
                toCheck.append("ip_v6")
            if self.socialSecNoCheckBox.isChecked():
                toCheck.append("socialsec")
            if self.idNoCheckBox.isChecked():
                toCheck.append("id_number")
            if self.macCheckButton.isChecked():
                toCheck.append("mac")
            if self.domainsCheckBox.isChecked():
                toCheck.append("domain")
            if self.emailsCheckBox.isChecked():
                toCheck.append("email")
            if self.passwdsCheckBox.isChecked():
                toCheck.append("password")
            if self.loginsCheckBox.isChecked():
                toCheck.append("login")
            if self.phoneNoCheckBox.isChecked():
                toCheck.append("phone_number")
            if self.additionalCheckBox.isChecked():
                additional = True

            self.progressValue = 0
            self.progressBar.setValue(self.progressValue)
            self.working = True

            if self.outPathLineEdit.text() == '':
                inPath = self.inPathLineEdit.text()
                self.outPathLineEdit.setText(os.path.splitext(inPath)[0] + "_output.json")

            try:
                self.core = Core(self.inPathLineEdit.text(), self.outPathLineEdit.text(), 
                                expectedRegexes=toCheck, data=self.data, additional=additional, 
                                progressEvent=self.progressBarEvent, finishedEvent=self.finishedDataEvent)

            except Exception as x:
                self.displayException(x)
                self.stopPushButtonEvent()
                return
            self.core.start()

    def stopPushButtonEvent(self):
        if self.core is not None:
            self.core.cancel = True
            self.core = None
        self.working = False
        #reset progress bar

    def displayException(self, x):
        print("-"*15,"EXCEPTION","-"*15)
        print(type(x))
        print(x)
        print(traceback.format_exc())

    def setDebugValues(self):
        self.inPathLineEdit.setText("C:/Projects/ThesisTestData/facebook/facebookDump_50000_strid.json")
        self.dictPathLineEdit.setText("")

    def loadDebugOutput(self):
        with open("C:\\Projects\\ThesisTestData\\results\\output_facebookDump_50000.json", 'r') as file:
            self.data = json.load(file)
        self.typeModel = QtCore.QStringListModel(self.data.keys())
        self.typeListView.setModel(self.typeModel)
        self.typeSelectionModel = self.typeListView.selectionModel()
        self.typeSelectionModel.selectionChanged.connect(self.typeSelectionChanged)

    def typeSelectionChanged(self, index):
        self.selectedType = self.typeSelectionModel.selection().indexes()[0].data()
        self.resultModel = QtCore.QStringListModel(self.data[self.selectedType]['results'].keys())
        self.resultListView.setModel(self.resultModel)
        self.resultSelectionModel = self.resultListView.selectionModel()
        self.resultSelectionModel.selectionChanged.connect(self.resultSelectionChanged)

    def resultSelectionChanged(self, index):
        self.selectedResult = self.resultSelectionModel.selection().indexes()[0].data()
        self.occuranceModel = QtCore.QStringListModel(self.data[self.selectedType]['results'][self.selectedResult]['occurances'])
        self.occuranceListView.setModel(self.occuranceModel)
        self.occuranceSelectionModel = self.occuranceListView.selectionModel()
        self.occuranceSelectionModel.selectionChanged.connect(self.occuranceSelectionChanged)

    def occuranceSelectionChanged(self, index):
        self.selectedOccurance = self.occuranceSelectionModel.selection().indexes()[0].data()
        self.inputData = json.load(open(self.inPathLineEdit.text(), 'r', encoding='utf-8'))
        i = 0
        self.inputIndex = 0
        for x in self.inputData["messages"]:
            if str(x["id"]) == self.selectedOccurance:
                self.inputIndex = i
                break
            i += 1
        self.dialog = QtWidgets.QDialog()
        self.Ui_previewDialog = Ui_PreviewDialog()
        self.Ui_previewDialog.setupUi(self.dialog)
        self.Ui_previewDialog.prevPushButton.clicked.connect(self.prevButtonEvent)
        self.Ui_previewDialog.nextPushButton.clicked.connect(self.nextButtonEvent)
        self.Ui_previewDialog.textBrowser.setText(self.inputData["messages"][self.inputIndex]["content"])
        self.dialog.show()

    def nextButtonEvent(self):
        self.inputIndex +=1
        self.Ui_previewDialog.textBrowser.setText(self.inputData["messages"][self.inputIndex]["content"])

    def prevButtonEvent(self):
        self.inputIndex -=1
        self.Ui_previewDialog.textBrowser.setText(self.inputData["messages"][self.inputIndex]["content"])


    def increaseProgressbar(self):
        self.progressValue += 1
        if self.progressValue < 101:
            self.progressBar.setValue(self.progressValue)

    def loadOutput(self):
        self.working = False
        self.typeModel = QtCore.QStringListModel(self.data.keys())
        self.typeListView.setModel(self.typeModel)
        self.typeListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.typeSelectionModel = self.typeListView.selectionModel()
        self.typeSelectionModel.selectionChanged.connect(self.typeSelectionChanged)

    def __del__(self):
        if self.core is not None:
            self.core.cancel = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    ui.setDebugValues()
    # ui.loadDebugOutput()
    window.show()
    sys.exit(app.exec_())
