# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bowtiegui.ui'
#
# Created: Tue Mar  1 14:46:40 2016
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(930, 1500)
        MainWindow.setMinimumSize(QtCore.QSize(0, 1500))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 1500))
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.centralWidget = QtGui.QWidget(MainWindow)
        layout = QtGui.QVBoxLayout(self.centralWidget)
        layout.addWidget(self.scrollArea)

        #self.scrollArea.setGeometry(QtCore.QRect(0, 0, 41, 111))
        #self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        #self.scrollAreaWidgetContents = QtGui.QWidget()
       # self.scrollArea.setGeometry(QtCore.QRect(230, 0, 841, 2481))
        self.scrollArea.setFrameShape(QtGui.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(7)
        self.scrollArea.setWidgetResizable(False)
       # self.scrollArea.setToolTip("place cursor over the controls for information")

        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 850,1252))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        layout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.frame = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setGeometry(QtCore.QRect(50, 10, 801, 1200))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(10)

        #self.setStyleSheet('background-image: url("/home/amrata/PycharmProjects/bowtieuser/images/images/logn.jpg")')
        self.frame.setObjectName(_fromUtf8("frame"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)



        self.selgtflbl = QtGui.QLabel(self.frame) # select gtf file
        self.selgtflbl.setGeometry(QtCore.QRect(10, 30, 391, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setWeight(75)
        self.selgtflbl.setFont(font)
        self.selgtflbl.setToolTip("select the GTF file produced by cufflinks")
        self.selgtflbl.setObjectName(_fromUtf8("selgtflbl"))
        self.selfile = QtGui.QPushButton(self.frame) # single gtf file
        self.selfile.setGeometry(QtCore.QRect(10, 50, 31, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selfile.setFont(font)
        self.selfile.setToolTip("Click here to select single GTF file")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/amrata/PycharmProjects/bowtieuser/images/index.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selfile.setIcon(icon)
        self.selfile.setToolTip("click here to select the file")
        self.selfile.setObjectName(_fromUtf8("selfile"))
        self.mulfile = QtGui.QPushButton(self.frame)
        self.mulfile.setGeometry(QtCore.QRect(40, 50, 31, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mulfile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/amrata/PycharmProjects/bowtieuser/images/index1.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mulfile.setIcon(icon)
        self.mulfile.setToolTip("Click here to select multiple GTF file")
        self.mulfile.setObjectName(_fromUtf8("mulfile"))
        self.builselcom = QtGui.QComboBox(self.frame)
        self.builselcom.setGeometry(QtCore.QRect(90, 50, 681, 27))
        self.builselcom.setToolTip("Please select the file")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        #font.setBold(True)
        #font.setPointSize(11)
        #font.setBold(False)
        #font.setItalic(False)
        font.setWeight(50)
        self.builselcom.setFont(font)
        self.builselcom.setObjectName(_fromUtf8("builselcom"))

        self.refanotlbl = QtGui.QLabel(self.frame) #Do you want to use the Reference Annotation
        self.refanotlbl.setGeometry(QtCore.QRect(10, 100, 711, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.refanotlbl.setFont(font)
        self.refanotlbl.setObjectName(_fromUtf8("refanotlbl"))
        self.refannotcmb = QtGui.QComboBox(self.frame)
        self.refannotcmb.setGeometry(QtCore.QRect(10, 120, 761, 27))
        self.refannotcmb.setToolTip("Select yes to provide reference annotation")
        self.refannotcmb.addItem(_fromUtf8(""))
        self.refannotcmb.addItem(_fromUtf8(""))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.refannotcmb.setFont(font)
        self.refannotcmb.setObjectName(_fromUtf8("refannotcmb"))

        self.groupBox = QtGui.QGroupBox(self.frame) # groupbox that containes reference annot. file
        self.groupBox.setGeometry(QtCore.QRect(10, 150,800, 261))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.subrefanlbl1 = QtGui.QLabel(self.groupBox) # ref.anno.
        self.subrefanlbl1.setGeometry(QtCore.QRect(10, 20, 711, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subrefanlbl1.setFont(font)
        self.subrefanlbl1.setObjectName(_fromUtf8("subrefanlbl"))
        self.subrefanpush1 = QtGui.QPushButton(self.groupBox)
        self.subrefanpush1.setGeometry(QtCore.QRect(10, 40, 31, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subrefanpush1.setFont(font)
        self.subrefanpush1.setText(_fromUtf8(""))
        self.subrefanpush1.setToolTip("Click here to select Single reference annotation file")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../img/index.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.subrefanpush1.setIcon(icon)
        self.subrefanpush1.setObjectName(_fromUtf8("subrefanpusk1"))
        self.mulfile1 = QtGui.QPushButton(self.groupBox)
        self.mulfile1.setGeometry(QtCore.QRect(40, 40, 31, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mulfile1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/amrata/PycharmProjects/bowtieuser/images/index1.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mulfile1.setIcon(icon)
        self.mulfile1.setToolTip("Click here to select multiple reference annotation file")
        self.mulfile1.setObjectName(_fromUtf8("mulfile1"))
        self.subrefcomb = QtGui.QComboBox(self.groupBox)
        self.subrefcomb.setGeometry(QtCore.QRect(80, 40, 681, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        #font.setBold(True)
        font.setWeight(50)
        self.subrefcomb.setFont(font)
        self.subrefcomb.setObjectName(_fromUtf8("subrefcomb"))

        self.ovrhngtollbl = QtGui.QLabel(self.groupBox) #Do you want to Ignore reference transcripts that are not overlapped by any input transfrags
        self.ovrhngtollbl.setGeometry(QtCore.QRect(10, 90, 810, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ovrhngtollbl.setFont(font)
        self.ovrhngtollbl.setObjectName(_fromUtf8("ovrhngtollbl"))

        self.spno = QtGui.QPushButton(self.groupBox)
        self.spno.setGeometry(QtCore.QRect(70, 110, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setWeight(50)
        self.spno.setFont(font)
        self.spno.setObjectName(_fromUtf8("spno"))
        self.spyes = QtGui.QPushButton(self.groupBox)
        self.spyes.setToolTip("Click here if you want to ignore reference transcripts that are not overlapped by any input transfrags otherwise click No ")
        self.spyes.setGeometry(QtCore.QRect(10, 110, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setWeight(50)
        self.spyes.setFont(font)
        self.spyes.setObjectName(_fromUtf8("spyes"))

        self.ovrhngtollbl1 = QtGui.QLabel(self.groupBox) #Do you want to Ignore input transcripts that are not overlapped by any reference transcripts
        self.ovrhngtollbl1.setGeometry(QtCore.QRect(10, 160, 811, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ovrhngtollbl1.setFont(font)
        self.ovrhngtollbl1.setObjectName(_fromUtf8("ovrhngtollbl"))
        self.spno1 = QtGui.QPushButton(self.groupBox)
        self.spno1.setGeometry(QtCore.QRect(70, 180, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)

        font.setWeight(50)
        self.spno1.setFont(font)
        self.spno1.setObjectName(_fromUtf8("spno"))
        self.spyes1 = QtGui.QPushButton(self.groupBox)
        self.spyes1.setGeometry(QtCore.QRect(10, 180, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)

        font.setWeight(50)
        self.spyes1.setFont(font)
        self.spyes1.setToolTip("Click here if you want to Ignore input transcripts that are not overlapped by any reference transcripts")
        self.spyes1.setObjectName(_fromUtf8("spyes"))

        self.frame2 = QtGui.QGroupBox(self.frame)
        self.frame2.setGeometry(QtCore.QRect(10, 170, 811, 541))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame2.setFont(font)
        self.frame2.setTitle(_fromUtf8(""))
        self.frame2.setObjectName(_fromUtf8("frame2"))

        self.label_8 = QtGui.QLabel(self.frame2) #Do you want to discard (ignore) single-exon transcripts
        self.label_8.setGeometry(QtCore.QRect(0, 0, 491, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.inp = QtGui.QComboBox(self.frame2)
        self.inp.setGeometry(QtCore.QRect(0, 20, 761, 27))
        self.inp.setToolTip("Click Yes for Provide values to input parameter and No for provide default values to input parameters")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inp.setFont(font)
        self.inp.setObjectName(_fromUtf8("inp"))
        self.inp.addItem(_fromUtf8(""))
        self.inp.addItem(_fromUtf8(""))
        self.inp.addItem(_fromUtf8(""))
        #self.yesnext = QtGui.QGroupBox(self.pargp)
       # self.yesnext.setGeometry(QtCore.QRect(10, 70, 801, 1201))
       # self.yesnext.setTitle(_fromUtf8(""))
       # self.yesnext.setObjectName(_fromUtf8("yesnext"))

        self.label_28 = QtGui.QLabel(self.frame2) #Do you want to Set the value for Max. Distance for assessing exon accuracy
        self.label_28.setGeometry(QtCore.QRect(0, 70, 791, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))

        self.skip = QtGui.QTextEdit(self.frame2)
        self.skip.setGeometry(QtCore.QRect(0, 90, 761, 25))
        self.skip.setToolTip("Please provide integer value")
        self.skip.setObjectName(_fromUtf8("skip"))

        self.encolbl = QtGui.QLabel(self.frame2) #Do you want to set the  value for Max.Distance for transcript grouping
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setWeight(75)
        self.encolbl.setFont(font)
        self.encolbl.setGeometry(QtCore.QRect(0,140, 641, 17))
        self.encolbl.setObjectName(_fromUtf8("encolbl"))
        self.textEdit1 = QtGui.QTextEdit(self.frame2)
        self.textEdit1.setGeometry(QtCore.QRect(0, 160, 761, 25))
        self.textEdit1.setToolTip("Please provide integer value")
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))



        self.label_35 = QtGui.QLabel(self.frame2) #Do you want to discard intron-redundant transfrags sharing 5
        self.label_35.setGeometry(QtCore.QRect(0, 210, 551, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setWeight(75)

        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_34"))

        self.asno = QtGui.QPushButton(self.frame2)
        self.asno.setGeometry(QtCore.QRect(50, 230, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setWeight(50)
        self.asno.setFont(font)
        self.asno.setObjectName(_fromUtf8("asno"))
        self.asyes = QtGui.QPushButton(self.frame2)
        self.asyes.setGeometry(QtCore.QRect(0, 230, 51, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)
        font.setWeight(50)
        self.asyes.setFont(font)
        self.asyes.setToolTip("Click here if you want to discard intron-redundant transfrags sharing 5 otherwise click NO")
        self.asyes.setObjectName(_fromUtf8("asyes"))


        self.Execute = QtGui.QPushButton(self.frame)
        self.Execute.setGeometry(QtCore.QRect(660, 480, 98, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(11)

        font.setWeight(75)
        self.Execute.setFont(font)
        self.Execute.setToolTip("Click here if you are submit these values")
        self.Execute.setObjectName(_fromUtf8("Execute"))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CUFFCOMPARE", None))

        self.selgtflbl.setText(_translate("MainWindow", "Select the gtf file produced by cufflinks?\n"
"", None))
        self.refanotlbl.setText(_translate("MainWindow", "Do you want to use the Reference Annotation?\n""",None))
        self.refannotcmb.setItemText(0, _translate("MainWindow", "Yes", None))
        self.refannotcmb.setItemText(1, _translate("MainWindow", "No", None))
        self.subrefanlbl1.setText(_translate("MainWindow", "Select Reference Annotation\n"
"", None))

        self.ovrhngtollbl.setText(_translate("MainWindow", "Do you want to Ignore reference transcripts that are not overlapped by any input transfrags", None))
        self.spno.setText(_translate("MainWindow", "No", None))
        self.spyes.setText(_translate("MainWindow", "Yes", None))
        self.ovrhngtollbl1.setText(_translate("MainWindow", "Do you want to Ignore input transcripts that are not overlapped by any reference transcripts", None))
        self.spno1.setText(_translate("MainWindow", "No", None))
        self.spyes1.setText(_translate("MainWindow", "Yes", None))


        self.label_8.setText(_translate("MainWindow", "Do you want to discard (ignore) single-exon transcripts", None))

        self.inp.setItemText(0, _translate("MainWindow", "No", None))
        self.inp.setItemText(1, _translate("MainWindow", "Discard single-exon transfrag and reference transcripts", None))
        self.inp.setItemText(2, _translate("MainWindow", "Discard single-exon reference transcripts", None))

        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.Execute.setText(_translate("MainWindow", "Execute", None))
        self.label_28.setText(_translate("MainWindow", "Do you want to Set the value for Max. Distance for assessing exon accuracy", None))
        self.encolbl.setText(_translate("MainWindow", "Do you want to set the  value for Max.Distance for transcript grouping", None))
        self.label_35.setText(_translate("MainWindow", "Do you want to discard intron-redundant transfrags sharing 5'",None))


        self.asno.setText(_translate("MainWindow", "No", None))
        self.asyes.setText(_translate("MainWindow", "Yes", None))

