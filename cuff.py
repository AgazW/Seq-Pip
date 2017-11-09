from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import cufflinksgui
import subprocess
import allignment
import pickle

#import images
from subprocess import call
import os
import cuff
import cuffquant
import bowt
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge
from subprocess import Popen, PIPE



class Cuffl(QtGui.QMainWindow,cufflinksgui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None): # code for initialization
        super(Cuffl, self).__init__( parent)
        self.setupUi(self)
        fp1 = open("sharedcufffile.pkl","rb") # containes reference genome file name
        self.file = pickle.load(fp1)
        fpt1 = open("build.pkl","rb") # containes bowtie-build command  along with file
        self.buildfile = pickle.load(fpt1)
        fptt1 = open("bowtieout.pkl","rb") # containes  output of bowtie
        self.bowtie = pickle.load(fptt1)
        #fptr = open("bowtieout.pkl","rb")
        #self.bowtout = pickle.load(fptr)
        fptr1 = open("botout.pkl","rb") # containes whether we want to see the output of bowtie or not
        self.botout = pickle.load(fptr1)
        fi = open("file.pkl","rb") # this containe which module we used for alignmnet either bowtie or tophat
        self.fil= pickle.load(fi)
        fi.close()
        fi1 = open("filegen.pkl","rb") # this containes either we continue from staring from creating index file or we directly start from specified module
        self.filg= pickle.load(fi1)
        fi1.close()
        print(self.filg)

        self.strin=" "
        self.bias = " "
        self.gtfile1= " "
        self.maskfil= " "
        self.progressbar.hide()


        self.parent = parent
        self.groupBox_4.hide()
        self.refgrp.hide()
       # self.framesh.hide()
       # self.groupBox_2.hide()
        self.groupBox.hide()
        self.msk = " "
      #  self.groupBox_31.hide()
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.connect(self.refannotcmb, SIGNAL('activated(QString)'), self.onIndexChange)
        #self.connect(self.biascmb, SIGNAL('activated(QString)'), self.onIndexChange2)
        #self.connect(self.seqcmb, SIGNAL('activated(QString)'), self.showscr)
        self.connect(self.advcufoptcmb, SIGNAL('activated(QString)'), self.nextshow)
        #self.lcd = QtGui.QLCDNumber(self)
        #self.sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        #vbox = QtGui.QVBoxLayout()
        #vbox.addWidget(self.lcd)
        #vbox.addWidget(self.sld)

        #self.setLayout(vbox)
        #self.sld.valueChanged.connect(self.lcd.display)

        #self.setGeometry(300, 300, 250, 150)
        #self.setWindowTitle('Signal & slot')

        #self.show()

        self.subrefanpusk.clicked.connect(self.selectFile)
        #self.biaspus.clicked.connect(self.biasop)
        self.subrefanpusk1.clicked.connect(self.selectF)
        self.maskpush.clicked.connect(self.selectFl)
        self.maskmulfile2.clicked.connect(self.multifile1)
        self.biaspus.clicked.connect(self.selectFl1)
        self.biasmulfile3.clicked.connect(self.multifile)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.changeText)
        QtCore.QObject.connect(self.maxfracsld, QtCore.SIGNAL('valueChanged(int)'), self.changeText6)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText1)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL('valueChanged(int)'), self.changeText2)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL('valueChanged(int)'), self.changeText3)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL('valueChanged(int)'), self.changeText4)
        QtCore.QObject.connect(self.horizontalSlider_6, QtCore.SIGNAL('valueChanged(int)'), self.changeText5)
        QtCore.QObject.connect(self.maxfracsld, QtCore.SIGNAL('valueChanged(int)'), self.maxop)

        self.connect(self.subrefancmb, SIGNAL('activated(QString)'), self.runindex)
        self.connect(self.subrefcomb, SIGNAL('activated(QString)'), self.runindex)
        #self.connect(self.maskcmb, SIGNAL('activated(QString)'), self.runindex1)


        self.connect(self.comboBox, SIGNAL('activated(QString)'), self.rnashow)
        self.connect(self.tilingtxt, SIGNAL('activated(QString)'), self.tiling)
        self.connect(self.multireadcmb, SIGNAL('activated(QString)'), self.multiread)
        self.connect(self.lengthcorcmb, SIGNAL('activated(QString)'), self.lengthc)

        self.connect(self.libinpcmb, SIGNAL('activated(QString)'), self.libfun)
        self.strin = " "+"--library-type"+" "+"fr-unstranded"
        self.execute.clicked.connect(self.executeop)


        self.ok.clicked.connect(self.okclicked)

    def increaseValue(self):

        self.setValue(self.value)
        self.value = self.value+1

    def tiling(self): #disable tiling by faux reads
        self.st=self.tilingtxt.currentText()
        if self.st=="Yes":
            self.strin += " "+"--no-faux-reads"+" "+" "+"True"
        else:
            self.strin +=" "+"--no-faux-reads"+" "+" "+"False"

    def libfun(self): #library prep used for input reads
        self.std = self.libinpcmb.currentText()
        if self.std:
            self.strin += " "+"--library-type"+" "+self.std
        else:
            self.strin += " "+"--library-type"+" "+"fr-unstranded"

    def runindex(self): # selecting GTF file
        self.gtfile = self.subrefancmb.currentText()
        self.gtf= self.subrefcomb.currentText()
        if self.gtfile:
            self.gtfile1 = " "+"-G"+" "+self.gtfile
        elif self.gtf:
            self.gtfile1 = " "+"-G"+" "+self.gtf



    def maxop(self, value): # code for setting value for horizontal slider corresponding value will be occure on text box
        #maximum fraction of allowed multireads per transcript
        if value:
            self.z1 = float(value) / 10000
            self.fracavgtxt.setText(str(self.z1))
        else:
            self.z1 = "0.75"









    def lengthc(self): # code for length correction
        self.stc=self.lengthcorcmb.currentText()
        if self.stc == "Standard alength Correction":
            self.strin += " "+"--no-effective-length-correction"+" "+"True"
        else:
            self.strin += " "+"--no-effective-length-correction"+" "+"False"

        if self.stc== "No Length Correction at all (use raw counts)":
            self.strin += " "+"--no-length-correction"+" "+"True"
        else:
            self.strin += " "+"--no-length-correction"+" "+"False"

    def selectFile(self):
        self.subrefancmb.addItem(QtGui.QFileDialog.getOpenFileName())


    def selectF(self):
        self.subrefcomb.addItem(QtGui.QFileDialog.getOpenFileName())

    def selectFl(self): # code for selecting mask file

        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"
            st1 = ".gff"

            if sta1 in self.fl or st1 in self.file:
                self.maskcmb.addItem(self.fl)
                self.readfl2 = self.maskcmb.currentText()
                self.msk = " "+"-M"+" "+self.readfl2

            else:
                quit_msg = "Error! Please select proper mask file(I.e file in the form of (gtf/gff)"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.selectFl()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def selectFl1(self): # code for selecting reference annotation for bias corection

        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fa"


            if sta1 in self.fl:
                self.biastxtcor.addItem(self.fl)
                self.readfl2 = self.biastxtcor.currentText()
                self.strin +=" "+"-b"+" "+self.readfl2

            else:
                quit_msg = "Error! Please select proper genome file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.selectFl1()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)



    def multiread(self): # code for multi reads
        self.st= self.multireadcmb.currentText()
        if self.st=="Yes":
            self.strin +=" "+"-u"+" "+"True"
        else:
            self.strin +=" "+"-u"+" "+"False"

    def rnashow(self): #code for hits
        self.st = self.comboBox.currentText()
        if self.st =="Yes":

            self.strin += " " +"--compatible-hits-norm"+" "+"True"
        else:
            self.strin += " " +"--compatible-hits-norm"+" "+"False"

    def changeText1(self, value): # code for setting value for horizontal slider corresponding value will be occure on text box code for max intron length
        if value:
            self.z = value
            self.maxintrontxt.setText(str(self.z))
        else:
            self.z = "300000"

    def changeText5(self, value): # code for setting value for horizontal slider corresponding value will be occure on text box for minimum fragments
        if value:
            self.z1 = float(value)/10000
            self.fracavgtxt.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def changeText6(self,
                    value):  # code for setting value for horizontal slider corresponding value will be occure on text box for minimum fragments
        if value:
            self.z1 = float(value) / 10000
            self.muitxt.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def changeText(self, value): # code for setting value for horizontal slider corresponding value will be occure on text box for minimum isoforms
        if value:
            self.z1 = float(value)/10000
            self.minisoformtxt.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def changeText3(self, value): # code for setting value for horizontal slider corresponding value will be occure on text box for alpha for junction binomial test filter
        if value:
            self.z1 = float(value)/10000
            self.alphatxt.setText(str(self.z1))
        else:
            self.z1 = "0.001"

    def changeText4(self, value): #percent read overhang taken as 'suspiciously small'
        if value:
            self.z1 = float(value)/10000
            self.percenttxt.setText(str(self.z1))
        else:
            self.z1 = "0.09"




    def changeText2(self, value):#suppress intra-intronic transcripts below this level
        if value:
            self.z11 = float(value)/10000
            self.mrnatxt.setText(str(self.z11))
        else:
            self.z11 = "0.15"

    def onIndexChange(self): # code for showing or hiding refeence annotation options
                self.str1 = self.refannotcmb.currentText()
                #self.groupBox_2.hide()

                if self.str1 == "No":

                    self.refgrp.hide()
                    self.groupBox.hide()

                    self.frame2.setGeometry(QtCore.QRect(10, 310, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 750, 75, 27))

                        #self.yesnext.show()
                       #self.parnext.hide()
                elif self.str1 == "Use reference annotation":

                    self.refgrp.show()
                    self.groupBox.hide()

                    self.frame2.setGeometry(QtCore.QRect(10, 450, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 880, 75, 27))
                elif self.str1 == "Use reference annotation as guide":

                    self.refgrp.hide()
                    self.groupBox.show()

                    self.frame2.setGeometry(QtCore.QRect(10, 590, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 1020, 75, 27))

    def onIndexChange2(self):
                self.str1 = self.biascmb.currentText()


                if self.str1 == "Yes":

                     self.framesh.show()
                    # self.execute.setGeometry(QtCore.QRect(600, 1000, 75, 27))

                elif self.str1 == "No":
                     self.framesh.hide()
                     #self.execute.setGeometry(QtCore.QRect(600, 950, 75, 27))


    def showscr(self):
                self.str2 = self.seqcmb.currentText()
                if self.str2 == "Locally cached":
                    self.groupBox_31.hide()
                    self.groupBox_3.show()
                elif self.str2 == "History":
                    self.groupBox_3.hide()
                    self.groupBox_31.show()

    def nextshow(self):
        self.sd = self.advcufoptcmb.currentText()
        if self.sd== "Yes":
            self.frame.hide()
            self.groupBox_4.show()


    def okclicked(self):
        self.groupBox_4.hide()
        self.frame.show()



    def multifile(self): # code for selecting multi annotation files
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".fa"

            if sta1 in self.fl:
                quit_msg = "Do you want to select any other reference file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.biastxtcor.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.biastxtcor.count()
                    self.file3 = self.biastxtcor.itemText(0)
                    self.file1 = self.biastxtcor.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.biastxtcor.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.strin += " " + "-b" + " " + self.file3
                    self.multifile()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.biastxtcor.count()
                    self.file3 = self.biastxtcor.itemText(0)
                    self.file1 = self.biastxtcor.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.biastxtcor.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.strin += " " + "-b" + " " + self.file3


            else:
                quit_msg = "Error! Please select genome file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multifile1(self): # multi GTF files
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".gtf"
            st1 = ".gff"

            if sta1 in self.fl or st1 in self.fl:
                quit_msg = "Do you want to select any other Mask file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.maskcmb.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.maskcmb.count()
                    self.file3 = self.maskcmb.itemText(0)
                    self.file1 = self.maskcmb.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.maskcmb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.msk= " "+"-M"+" "+ self.file3
                    self.multifile1()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.maskcmb.count()
                    self.file3 = self.maskcmb.itemText(0)
                    self.file1 = self.maskcmb.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.maskcmb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.msk +=" "+"-M"+" "+ self.file3


            else:
                quit_msg = "Error! Please select Proper Mask file(I,e file in the form of(gtf/gff)"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile1()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)



    def executeop(self): # code for executing cufflink modules here recieving and setting value for all the parameters
        quit_msg1 = "Processing Please Wait Some Minutes"
        reply3 = QtGui.QMessageBox.information(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Ok)
        intr = self.maxintrontxt.text()
        iso = self.minisoformtxt.text()
        mrn = self.mrnatxt.text()
        prm = self.ovrtoltxt.text()
        introvr = self.introvtoltxt.text()
        inrmn = self.inrmindisttxt.text()
        instdev = self.intdiststddevtxt.text()
        maxmle = self.maxmletxt.text()
        alp = self.alphatxt.text()
        per = self.percenttxt.text()
        intronover = self.intronovertxt.text()
        maxgen = self.maxgnbuntxt.text()
        maxnum = self.maxnumtxt.text()
        minintr = self.minintsiztxt.text()
        minavg = self.minavgtxt.text()
        fracavg = self.fracavgtxt.text()
        outd = self.outdirtxt.text()
        thrd = self.thrdtxt.text()
        seed = self.seedtxt.text()
        avg = self.avgfrtxt.text()
        frg = self.fragstdtxt.text()
        gen = self.gensamtxt.text()
        num = self.numfrantxt.text()
        maxn= self.maxtxts.text()
        norm = self.normalitxt.text()
        idt = self.idtxt.text()
        tran = self.trantxt.text()
        mul = self.muitxt.text()
        gsp = self.gaptxt.text()
        if not self.msk == " ":
            self.strin += " "+self.msk
            self.stri1 = self.strin
        if gsp:
            self.strin += " " + "  --overlap-radius " + " " + gsp + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "--overlap-radius" + " " + "50" + " "
            self.stri1 = self.strin
        if mul:
            self.strin += " " + "  --max-multiread-fraction " + " " + mul + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "  --max-multiread-fraction " + " " + "1" + " "
            self.stri1 = self.strin
        if idt:
            self.strin += " " + "  -L" + " " + idt + " "
            self.stri1 = self.strin
        if tran:
            self.strin += " " + "  --min-frags-per-transfrag " + " " + tran + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "  --min-frags-per-transfrag " + " "+"10"+" "
            self.stri1 = self.strin
        if norm:
            self.strin += " " + "  -N" + " " + norm + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "  -N" + " "
            self.stri1 = self.strin

        if maxn:
            self.strin += " " + "  --max-frag-multihits" + " " + maxn + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "  --max-frag-multihits" + " "+"1"
            self.stri1 = self.strin

        if num:
            self.strin += " " + " --num-frag-assign-draws" + " " + num + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + " --num-frag-assign-draws" + " " + "50" + " "
            self.stri1 = self.strin

        if gen:
            self.strin += " " + "--num-frag-count-draws" + " " + gen + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "--num-frag-count-draws" + " " + "100" + " "
            self.stri1 = self.strin

        if frg:
            self.strin += " " + "-s" + " " + frg + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "-s" + " " + "80" + " "
            self.stri1 = self.strin
        if avg:
            self.strin += " " + "-m" + " " + avg + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "-m" + " " + "200" + " "
            self.stri1 = self.strin
        if seed:
            self.strin += " " + "--seed " + " " +seed + " "
            self.stri1 = self.strin
        else:
            self.strin += " " + "--seed" + " " + "0" + " "
            self.stri1 = self.strin
        if thrd:
            self.strin += " " + "-p" + " " + thrd + " "
            self.stri1 = self.strin
        if outd:
            self.strin += " " + "-o" + " " + outd + " "
            self.stri1 = self.strin
        if intr:
            self.strin += " "+"-I"+" "+intr+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-I"+" "+"300000"+" "
            self.stri1 = self.strin
        if iso:
            self.strin += " "+"-F"+" "+iso+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-F"+" "+"0.1"+" "
            self.stri1 = self.strin
        if mrn:
            self.strin += " "+"-j"+" "+mrn+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-j"+" "+"0.15"+" "
            self.stri1 = self.strin
        if prm:
            self.strin += " "+"--3-overhang-tolerance"+" "+prm+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--3-overhang-tolerance"+" "+"600"+" "
            self.stri1 = self.strin
        if introvr:
            self.strin += " "+"--intron-overhang-tolerance"+" "+ introvr+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--intron-overhang-tolerance"+" "+"50"+" "
            self.stri1 = self.strin
        if inrmn:
            self.strin += " "+"-m"+ " "+inrmn+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-m"+" "+"200"+" "
            self.stri1 = self.strin
        if instdev:
            self.strin += " "+" -s"+" "+ instdev+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-s"+" "+"80"+" "
            self.stri1 = self.strin
        if maxmle:
            self.strin += " "+"--max-mle-iterations"+" "+ maxmle+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--max-mle-iterations"+" "+"5000"+" "
            self.stri1 = self.strin
        if alp:
            self.strin += " "+"-a"+" "+ alp+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-a"+" "+"0.001"+" "
            self.stri1 = self.strin
        if per:
            self.strin += " "+" -A"+" "+ per+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"-A"+" "+"0.09"+" "
            self.stri1 = self.strin
        if intronover:
            self.strin += " "+"--overhang-tolerance"+" "+ intronover+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--overhang-tolerance"+" "+"8"+" "
            self.stri1 = self.strin
        if maxgen:
            self.strin += " "+"--max-bundle-length"+" "+ maxgen+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--max-bundle-length"+" "+"3500000"+" "
            self.stri1 = self.strin
        if maxnum:
            self.strin += " "+"--max-bundle-frags"+" " +maxnum+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--max-bundle-frags"+" "+"500000"+" "
            self.stri1 = self.strin
        if minintr:
            self.strin += " "+"--min-intron-length"+" "+ minintr+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--min-intron-length"+" "+"50"+" "
            self.stri1 = self.strin
        if minavg:
            self.strin += " "+"--trim-3-avgcov-thresh"+ " "+minavg+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--trim-3-avgcov-thresh"+" "+"10"+" "
            self.stri1 = self.strin
        if fracavg:
            self.strin += " "+"--trim-3-dropoff-frac "+" "+ fracavg+" "
            self.stri1 = self.strin
        else:
            self.strin += " "+"--trim-3-dropoff-frac "+" "+"0.1"+" "
            self.stri1 = self.strin
        print(self.stri1)

        if self.filg == "Yes": # cufflink option along with gtf file
                if self.gtfile1:

                     proc = subprocess.Popen(["cufflinks" +" "+ self.gtfile1+" "+self.stri1+" "+self.file , ""],stdout=subprocess.PIPE, shell=True)
                     (out, err) = proc.communicate()
                else:# cufflink option with no gtf file

                     proc = subprocess.Popen(["cufflinks" +" "+ self.stri1+" "+self.file , ""],stdout=subprocess.PIPE, shell=True)
                     (out, err) = proc.communicate()

                quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
                reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.outfile="transcripts.gtf"

                if reply3 == QtGui.QMessageBox.Yes:
                    proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                quit_msg1 = "if you want to Use Cuffcompare?  (Press Yes if you want)"
                reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                if reply3 == QtGui.QMessageBox.Yes:
                    self.top = cuffcompare.Cuffcomp(self)
                    self.top.closed.connect(self.show)
                    self.top.show()
        elif self.filg == "No": # running from starting I,e from buling index file and alignment options
            proc = subprocess.Popen([self.buildfile, ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            proc = subprocess.Popen([self.bowtie, ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()

            if self.botout == "yes":

                 proc = subprocess.Popen(["gedit"+" "+self.file, ""],stdout=subprocess.PIPE, shell=True)
                 (out, err) = proc.communicate()

            if self.fil =="bowtie":

                    self.file1 =self.file+".sam"
                # sorting bowtie output
                    proc = subprocess.Popen(["sort -k 3,3 -k 4,4n "+" "+self.file+" >"+ self.file1, ""],stdout=subprocess.PIPE, shell=True)
                    (out, err) = proc.communicate()
                    if self.gtfile1 == " ": # cufflink with GTF

                        proc = subprocess.Popen(["cufflinks" + " " + self.stri1 + " " + self.file1, ""],stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()
                    elif self.gtfile1: #without GTF
                       print(self.gtfile1)

                       proc = subprocess.Popen(["cufflinks"+" "+ self.gtfile1+" "+self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                       (out, err) = proc.communicate()


                    quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    self.outfile="transcripts.gtf"

                    if reply3 == QtGui.QMessageBox.Yes:
                        proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()

                    quit_msg1 = "if you want to Use Cuffcompare?  (Press Yes if you want)"
                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)


                    quit_msg1 = "if you want to Use Cuffdiff?  (Press Yes if you want)"
                    reply31 = QtGui.QMessageBox.question(self, 'Message',
                                                        quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    quit_msg1 = "if you want to Use Cuffquant?  (Press Yes if you want)"
                    reply32 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                    quit_msg1 = "if you want to Use Cuffnorm?  (Press Yes if you want)"
                    reply33 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                    quit_msg1 = "if you want to Use Cuffmerge?  (Press Yes if you want)"
                    reply34 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply3 == QtGui.QMessageBox.Yes:
                        self.top = cuffcompare.Cuffcomp(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply32 == QtGui.QMessageBox.Yes:
                        self.top = cuffquant.Cuffq(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply33 == QtGui.QMessageBox.Yes:
                        self.top = cuffnorm.Cuffnorm(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply31 == QtGui.QMessageBox.Yes:
                        self.top = cuffdiff.Cuffdiff(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply34 == QtGui.QMessageBox.Yes:
                        self.top = cuffmerge.Cuffm(self)
                        self.top.closed.connect(self.show)
                        self.top.show()

            elif self.fil == "tophat": # for tophat
                    self.file1 ="/home/amrata/PycharmProjects/bowtieuser/tophat_out/accepted_hits.bam" # topht output

                    if self.gtfile1:
                        proc = subprocess.Popen(["cufflinks" +" "+ self.gtfile1+" "+self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()
                    else:
                        proc = subprocess.Popen(["cufflinks" +" "+ self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()
                    quit_msg = "Successfully created"
                    reply = QtGui.QMessageBox.information(self, 'Message',
                                                              quit_msg, QtGui.QMessageBox.Ok)
                    quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                    quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    self.outfile="transcripts.gtf"

                    if reply3 == QtGui.QMessageBox.Yes:
                            proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                            (out, err) = proc.communicate()
                    quit_msg1 = "if you want to Use Cuffcompare?  (Press Yes if you want)"
                    reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)


                    quit_msg1 = "if you want to Use Cuffdiff?  (Press Yes if you want)"
                    reply31 = QtGui.QMessageBox.question(self, 'Message',
                                                        quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    quit_msg1 = "if you want to Use Cuffquant?  (Press Yes if you want)"
                    reply32 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                    quit_msg1 = "if you want to Use Cuffnorm?  (Press Yes if you want)"
                    reply33 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                    quit_msg1 = "if you want to Use Cuffmerge?  (Press Yes if you want)"
                    reply34 = QtGui.QMessageBox.question(self, 'Message',
                                                         quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply3 == QtGui.QMessageBox.Yes:
                        self.top = cuffcompare.Cuffcomp(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply32 == QtGui.QMessageBox.Yes:
                        self.top = cuffquant.Cuffq(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply33 == QtGui.QMessageBox.Yes:
                        self.top = cuffnorm.Cuffnorm(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply31 == QtGui.QMessageBox.Yes:
                        self.top = cuffdiff.Cuffdiff(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                    if reply34 == QtGui.QMessageBox.Yes:
                        self.top = cuffmerge.Cuffm(self)
                        self.top.closed.connect(self.show)
                        self.top.show()



def main():
	app=QtGui.QApplication(sys.argv)
	form=Cuffl()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


