# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Projects\Thesis_v2\Code\gui\first_version_final_v3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
from core import Core
import traceback

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(636, 433)
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
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(0)

        # self.resultSelectionModel = self.resultListView.selectionModel()
        # self.resultSelectionModel.selectionChanged.connect(self.resultSelectionChanged)

        # self.resultSelectionModel = self.resultListView.selectionModel()
        # self.resultSelectionModel.selectionChanged.connect(self.occuranceSelectionChanged)

        self.core = None
        self.working = False
        self.data = {}

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("window", "Settings Tab"))
        self.typeLabel.setText(_translate("window", "Category:"))
        self.resultLabel.setText(_translate("window", "Results:"))
        self.occuranceLabel.setText(_translate("window", "Occurance:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("window", "Results Tab"))
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

    def progressBarEvent(self):
        pass
    
    def updateDataEvent(self):
        print("Update data")
        self.loadOutput()

    def startPushButtonEvent(self):
        if self.working == False:
            self.working = True
            # Inform about starting
            print(self.inPathLineEdit.text(), " ", self.outPathLineEdit.text(), " ", self.dictPathLineEdit.text())
            try:
                self.core = Core(self.inPathLineEdit.text(), self.outPathLineEdit.text(), data=self.data, progressEvent=self.progressBarEvent, updateDataEvent=self.updateDataEvent)
            except Exception as x:
                self.displayException(x)
                #Inform about error
                self.stopPushButtonEvent()
                return
            self.core.start()

        # if self.working == False:
        #     self.working = True
        #     self.outputInfo['text'] = 'Creating parsing core'
        #     self.core = Core(self.progressbar, )
            
        #     self.outputInfo['text'] = 'Initialising input parser'
        #     try:
        #         self.core.initInputParser(self.inPath.get())
        #     except Exception as x:
        #         self.displayException(x)
        #         self.outputInfo['text'] = "Couldn't open input path"
        #         self.cancelFunction()
        #         return

        #     self.outputInfo['text'] = 'Initialising output'
        #     try:
        #         self.core.initOutput(self.outPath.get())
        #     except Exception as x:
        #         self.displayException(x)
        #         self.outputInfo['text'] = "Couldn't open output"
        #         self.cancelFunction()
        #         return

        #     self.outputInfo['text'] = 'Initialising default regexes'
        #     try:
        #         self.core.initRegexes(self.checkbuttonValues)
        #     except Exception as x:
        #         self.displayException(x)
        #         self.outputInfo['text'] = "Couldn't initialize regexes"
        #         self.cancelFunction()
        #         return
            
        #     if self.additionalValue.get() == 1:
        #         self.outputInfo['text'] = 'Initialising additional regexes'
        #         try:
        #             self.core.initAdditional()
        #         except Exception as x:
        #             self.displayException(x)
        #             self.outputInfo['text'] = "Failed to load additional regexes"
        #             self.cancelFunction()
        #             return

        #     if self.dictionaryValue.get() == 1:
        #         self.outputInfo['text'] = 'Initialising dictionary'
        #         try:
        #             self.core.initDictionary(self.dictPath.get())
        #         except Exception as x:
        #             self.displayException(x)
        #             self.outputInfo['text'] = "Couldn't open dictionary path"
        #             self.cancelFunction()
        #             return

        #     self.outputInfo['text'] = 'Started parsing'
        #     self.core.start()

    def stopPushButtonEvent(self):
        if self.core is not None:
            self.core.cancel = True
            self.core = None
        #reset progress bar

    def displayException(self, x):
        print("-"*15,"EXCEPTION","-"*15)
        print(type(x))
        print(x)
        print(traceback.format_exc())

    def setDebugValues(self):
        self.inPathLineEdit.setText("C:/Projects/ThesisTestData/facebook/facebookDump_50000.json")
        self.outPathLineEdit.setText("C:/Projects/ThesisTestData/results/output_facebookDump_50000.json")
        self.dictPathLineEdit.setText("")

    def loadDebugOutput(self):
        with open("C:\\Projects\\ThesisTestData\\results\\output_facebookDump_50000.json", 'r') as file:
            self.data = json.load(file)
        self.typeModel = QtCore.QStringListModel(self.data.keys())
        self.typeListView.setModel(self.typeModel)
        self.typeListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.typeSelectionModel = self.typeListView.selectionModel()
        self.typeSelectionModel.selectionChanged.connect(self.typeSelectionChanged)

    def typeSelectionChanged(self, index):
        self.selectedType = self.typeSelectionModel.selection().indexes()[0].data()
        self.resultModel = QtCore.QStringListModel(self.data[self.selectedType]['results'].keys())
        self.resultListView.setModel(self.resultModel)
        self.resultListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultSelectionModel = self.resultListView.selectionModel()
        self.resultSelectionModel.selectionChanged.connect(self.resultSelectionChanged)

    def resultSelectionChanged(self, index):
        self.selectedResult = self.resultSelectionModel.selection().indexes()[0].data()
        self.occuranceModel = QtCore.QStringListModel(self.data[self.selectedType]['results'][self.selectedResult]['occurances'])
        self.occuranceListView.setModel(self.occuranceModel)
        self.occuranceListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultSelectionModel = self.resultListView.selectionModel()
        self.resultSelectionModel.selectionChanged.connect(self.occuranceSelectionChanged)

    def occuranceSelectionChanged(self, index):
        pass

    def loadOutput(self):
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
    ui.loadDebugOutput()
    window.show()
    sys.exit(app.exec_())
