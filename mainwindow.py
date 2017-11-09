# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon May 16 15:04:04 2016
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
        MainWindow.resize(800, 600)
        #MainWindow.setStyleSheet('background-image: url("/home/amrata/PycharmProjects/bowtieuser/images/tody.jpeg")')
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #palette1 = QtGui.QPalette()

        #palette1.setColor(QtGui.QPalette.Background, QtCore.Qt.white)

        #MainWindow.setPalette(palette1)
        #palette = QtGui.QPalette()

       # palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkCyan)
       # self.centralwidget.setPalette(palette)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget) # code for 1st scrollarea containing many push buttons
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 351, 531))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.scrollArea.setFont(font)
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setLineWidth(36)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 529))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        palette = QtGui.QPalette()

        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkCyan)
        #self.scrollAreaWidgetContents.setPalette(palette)
        self.genind = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for generate index pushbutton
        self.genind.setGeometry(QtCore.QRect(40, 80, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.genind.setFont(font)
        self.genind.setToolTip("Click on this button if you want to create a index for reference genome")
        self.genind.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.genind.setObjectName(_fromUtf8("genind"))


        self.allignment = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for alignment pushbutton
        self.allignment.setGeometry(QtCore.QRect(40, 130, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.allignment.setFont(font)
        self.allignment.setToolTip("This module containes the Allignment options")
        self.allignment.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.allignment.setObjectName(_fromUtf8("allignment"))

        self.cufflinks = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for cufflinks pushbutton
        self.cufflinks.setGeometry(QtCore.QRect(40, 180, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cufflinks.setFont(font)
        self.cufflinks.setToolTip("Click on this button if you want to use Cufflinks module")
        self.cufflinks.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cufflinks.setObjectName(_fromUtf8("cufflinks"))

        self.CuffCompare = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for Cuffcompare pushbutton
        self.CuffCompare.setGeometry(QtCore.QRect(40, 230, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.CuffCompare.setFont(font)
        self.CuffCompare.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.CuffCompare.setToolTip("Click on this button if you want to Compare the files")
        self.CuffCompare.setObjectName(_fromUtf8("CuffCompare"))

        self.Cuffnorm = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for Cuffnorm pushbutton
        self.Cuffnorm.setGeometry(QtCore.QRect(40, 280, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Cuffnorm.setFont(font)
        self.Cuffnorm.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Cuffnorm.setObjectName(_fromUtf8("Cuffnorm"))

        self.cuffdif = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for Cuffdiff pushbutton
        self.cuffdif.setGeometry(QtCore.QRect(40, 330, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cuffdif.setFont(font)
        self.cuffdif.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cuffdif.setObjectName(_fromUtf8("cuffdif"))

        self.cuffquant = QtGui.QPushButton(self.scrollAreaWidgetContents) # code for cuffquant pushbutton
        self.cuffquant.setGeometry(QtCore.QRect(40, 380, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cuffquant.setFont(font)
        self.cuffquant.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cuffquant.setObjectName(_fromUtf8("cuffquant"))

        self.Cuffmerge = QtGui.QPushButton(self.scrollAreaWidgetContents) #code for Cuffmerge pushbutton
        self.Cuffmerge.setGeometry(QtCore.QRect(40, 430, 271, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Cuffmerge.setFont(font)
        self.Cuffmerge.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Cuffmerge.setObjectName(_fromUtf8("Cuffmerge"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


        #seecond scroll area
        self.scrollArea_2 = QtGui.QScrollArea(self.centralwidget) ##code for scrollarea 2nd that contain image
        self.scrollArea_2.setGeometry(QtCore.QRect(370, 10, 411, 531))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea_2.setLineWidth(36)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 529))
        self.scrollArea_2.setStyleSheet('background-image: url("/home/amrata/PycharmProjects/bowtieuser/images/images.jpeg")')
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollAreaWidgetContents_2.setPalette(palette)

        self.frame = QtGui.QFrame(self.centralwidget) #code for declaring new frame
        self.frame.setGeometry(QtCore.QRect(10, 20, 791, 531))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        palette3 = QtGui.QPalette()
        palette3.setColor(QtGui.QPalette.Background, QtCore.Qt.darkCyan)
        self.frame.setPalette(palette3)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.label_5 = QtGui.QLabel(self.frame) #label for create reference genome or use built in index files
        self.label_5.setGeometry(QtCore.QRect(20, 20, 561, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.selfilcom = QtGui.QComboBox(self.frame) #code for combobox that is used to store user created reference genome.
        self.selfilcom.setGeometry(QtCore.QRect(90, 120, 651, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selfilcom.setFont(font)
        self.selfilcom.setObjectName(_fromUtf8("selfilcom"))

        self.builselcom = QtGui.QComboBox(self.frame)# code for combobox that contains already built in index files
        self.builselcom.setGeometry(QtCore.QRect(70, 120, 671, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.builselcom.setFont(font)
        self.builselcom.setObjectName(_fromUtf8("builselcom"))

        self.selfilebuil = QtGui.QPushButton(self.frame) # code for push button that select the built in index file
        self.selfilebuil.setGeometry(QtCore.QRect(20, 120, 31, 27))
        self.selfilebuil.setToolTip("Click on this if you want to select built in index other than this")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selfilebuil.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/amrata/PycharmProjects/bowtieuser/images/index.png")),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selfilebuil.setIcon(icon)
        self.selfilebuil.setObjectName(_fromUtf8("selfilebuil"))


        self.createind = QtGui.QComboBox(self.frame)  # code for combobox containg two options like create referenece genome or use built in RG
        self.createind.setGeometry(QtCore.QRect(20, 40, 721, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.createind.setFont(font)
        self.createind.setObjectName(_fromUtf8("createind"))
        self.createind.addItem(_fromUtf8(""))
        self.createind.setItemText(0, _fromUtf8(""))
        self.createind.addItem(_fromUtf8(""))
        self.createind.addItem(_fromUtf8(""))

        self.label_7 = QtGui.QLabel(self.frame) # label that contain select reference genome
        self.label_7.setGeometry(QtCore.QRect(20, 100, 291, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.selfile = QtGui.QPushButton(self.frame) # pushbutton for select  single user interested reference genome file
        self.selfile.setGeometry(QtCore.QRect(20, 120, 31, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selfile.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/home/amrata/PycharmProjects/bowtieuser/images/index.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selfile.setIcon(icon)
        self.selfile.setObjectName(_fromUtf8("selfile"))

        self.mulfile = QtGui.QPushButton(self.frame) # pushbutton for select  multiple user interested reference genome file
        self.mulfile.setGeometry(QtCore.QRect(50, 120, 31, 27))
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
        self.mulfile.setObjectName(_fromUtf8("mulfile"))

        self.algnoption = QtGui.QGroupBox(self.frame)# frame that containes 2 push buttons 1 bowtie and 2 tophat.
        self.algnoption.setGeometry(QtCore.QRect(20, 170, 711, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        self.algnoption.setFont(font)
        self.algnoption.setAutoFillBackground(False)
        self.algnoption.setTitle(_fromUtf8(""))
        self.algnoption.setFlat(True)
        self.algnoption.setObjectName(_fromUtf8("algnoption"))

        self.label = QtGui.QLabel(self.algnoption)# label for Choose alignment options
        self.label.setGeometry(QtCore.QRect(10, 10, 711, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.bowtie = QtGui.QPushButton(self.algnoption) # pushbutton Bowtie
        self.bowtie.setGeometry(QtCore.QRect(10, 40, 98, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bowtie.setFont(font)
        self.bowtie.setFlat(False)
        self.bowtie.setObjectName(_fromUtf8("bowtie"))

        self.tophat = QtGui.QPushButton(self.algnoption)# tophat pushbutton
        self.tophat.setGeometry(QtCore.QRect(10, 80, 98, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setBold(True)
        font.setWeight(75)
        self.tophat.setFont(font)
        self.tophat.setObjectName(_fromUtf8("tophat"))

        self.frame_2 = QtGui.QFrame(self.frame) #new frame in the already existing frame that containes cufflinks options
        self.frame_2.setGeometry(QtCore.QRect(30, 310, 711, 80))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(14)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.label_2 = QtGui.QLabel(self.frame_2)# label for Do you want to use Cufflinks
        self.label_2.setGeometry(QtCore.QRect(10, 10, 711, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Serif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.cuffyes = QtGui.QPushButton(self.frame_2) # yes option pushbutton(for to use cufflink)
        self.cuffyes.setGeometry(QtCore.QRect(10, 40, 98, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cuffyes.setFont(font)
        self.cuffyes.setObjectName(_fromUtf8("cuffyes"))

        self.cuffno = QtGui.QPushButton(self.frame_2) # no pushbutton(didnt use cufflinks)
        self.cuffno.setGeometry(QtCore.QRect(120, 40, 98, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.cuffno.setFont(font)
        self.cuffno.setObjectName(_fromUtf8("cuffno"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Will you create a reference genome  or use a built-in index?", None))
        self.createind.setItemText(1, _translate("MainWindow", "Use a built-in genome index", None))
        self.createind.setItemText(2, _translate("MainWindow", "Create a reference genome", None))
        self.label_7.setText(_translate("MainWindow", "Select reference genome\n"
"", None))
        self.selfile.setToolTip(_translate("MainWindow", "<html><head/><body><p>single</p></body></html>", None))
        self.algnoption.setToolTip(_translate("MainWindow", "please click here one of the option present in the below for allignment", None))
        self.label.setText(_translate("MainWindow", "Choose the options you wish to use for Allignment", None))
        self.bowtie.setText(_translate("MainWindow", "BOWTIE", None))
        self.tophat.setText(_translate("MainWindow", "TOPHAT", None))
        self.label_2.setText(_translate("MainWindow", "Do you want to use Cufflinks", None))
        self.cuffyes.setText(_translate("MainWindow", "YES", None))
        self.cuffno.setText(_translate("MainWindow", "NO", None))
        self.genind.setText(_translate("MainWindow", "Generate Index", None))
        self.allignment.setText(_translate("MainWindow", "Allignment", None))
        self.cufflinks.setText(_translate("MainWindow", "Cufflinks", None))
        self.CuffCompare.setText(_translate("MainWindow", "CuffCompare", None))
        self.Cuffnorm.setText(_translate("MainWindow", "CuffNorm", None))
        self.cuffdif.setText(_translate("MainWindow", "CuffDiff", None))
        self.cuffquant.setText(_translate("MainWindow", "CuffQuant", None))
        self.Cuffmerge.setText(_translate("MainWindow", "CuffMerge", None))


