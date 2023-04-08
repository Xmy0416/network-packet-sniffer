# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Vera Sans"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.filter = QtGui.QLineEdit(self.centralwidget)
        self.filter.setGeometry(QtCore.QRect(180, 50, 441, 27))
        self.filter.setObjectName(_fromUtf8("LineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 201, 27))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 90, 181, 27))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.list_submissions = QtGui.QListWidget(self.centralwidget)
        self.list_submissions.setGeometry(QtCore.QRect(20, 160, 661, 192))
        self.list_submissions.setBatchSize(1)
        self.list_submissions.setObjectName(_fromUtf8("list_submissions"))
        # self.tableView = QtGui.QTableView(self.centralwidget)
        # self.tableView.setGeometry(QtCore.QRect(20, 160, 661, 192))
        # self.tableView.setObjectName(_fromUtf8("tableView"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 380, 640, 150))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStart_capture = QtGui.QMenu(self.menubar)
        self.menuStart_capture.setObjectName(_fromUtf8("menuStart_capture"))
        self.menuStop_capture = QtGui.QMenu(self.menubar)
        self.menuStop_capture.setObjectName(_fromUtf8("menuStop_capture"))
        self.menuRestart = QtGui.QMenu(self.menubar)
        self.menuRestart.setObjectName(_fromUtf8("menuRestart"))
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuStart_capture.menuAction())
        self.menubar.addAction(self.menuStop_capture.menuAction())
        self.menubar.addAction(self.menuRestart.menuAction())
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fifa_N_Wireshark", None))
        self.label.setText(_translate("MainWindow", "Capture", None))
        self.label_2.setText(_translate("MainWindow", "using this filter:", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        self.pushButton_2.setText(_translate("MainWindow", "Reset", None))
        ##self.pushButton_5.setText(_translate("MainWindow", "start", None))
        self.menuStart_capture.setTitle(_translate("MainWindow", "start capture", None))
        self.menuStop_capture.setTitle(_translate("MainWindow", "stop capture", None))
        self.menuRestart.setTitle(_translate("MainWindow", "refresh", None))

