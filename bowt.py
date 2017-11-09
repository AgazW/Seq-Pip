from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import bowtiegui
import subprocess
import allignment
import pickle

#import images
from subprocess import call
import os
import cuff
from subprocess import Popen, PIPE
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge




class Bowt(QtGui.QMainWindow,bowtiegui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None): # initializing all the variables amd link all the functions
        super(Bowt, self).__init__( parent)
        self.setupUi(self)
        self.rd = " "
        fp = open("shared.pkl","rb")
        self.file = pickle.load(fp)

        #fp1 = open("sharedcuff.pkl","rb")
       # self.cont = pickle.load(fp1)
        fptr1 = open("botout.pkl","rb")
        self.botout = pickle.load(fptr1)
        fptr1.close()
        #os.system('rm sharedcufffile.pkl')
        fpt1 = open("build.pkl","rb")
        self.buildfile = pickle.load(fpt1)
        fpt1.close()
        filp = open("nocont.pkl","rb")
        self.nofil = pickle.load(filp)
        filp.close()
        self.outputframe.hide()
        self.framepair.hide()
        self.readfl1 = " "
        self.readfl2 = " "
        self.read= " "
        self.read1= " "
        self.framepair1.hide()
        self.out1= " "
        self.txt =" "
        self.txt1=" "
        self.parent = parent
        self.pairedgrp.hide()
        self.sth = self.anal.currentText()
        self.pargp.hide()
        self.yesgp.hide()
       # self.builselcom.hide()
        self.groupBox.show()
        self.more.hide()
        self.frame_2.hide()
        self.scrfrm.hide()
        self.str1 = " "
       # self.lclfrm.hide()
        self.akfrm.hide()
        self.stri = " "
        self.st = " "
        self.efrtfrm.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        #self.anal.connect(self.anal,SIGNAL("currentIndexChanged(int)"),SLOT("onIndexChange(int)"))
        self.connect(self.anal, SIGNAL('activated(QString)'), self.onIndexChange)
        self.connect(self.inp, SIGNAL('activated(QString)'), self.onIndexChange2)
        self.connect(self.score, SIGNAL('activated(QString)'), self.showscr)
        self.connect(self.samcmb_2, SIGNAL('activated(QString)'), self.nextshow)
        self.connect(self.comboBox_8, SIGNAL('activated(QString)'), self.msgshw)
        self.connect(self.paircmb, SIGNAL('activated(QString)'), self.pair)
        self.connect(self.inpou1, SIGNAL('activated(QString)'), self.output)
        self.Execute.clicked.connect(self.onIndexChange1)
        self.push1.clicked.connect(self.readfile1)
        self.push2.clicked.connect(self.readfile2)
        self.mulfile1.clicked.connect(self.multifile1)
        self.mulfile.clicked.connect(self.multifile2)
        self.push21.clicked.connect(self.readfile21)
        self.mulfile11.clicked.connect(self.multifile11)
        self.disyes.clicked.connect(self.cond)
        self.discs.clicked.connect(self.cond1)
        self.allowyes.clicked.connect(self.cond2)
        self.diss.clicked.connect(self.cond3)
        self.mateyes.clicked.connect(self.cond4)
        self.fr.toggled.connect(self.frr)
        self.rf.toggled.connect(self.rfr)
        self.ff.toggled.connect(self.ffr)
        self.Qseqyes.clicked.connect(self.Qseqop)
        self.memyes.clicked.connect(self.memo)
        self.prntyes.clicked.connect(self.printop)
        self.usgtxt.clicked.connect(self.usage)
        self.radioButton.toggled.connect(self.setrdb)
        self.radioButton_2.toggled.connect(self.radiobutton2)
        self.radioButton_12.toggled.connect(self.ph33)
        self.radioButton_13.toggled.connect(self.ph64)
        self.radioButton_3.toggled.connect(self.default1)
        self.radioButton_4.toggled.connect(self.default2)
        self.radioButton_5.toggled.connect(self.default3)
        self.radioButton_6.toggled.connect(self.default4)
        self.radioButton_7.toggled.connect(self.default5)
        self.radioButton_8.toggled.connect(self.default6)
        self.radioButton_9.toggled.connect(self.default7)
        self.radioButton_10.toggled.connect(self.default8)
        self.radioButton_11.toggled.connect(self.default9)
        self.spyes.clicked.connect(self.spconvert)
        self.spno.clicked.connect(self.spno1)
        self.asyes.clicked.connect(self.asciconvert)
        self.asno.clicked.connect(self.ascino)
        self.Samyes.clicked.connect(self.samout)
        self.samnopb.clicked.connect(self.samnoshow)
        self.seqyespb.clicked.connect(self.seqgo)
        self.seqnopb.clicked.connect(self.seqnogo)
        self.pushButtonyes.clicked.connect(self.time)
        self.pushButtonyes_3.clicked.connect(self.time1)
        self.pushButtonyes_5.clicked.connect(self.time2)
        self.pushButtonyes_10.clicked.connect(self.time3)
        self.ok.clicked.connect(self.okclicked)
        self.pushButtok.clicked.connect(self.okclick)
        self.Execute1.clicked.connect(self.executeclick)
        #self.selfile.clicked.connect(self.selectFile)
        self.pushButton_7.clicked.connect(self.true1)
        self.pushButton_6.clicked.connect(self.false1)
        self.pushButton_9.clicked.connect(self.true2)
        self.pushButton_8.clicked.connect(self.false1)
        self.pushButton_12.clicked.connect(self.backfrm)
        self.pushButton_13.clicked.connect(self.backfrm1)
        self.pushButton_11.clicked.connect(self.backfrm2)
        self.pushButton_101.clicked.connect(self.backfrm3)
        self.outsamyespb.clicked.connect(self.samfile)
        self.outsamnopb.clicked.connect(self.samnoshow)
        self.ranyespb.clicked.connect(self.samfile2)
        self.randnopb.clicked.connect(self.samnoshow)
        self.samoutspb.clicked.connect(self.samfile3)
        self.samoutnopb.clicked.connect(self.samnoshow)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.changeText)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText1)
        #self.connect(self.createind, SIGNAL('activated(QString)'), self.runindex1)
        #self.connect(self.selfilcom, SIGNAL('activated(QString)'), self.runindex)
        self.connect(self.samcmb, SIGNAL('activated(QString)'),self.frmshow)
        self.connect(self.comboBox_7,SIGNAL('activated(QString)'),self.moreop)
        self.connect(self.eftcmb, SIGNAL('activated(QString)'), self.efrtshow)
        self.connect(self.jbrscparcmb, SIGNAL('activated(QString)'),self.jblshow)
        #self.connect(self.verticalScrollBar,SIGNAL('activated(QString'),self.mouse)


    def jblshow(self): # adjusting location of some frame here
        tx = self.jbrscparcmb.currentText()
        tx1 = self.anal.currentText()
        if (tx=="Paired-end") and (tx1 == "2:Full parameter list"):
            self.framepair.show()
            self.Execute.setGeometry(QtCore.QRect(600, 1100, 75, 27))
        elif (tx=="Paired-end") and (tx1 == "1:Default settings only"):
            self.framepair.show()
            self.Execute.setGeometry(QtCore.QRect(600, 900, 75, 27))
        elif (tx=="Single-end") and (tx1 == "2:Full parameter list"):
            self.framepair1.show()
            self.framepair1.setGeometry(QtCore.QRect(10, 800, 751, 107))
            self.Execute.setGeometry(QtCore.QRect(600, 900, 75, 27))
            self.framepair.hide()
        else:
            self.framepair1.show()
            self.Execute.setGeometry(QtCore.QRect(600, 600, 75, 27))
            self.framepair.hide()

    def time(self): # command for time variable
        self.stri += " "+"-t"+" "

    def time1(self): # print nothing to stderr except serious errors
        self.stri += " "+"--quiet"+" "

    def Qseqop(self):#filter out reads that are bad according to QSEQ filter
        self.stri += " "+"--qc-filter"+" "

    def memo(self): # use memory-mapped I/O for index; many 'bowtie's can share
        self.stri += " "+"--mm "+" "

    def printop(self): #print version information and quit
        self.stri += " "+"--version"+" "

    def usage(self): #print this usage message
        self.stri += " "+"-h"+" "

    def time2(self): #send metrics to stderr (off)
        self.stri += " "+"--met-stderr"+" "

    def time3(self): #supppress header lines, i.e. lines starting with @
        self.stri += " "+"--no-head"+" "

    def time4(self):# supppress @SQ header lines
        self.stri += " "+"--no-sq"+" "

    def readfile1(self): # code for selecting single read fasta files
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.fastcmb.addItem(self.fl)
                self.readfl2 = self.fastcmb.currentText()

            else:
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.readfile1()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multifile1(self):# code for selecting muliple read fasta files
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.fastcm2.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.fastcm2.count()
                    self.file3 = self.fastcm2.itemText(0)
                    self.file1 = self.fastcm2.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.fastcm2.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3
                    self.multifile1()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2= " "
                    num1 = self.fastcm2.count()
                    self.file3 = self.fastcm2.itemText(0)
                    self.file1 = self.fastcm2.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.fastcm2.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3
                    print(self.readfl2)

            else:
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile1()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)


    def multifile2(self):# code for selecting muliple read fasta files for paired end
        self.fl= QtGui.QFileDialog.getOpenFileName()
        if self.fl:

            sta2 = ".fq"

            if sta2 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.fastcmb.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num = self.fastcmb.count()
                    self.file3 = self.fastcmb.itemText(0)
                    self.file1 = self.fastcmb.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.fastcmb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl1 = self.file3
                    self.multifile2()
                elif reply == QtGui.QMessageBox.No:
                    num = self.fastcmb.count()
                    self.file3 = self.fastcmb.itemText(0)
                    self.file1 = self.fastcmb.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.fastcmb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl1 = self.file3



            else:


                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile2()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)


    def readfile2(self):# code for selecting single read fasta files for paired end
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.fastcm2.addItem(self.fl)
                self.readfl2 = self.fastcm2.currentText()

            else:
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.readfile2()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def readfile21(self):# code for selecting single read fasta files for singleend
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.fastcm21.addItem(self.fl)
                self.read = self.fastcm21.currentText()
                self.read1 = "-U"+" "+self.read

            else:
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.readfile21()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multifile11(self):# code for selecting muliple read fasta files for single end
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.fastcm21.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.fastcm21.count()
                    self.file3 = self.fastcm21.itemText(0)
                    self.file1 = self.fastcm21.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.fastcm21.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.read = self.file3
                    self.multifile11()

                elif reply == QtGui.QMessageBox.No:
                    self.read = " "
                    num1 = self.fastcm21.count()
                    self.file3 = self.fastcm21.itemText(0)
                    self.file1 = self.fastcm21.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.fastcm21.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.read = self.file3
                    print(self.read)

            else:
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile11()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def frr(self): #-1, -2 mates align fw/rev, rev/fw, fw/fw (--fr)
        self.stri += " "+"--fr"+" "

    def rfr(self):# -1, -2 mates align fw/rev, rev/fw, fw/fw (--fr)
        self.stri += " "+"--rf"+" "

    def ffr(self):# -1, -2 mates align fw/rev, rev/fw, fw/fw (--fr)
        self.stri += " "+"--ff"+" "

    def cond(self):#suppress unpaired alignments for paired reads
        self.stri += " "+"--no-mixed"+" "

    def cond1(self): # suppress discordant alignments for paired reads
        self.stri += " "+"--no-discordant"+" "

    def cond2(self): # not concordant when mates extend past each other
        self.stri += " "+" --no-dovetail"+" "

    def cond3(self): #not concordant when one mate alignment contains other
        self.stri += " "+"--no-contain"+" "

    def cond4(self):# not concordant when mates overlap at all
        self.stri += " "+"--no-overlap"+" "

    def output(self): # code for showing output frame that contain output options
        self.outst = self.inpou1.currentText()
        if self.outst == "Yes":
            self.frame.hide()
            self.outputframe.show()
        else:
            self.frame.show()
            self.outputframe.hide()

    def okclick(self): # code for return back from output frame to frame
        self.frame.show()
        self.outputframe.hide()

    def pair(self): # code for setting locations for paired end option
        self.tf = self.paircmb.currentText()
        self.sth = self.anal.currentText()

        if self.tf == "No" and self.sth =="1:Default settings only":
            self.pairedgrp.hide()
            self.Execute.setGeometry(QtCore.QRect(600, 800, 75, 27))
        elif self.tf == "No" and self.sth =="2:Full parameter list":
            self.pairedgrp.hide()
            self.Execute.setGeometry(QtCore.QRect(600, 1100, 75, 27))
        elif self.tf == "Yes" and self.sth =="1:Default settings only":
            self.pairedgrp.show()
            self.Execute.setGeometry(QtCore.QRect(600, 1500, 75, 27))
        elif self.tf == "Yes" and self.sth =="2:Full parameter list":
            self.pairedgrp.show()
            self.Execute.setGeometry(QtCore.QRect(600, 1700, 75, 27))

    def samfile(self): #force SAM output order to match order of input reads
        self.stri +=" "+"--reorder"+" "

    def samfile2(self):# seed rand. gen. arbitrarily instead of using read attribute
        self.stri += " "+"--non-deterministic"+" "

    def samfile3(self): # code for setting sam output yes
        self.st = "yes"

    #  commands for default options

    def default2(self):
        self.stri = "-D"+" "+"5"+" "+"-R" +" "+"1"+" "+"-N"+" "+"0"+" "+"-L"+" "+"22"+" "+" -i S,0,2.50"

    def default3(self):
        self.stri = "-D"+" "+"10"+" "+"-R" +" "+"2"+" "+"-N"+" "+"0"+" "+"-L"+" "+"22"+" "+" -i S,0,2.50"

    def default4(self):
        self.stri = "-D"+" "+"15"+" "+"-R" +" "+"2"+" "+"-L"+" "+"22"+" "+" -i S,1,1.15"

    def default5(self):
        self.stri = "-D"+" "+"20"+" "+"-R" +" "+"3"+" "+"-N"+" "+"0"+" "+"-L"+" "+"20"+" "+" -i S,1,0.50"

    def default6(self):
        self.stri = "-D"+" "+"5"+" "+"-R" +" "+"1"+" "+"-N"+" "+"0"+" "+"-L"+" "+"25"+" "+" -i S,1,2.00"

    def default7(self):
        self.stri = "-D"+" "+"10"+" "+"-R" +" "+"2"+" "+"-N"+" "+"0"+" "+"-L"+" "+"22"+" "+" -i S,1,1.75"

    def default8(self):
        self.stri = "-D"+" "+"15"+" "+"-R" +" "+"2"+" "+"-N"+" "+"0"+" "+"-L"+" "+"20"+" "+" -i S,1,0.75"

    def default9(self):
        self.stri = "-D"+" "+"20"+" "+"-R" +" "+"3"+" "+"-N"+" "+"0"+" "+"-L"+" "+"20"+" "+" -i S,1,0.50"



    def msgshw(self): # code for reporting options
         text = self.comboBox_8.currentText()
         print(text)
         if (text == "Set -K option and -K value"):
                quit_msg = "if you want to Searches for at most that many distinct, valid alignments for each read?"
                reply = QtGui.QMessageBox.question(self, 'Message',
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    text = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),self.tr("Enter Value:"), QtGui.QLineEdit.Normal)
                    fil = text[0]
                    self.stri += " "+"-k"+fil
                else:
                    self.stri +=" "+"-k"+"1"
         else:
                self.stri +=" "+"-a"+"1"



    def samout(self): #
        self.stri +=" "+"--no-unal"+" "


    def samnoshow(self):
        self.stri += " "

    def seqgo(self):
        self.stri +=" "+"--omit-sec-seq"+" "

    def seqnogo(self):
        self.stri += " "

    def ph33(self):
        self.stri += " "+"--phred33"+" "

    def ph64(self):
        self.stri += " "+"--phred64"+" "

    def spconvert(self):
        self.stri += " "+"--solexa-quals"+" "

    def spno1(self):
        self.stri +=" "

    def ascino(self):
        self.stri +=" "

    def asciconvert(self):
        self.stri +=" "+"--int-quals"+" "

    def setrdb(self):
        if self.radioButton.isChecked():
            self.minmax.setText("L,-0.6,-0.6")
            self.stri +=" "+"--end-to-end"+" "

    def radiobutton2(self):
        if self.radioButton_2.isChecked():
            self.minmax.setText("G,20,8")
            self.stri +=" "+"--local"+" "

    # code for hiding current frame ang showing several other frames that contain effort, other and sam or bam options

    def nextshow(self):
        self.frame.hide()
        self.frame_3.show()

    def frmshow(self):
        self.frame.hide()
        self.frame_2.show()

    def default1(self):
        self.str1== "2:Full parameter list"

    def backfrm3(self):
        self.frame_2.hide()
        self.frame.show()

    def backfrm2(self):
        self.frame_3.hide()
        self.frame.show()

    def backfrm(self):
        self.scrfrm.hide()
        self.frame.show()

    def backfrm1(self):
        self.efrtfrm.hide()
        self.frame.show()

    def okclicked(self):
        self.yesgp.hide()
        self.yesgp.clearMask()
        self.frame.show()

    def executeclick(self):
        self.frame.show()
        self.more.hide()

    def showscr(self):
        self.frame.hide()
        self.scrfrm.show()

    def efrtshow(self):
        self.frame.hide()
        self.efrtfrm.show()

    def changeText(self, value):
        if value:
            self.z = value
            self.textEdit_2.setText(str(self.z))
        else:
            self.z = "22"
        #print(self.z)

    def true1(self):
        self.stri += " " +"--nofw"+" "

    def true2(self):
        self.stri += " " +"--norc"+" "

    def false1(self):
        self.stri = " "

    def prnt(self):
        print("aaa"+ str(self.file))


    def changeText1(self, value):
        if value:
            self.z1 = value
            self.textEdit.setText(str(self.z1))
        else:
            self.z1 = "0"

    def mouse(self):
        self.centralwidget.scroll(self,100,100,1)


    def runindex1(self): #code for seting built in index files or user defined files

        txt = self.createind.currentText()
        if txt == "Use a built-in genome index":
            self.builselcom.show()
            self.selfile.hide()
            self.selfilcom.hide()
            mypath = "/home/amrata/PycharmProjects/builinfil"
            onlyfiles = [f for f in tuple(listdir(mypath)) ]
            self.builselcom.addItems((onlyfiles))
            self.connect(self.builselcom, SIGNAL('activated(QString)'), self.load)
        elif txt == "Create a reference genome":
            self.selfile.show()
            self.selfilcom.show()
            self.builselcom.hide()
            #os.system('python tophat.py')


    def load(self): # code for showing builtin index files
         pfil = str(self.builselcom.currentText())
         self.pfl = pfil
         str2= "."
         str1 = pfil.find(str2)
         print(str1)
         file =  pfil[:str1]
         self.file = file
         print(file)
         proc = subprocess.Popen(["cp -r /home/amrata/PycharmProjects/builinfil/"+self.pfl+ "/* "+" "+"/home/amrata/PycharmProjects/bowtieuser" , ""],stdout=subprocess.PIPE, shell=True)
         (out, err) = proc.communicate()
         print(out)


    def runindex(self):
        file = self.selfilcom.currentText()
        self.connect(self.selfilcom,SIGNAL('activated(QString)'),self.filevent)
        #self.connect(self.selfilcom,SIGNAL('activated(QString)'),self.filevent1)

    def filevent(self):
            quit_msg = "if you want to Provide the File Name? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                text = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),self.tr("File Name:"), QtGui.QLineEdit.Normal)
                fil = text[0]

                fil1=globals()

                #label = QtGui.QLabel(self.scrollAreaWidgetContents_2)

               # quit_msg = "Please wait"
                #QtGui.QErrorMessage(quit_msg)
                #movie = QtGui.QMovie("/home/amrata/PycharmProjects/bowtieuser/images/Floatingrays.gif", QtCore.QByteArray(), self)
                #movie.setCacheMode(QtGui.QMovie.CacheAll)
                #movie.setSpeed(100)
                #self.label.setMovie(movie)
                #self.label.setGeometry(QtCore.QRect(500, 300, 721, 27))
                #movie.start()
                self.file = fil
                file = self.selfilcom.currentText()
                #imag = QtGui.QPixmap("")
                proc = subprocess.Popen(["bowtie2-build" + " "+ file + " "+ fil, ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()




                #self.selfilcom.addItems(str(out))/home/amrata/PycharmProjects/bowtieuser/images/Floatingrays.gif

    def onIndexChange(self): # code for adjusting location
                self.str1 = self.anal.currentText()
                if self.str1== "2:Full parameter list":
                    self.nowpres.hide()
                    self.framepair.hide()
                    self.defaulfram.hide()
                    self.pargp.show()
                    self.jobreslbl.setGeometry(QtCore.QRect(10, 730, 751, 17))
                    self.jbrscparcmb.setGeometry(QtCore.QRect(10, 750, 721, 27))
                    #self.frame_4.setGeometry(QtCore.QRect(10, 770, 721, 87))
                    self.framepair.setGeometry(QtCore.QRect(10, 800, 721, 1007))
                    self.pairedgrp.hide()
                    self.Execute.setGeometry(QtCore.QRect(600, 900, 75, 27))
                        #self.yesnext.show()
                       #self.parnext.hide()
                else:
                    self.pargp.hide()
                    self.nowpres.show()
                    self.defaulfram.show()
                    self.jobreslbl.setGeometry(QtCore.QRect(10, 450, 751, 17))
                    self.jbrscparcmb.setGeometry(QtCore.QRect(10, 470, 720, 27))
                    #self.frame_4.setGeometry(QtCore.QRect(10, 740, 720, 81))
                    self.framepair.setGeometry(QtCore.QRect(10, 510, 721, 1007))
                    self.pairedgrp.hide()
                    self.framepair.hide()
                    self.Execute.setGeometry(QtCore.QRect(600, 650, 75, 27))





    def moreop(self):# code   for showing more frame that containes alignment options
        str2 = self.comboBox_7.currentText()

        self.more.hide()
        if str2 == "Yes":
                        self.frame.hide()
                        self.more.show()
                        #self.yesnext1.setGeometry(QtCore.QRect(0, 1050, 951, 200))
        elif str2 == "No":
                        self.frame.show()
                        self.more.hide()
                        #self.yesnext1.setGeometry(QtCore.QRect(0, 70, 951, 200))

    def onIndexChange2(self): # code for showing yesgp it containes input options
                    str1 = self.inp.currentText()

                    if str1 == "Yes":
                        #self.yesnext.hide()
                        self.frame.hide()
                        self.yesgp.show()
                        #self.yesnext.show()
                        #self.yesnext.setGeometry(QtCore.QRect(10, 480, 951, 1200))
                        #self.yesnext1.setGeometry(QtCore.QRect(0, 100, 951, 200))
                    elif str1 == "No":
                        self.frame.show()
                        self.yesgp.hide()
                        #self.yesnext.show()
                        #self.yesnext.setGeometry(QtCore.QRect(10, 60, 951, 1200))
                        #self.yesnext1.setGeometry(QtCore.QRect(0, 90, 951, 200))


    def onIndexChange1(self): #code for setting either user specified value or default value for each parameter and execute those parms
                    #str1 = self.inp.currentText()
                    #print(str1)
                    #if str1 == "Yes":
                        #self.yesnext.hide()
                       # self.yesgp.show()
                self.str1 = self.anal.currentText()
                mit = self.mint.text()
                maxt = self.maxtx.text()
                if mit:
                    self.stri += " "+"-I"+" "+mit
                    self.stri1=self.stri
                else:
                    self.stri +=" "+"-I"+" "+"0"
                    self.stri1 = self.stri
                if maxt:
                    self.stri += " "+"-X"+" "+maxt
                    self.stri1=self.stri
                else:
                    self.stri +=" "+"-X"+" "+"500"
                    self.stri1 = self.stri


                if self.str1== "2:Full parameter list":
                        length=self.textEdit_2.toPlainText()

                        algn = self.textEdit.toPlainText()
                        #self.parnext.show()
                        interval = self.lineEdit.text()
                        skip = self.skip.toPlainText()
                        u = self.uskip.toPlainText()
                        trm5 = self.trimlft.toPlainText()
                        trm3 = self.trimrgt.toPlainText()
                        dpad = self.lineEdit_3.text()
                        gbar = self.lineEdit_4.text()
                        amb = self.lineEdit_2.text()
                        scrmin = self.minmax.text()
                        ma =self.lineEdit_6.text()
                        mp = self.lineEdit_7.text()
                        np = self.lineEdit_8.text()
                        rgbop = self.lineEdit_9.text()
                        rgbex = self.lineEdit_10.text()
                        rfgop = self.lineEdit_11.text()
                        rfgex = self.lineEdit_12.text()
                        seedex = self.lineEdit_14.text()
                        reseed = self.lineEdit_15.text()
                        seed =self.lineEdit_16.text()
                        un = self.lineEdita.text()
                        al = self.lineEdit_3a.text()
                        uncon = self.lineEdit_4a.text()
                        alconc = self.lineEdit_5a.text()
                        met = self.lineEdit_7a.text()
                        metin = self.lineEdit_9a.text()
                        rgid =self.lineEdit_15a.text()
                        rgtxt =self.lineEdit_16a.text()
                        over = self.overrtxt.text()
                        thrd = self.thrdtxt.text()
                        if over:
                            self.stri += " "+"-o"+" "+"~"+un
                            self.stri1=self.stri
                        if thrd:
                            self.stri += " "+"-p"+" "+"~"+un
                            self.stri1=self.stri

                        if un:
                            self.stri += " "+"--un"+" "+"~"+un
                            self.stri1=self.stri
                        if al:
                            self.stri += " "+"--al"+" "+"~"+al
                            self.stri1=self.stri
                        if uncon:
                            self.stri += " "+"--un-conc"+" "+"~"+uncon
                            self.stri1=self.stri
                        if alconc:
                            self.stri += " "+"--al-conc"+" "+"~"+alconc
                            self.stri1=self.stri
                        if met:
                            self.stri += " "+"--met-file"+" "+"~"+met
                            self.stri1=self.stri
                        if metin:
                            self.stri += " "+"--met"+" "+metin
                            self.stri1=self.stri
                        if rgid:
                            self.stri += " "+"--rg-id"+" "+rgid
                            self.stri1=self.stri
                        if rgtxt:
                            self.stri += " "+" --rg"+" "+rgtxt
                            self.stri1=self.stri


                        #self.stri += " "
                        if skip:
                            self.stri += " "+"-s"+" "+skip
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"-s"+" "+"0"
                            self.stri1 = self.stri
                        if u:
                            self.stri += " "+"-u"+" "+u
                            self.stri1=self.stri
                        else:
                            self.stri +=" "+"-u"+" "+"100000000"
                            self.stri1 = self.stri
                        if trm5:
                            self.stri += " "+"--trim5"+" "+trm5
                            self.stri1=self.stri
                        else:
                            self.stri +=" "+"--trim5"+" "+"0"
                            self.stri1 = self.stri
                        if trm3:
                            self.stri += " "+"--trim3"+" "+trm3
                            self.stri1=self.stri
                        else:
                            self.stri +=" "+"--trim3"+" "+"0"
                            self.stri1 = self.stri


                        if interval:
                            self.stri += " "+"-i"+" "+interval
                            self.stri1=self.stri
                        else:
                            self.stri +=" "+"-i"+" "+"S,1,1.15"
                            self.stri1 = self.stri
                        if length:
                            self.stri +=" "+"-L"+" "+length
                            self.stri1=self.stri
                        else:

                            self.stri +=" "+"-L"+" "+"22"
                            self.stri1 = self.stri
                        if algn:
                            self.stri +=" "+"-N"+" "+algn
                            self.stri1=self.stri
                        else:
                            self.stri =" "+"-N"+" "+"0"
                            self.stri1 = self.stri
                        if dpad:
                            self.stri += " "+"--dpad"+" " +dpad
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--dpad"+" "+"15"
                            self.stri1 = self.stri
                        if gbar:
                            self.stri += " "+"--gbar"+" " +gbar
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--gbar"+" "+"4"
                            self.stri1 = self.stri
                        if amb:
                            self.stri += " "+"--n-ceil"+" "+amb
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--n-ceil"+" "+"L,0,0.15"
                            self.stri1 = self.stri
                        if scrmin:
                            self.stri += " "+"--score-min"+" "+scrmin
                            self.stri1 = self.stri
                        if ma:
                            self.stri += " "+"--ma"+" "+ma
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--ma"+" "+"2"
                            self.stri1 = self.stri
                        if mp:
                            self.stri += " "+"--mp"+" "+mp
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--mp"+" "+"6,2"
                            self.stri1 = self.stri
                        if np:
                            self.stri += " "+"--np"+" "+np
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--np"+" "+"1"
                            self.stri1 = self.stri
                        if rgbop:
                            self.stri += " "+"--rdg"+" "+rgbop
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--rdg"+" "+"5"
                            self.stri1 = self.stri
                        if rgbex:
                            self.stri += " "+"--rdg"+" "+rgbex
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--rdg"+" "+"3"
                            self.stri1 = self.stri
                        if rfgop:
                            self.stri += " "+"--rfg"+" "+rfgop
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--rfg"+" "+"5"
                            self.stri1 = self.stri
                        if rfgex:
                            self.stri += " "+"--rfg"+" "+rfgex
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--rfg"+" "+"3"
                            self.stri1 = self.stri
                        if seedex:
                            self.stri += " "+"-D"+" "+seedex
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"-D"+" "+"15"
                            self.stri1 = self.stri
                        if reseed:
                            self.stri += " "+"-R"+" "+reseed
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"-R"+" "+"2"
                            self.stri1 = self.stri
                        if seed:
                            self.stri += " "+"--seed"+" "+seed
                            self.stri1 = self.stri
                        else:
                            self.stri += " "+"--seed"+" "+"0"
                            self.stri1 = self.stri

                            print(self.stri1)

                        self.opt = self.jbrscparcmb.currentText()
                        if self.opt=="Single-end": # for single end
                            if not self.read == " ":

                                quit_msg1 = "if you want to Provide the Output File Name? (Press Yes if you want)"
                                reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                    quit_msg1, QtGui.QMessageBox.Yes,
                                                                    QtGui.QMessageBox.No)

                                if reply3 == QtGui.QMessageBox.Yes:
                                    text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                       self.tr("File Name:"), QtGui.QLineEdit.Normal)
                                    out1 = text3[0]
                                    self.out1 = out1
                                elif reply3 == QtGui.QMessageBox.No:
                                    quit_msg1 = "you have not specified any output file,Please Provide the Output File Name"
                                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                        quit_msg1, QtGui.QMessageBox.Ok)
                                    text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                       self.tr("File Name:"), QtGui.QLineEdit.Normal)
                                    out1 = text3[0]
                                    self.out1 = out1

                                if self.st == "yes": # for sam output
                                    output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read1 + " " + "-S" + " " + self.out1
                                    fpt1 = open("bowtieout.pkl", "wb")
                                    pickle.dump(str(output), fpt1, protocol=2)
                                    fpt1.close()
                                    print(output)

                                else: # output doent in sam format
                                    output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read1 + "  " + self.out1
                                    fpt1 = open("bowtieout.pkl", "wb")
                                    pickle.dump(str(output), fpt1, protocol=2)
                                    fpt1.close()
                                    # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                    # (out, err) = proc.communicate()
                                cfil1 = self.out1
                                fp1 = open("sharedcufffile.pkl", "wb")
                                pickle.dump(str(cfil1), fp1, protocol=2)
                                fp1.close()


                            elif self.read == " ": # check whether read is empty or not
                                quit_msg = "You have not selected any read files Please provide the read files "
                                reply = QtGui.QMessageBox.question(self, 'Message',
                                        quit_msg, QtGui.QMessageBox.Ok)


                        elif self.opt == "Paired-end": # paired end

                            if self.readfl1 ==" " and  self.readfl2== " ":# check whether read is empty or not
                                quit_msg = "Please select the Read File "
                                reply = QtGui.QMessageBox.warning(self, 'warning',
                                                                  quit_msg, QtGui.QMessageBox.Ok)
                            else:
                                self.read = "-1" + self.readfl1 + " " + "-2" + self.readfl2


                                quit_msg1 = "if you want to Provide the Output File Name? (Press Yes if you want)"
                                reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                        quit_msg1, QtGui.QMessageBox.Yes,
                                                                        QtGui.QMessageBox.No)

                                if reply3 == QtGui.QMessageBox.Yes:
                                        text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                           self.tr("File Name:"),
                                                                           QtGui.QLineEdit.Normal)
                                        out1 = text3[0]
                                        self.out1 = out1
                                elif reply3 == QtGui.QMessageBox.No:
                                    quit_msg1 = "you have not specified any output file,Please Provide the Output File Name"
                                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                        quit_msg1, QtGui.QMessageBox.Ok)
                                    text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                       self.tr("File Name:"), QtGui.QLineEdit.Normal)
                                    out1 = text3[0]
                                    self.out1 = out1
                                if self.st == "yes": # output is in the sam format
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read + " " + "-S" + " " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        print(output)

                                        # proc = subprocess.Popen(["bowtie" +" "+ "-v2"+" "+"-s"+ skip +" "+"-u" +u+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+"-S"+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                else: # output is not in the sam format
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read + "  " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                cfil1 = self.out1 # for store this output file for future use
                                fp1 = open("sharedcufffile.pkl", "wb")
                                pickle.dump(str(cfil1), fp1, protocol=2)
                                fp1.close()

                        #if not self.buildfile == " " and not self.read == " " and not self.out1 == " ":

                        if self.nofil == "No": # code if we mot continue cufflink module when we want bowtie output olny
                                 fptt1 = open("bowtieout.pkl","rb")
                                 self.bowtie = pickle.load(fptt1)
                                 fptt1.close()
                                 quit_msg = "Processing Please wait"
                                 reply = QtGui.QMessageBox.question(self, 'Message',quit_msg, QtGui.QMessageBox.Default)
                                 proc = subprocess.Popen([self.buildfile, ""],stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                                 (out, err) = proc.communicate()

                                 f = open("error1", "w")
                                 f.write(str(err))
                                 f.close()
                                 f = open("error1", "r")
                                 self.txt = f.read(5)
                                 self.txt1 = f.read(10)
                                 f.close()
                                 if not self.txt1: # checking for error
                                     quit_msg = "Successfully created"
                                     reply = QtGui.QMessageBox.information(self, 'Message',
                                                                           quit_msg, QtGui.QMessageBox.Ok)


                                     proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                                     (out, err) = proc.communicate()

                                     self.file1 = self.out1 + ".sam"

                                     proc = subprocess.Popen(["sort -k 3,3 -k 4,4n " + " " + self.out1 + " >" + self.file1, ""],
                                         stdout=subprocess.PIPE, shell=True)
                                     (out, err) = proc.communicate()

                                     if self.botout == "yes": # open output file if we need
                                         proc = subprocess.Popen(["gedit" + " " + self.file1, ""],
                                                                 stdout=subprocess.PIPE, shell=True)
                                         (out, err) = proc.communicate()


                                 elif self.txt1: # if error is there
                                     quit_msg = "is not a valid reference file"
                                     reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Ok)
                                     self.txt = " "
                                     self.txt1 = " "



                        else:


                                #if self.cont =="yes" and not self.read== " ":
                                self.top = cuff.Cuffl(self)
                                self.top.closed.connect(self.show)
                                self.top.show()

                                #elif self.cont == "no":



                elif self.str1== "1:Default settings only": # for default settings same thing as there in the full parameter list
                        self.opt = self.jbrscparcmb.currentText()
                        print(self.opt)

                        if self.opt == "Single-end":
                                if not self.read == " ":

                                    quit_msg1 = "if you want to Provide the Output File Name? (Press Yes if you want)"
                                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                        quit_msg1, QtGui.QMessageBox.Yes,
                                                                        QtGui.QMessageBox.No)

                                    if reply3 == QtGui.QMessageBox.Yes:
                                        text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                           self.tr("File Name:"),
                                                                           QtGui.QLineEdit.Normal)
                                        out1 = text3[0]
                                        self.out1 = out1
                                    elif reply3 == QtGui.QMessageBox.No:
                                        quit_msg1 = "you have not specified any output file,Please Provide the Output File Name"
                                        reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                            quit_msg1, QtGui.QMessageBox.Ok)
                                        text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                           self.tr("File Name:"),
                                                                           QtGui.QLineEdit.Normal)
                                        out1 = text3[0]
                                        self.out1 = out1
                                    if self.st == "yes":
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read1 + " " + "-S" + " " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        print(output)

                                        # proc = subprocess.Popen(["bowtie" +" "+ "-v2"+" "+"-s"+ skip +" "+"-u" +u+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+"-S"+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                    else:
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read1 + "  " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                    cfil1 = self.out1
                                    fp1 = open("sharedcufffile.pkl", "wb")
                                    pickle.dump(str(cfil1), fp1, protocol=2)
                                    fp1.close()


                                elif self.read == " ":
                                    quit_msg = "You have not selected any read files Do you want to select the read files "
                                    reply = QtGui.QMessageBox.question(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Yes,
                                                                       QtGui.QMessageBox.No)
                                    if reply == QtGui.QMessageBox.Yes:
                                        self.readfile21()
                                        quit_msg1 = "if you want to Provide the Output File Name? (Press Yes if you want)"
                                        reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                            quit_msg1, QtGui.QMessageBox.Yes,
                                                                            QtGui.QMessageBox.No)

                                        if reply3 == QtGui.QMessageBox.Yes:
                                            text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                               self.tr("File Name:"),
                                                                               QtGui.QLineEdit.Normal)
                                            out1 = text3[0]
                                            self.out1 = out1
                                        elif reply3 == QtGui.QMessageBox.No:
                                            quit_msg1 = "you have not specified any output file,Please Provide the Output File Name"
                                            reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                                quit_msg1, QtGui.QMessageBox.Ok)
                                            text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                               self.tr("File Name:"),
                                                                               QtGui.QLineEdit.Normal)
                                            out1 = text3[0]
                                            self.out1 = out1
                                    else:
                                        quit_msg = "Do you want to Quit from this "
                                        reply = QtGui.QMessageBox.question(self, 'Message',
                                                                           quit_msg, QtGui.QMessageBox.Yes,
                                                                           QtGui.QMessageBox.No)
                                        if reply == QtGui.QMessageBox.Yes:
                                            self.close()

                        elif self.opt == "Paired-end":

                                if self.readfl1 == " " and self.readfl2 == " ":
                                    quit_msg = "Please select the Read File "
                                    reply = QtGui.QMessageBox.warning(self, 'warning',
                                                                      quit_msg, QtGui.QMessageBox.Ok)
                                else:
                                    self.read = "-1" + self.readfl1 + " " + "-2" + self.readfl2

                                    quit_msg1 = "if you want to Provide the Output File Name? (Press Yes if you want)"
                                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                                                                        quit_msg1, QtGui.QMessageBox.Yes,
                                                                        QtGui.QMessageBox.No)

                                    if reply3 == QtGui.QMessageBox.Yes:
                                        text3 = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),
                                                                           self.tr("File Name:"),
                                                                           QtGui.QLineEdit.Normal)
                                        out1 = text3[0]
                                        self.out1 = out1
                                    if self.st == "yes":
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read + " " + "-S" + " " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        print(output)

                                        # proc = subprocess.Popen(["bowtie" +" "+ "-v2"+" "+"-s"+ skip +" "+"-u" +u+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+"-S"+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                    else:
                                        output = "bowtie2" + " " + self.stri1 + " " + self.file + " " + self.read + "  " + out1
                                        fpt1 = open("bowtieout.pkl", "wb")
                                        pickle.dump(str(output), fpt1, protocol=2)
                                        fpt1.close()
                                        # proc = subprocess.Popen(["bowtie2" +" "+ self.stri1+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                        # (out, err) = proc.communicate()
                                    cfil1 = self.out1
                                    fp1 = open("sharedcufffile.pkl", "wb")
                                    pickle.dump(str(cfil1), fp1, protocol=2)
                                    fp1.close()




                                    #proc = subprocess.Popen(["bowtie" +" "+ "-v2"+" "+"-s"+ skip +" "+"-u" +u+" "+self.file+" " + read+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                               # proc = subprocess.Popen(["bowtie2" +" "+ self.stri+" "+self.file+" " + read+" "+"-S"+" "+ out1 , ""],stdout=subprocess.PIPE, shell=True)
                                #(out, err) = proc.communicate()

                        if self.nofil == "No":
                                    fptt1 = open("bowtieout.pkl","rb")
                                    self.bowtie = pickle.load(fptt1)
                                    fptt1.close()
                                # print(self.bowtie)
                                    quit_msg = "Processing Please wait"
                                    reply = QtGui.QMessageBox.question(self, 'Message',
                                    quit_msg, QtGui.QMessageBox.Ok)
                                    proc = subprocess.Popen([self.buildfile, ""],stdout=subprocess.PIPE, shell=True)
                                    (out, err) = proc.communicate()
                                    f = open("error1", "w")
                                    f.write(str(err))
                                    f.close()
                                    f = open("error1", "r")
                                    self.txt = f.read(5)
                                    self.txt1 = f.read(10)
                                    f.close()

                                    print(proc)

                                    if not self.txt1:
                                        proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                                        (out, err) = proc.communicate()
                                        self.file1 = self.out1 + ".sam"
                                        proc = subprocess.Popen(
                                            ["sort -k 3,3 -k 4,4n " + " " + self.out1 + " >" + self.file1, ""],
                                            stdout=subprocess.PIPE, shell=True)
                                        (out, err) = proc.communicate()
                                        quit_msg = "Successfully created"
                                        reply = QtGui.QMessageBox.information(self, 'Message',
                                                                              quit_msg, QtGui.QMessageBox.Ok)

                                        if self.botout == "yes":
                                            proc = subprocess.Popen(["gedit" + " " + self.file1, ""],
                                                                    stdout=subprocess.PIPE, shell=True)
                                            (out, err) = proc.communicate()




                                    elif self.txt1:
                                         quit_msg = "is not a valid reference file"
                                         reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Ok)
                                         self.txt = " "
                                         self.txt1 = " "

                        else:

                    # if self.cont =="yes" and not self.read:
                                self.top = cuff.Cuffl(self)
                                self.top.closed.connect(self.show)
                                self.top.show()











def main():
	app=QtGui.QApplication(sys.argv)
	form=Bowt()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


