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


class Cuffl(QtGui.QMainWindow,cufflinksgui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Cuffl, self).__init__( parent)
        self.setupUi(self)
        fp1 = open("sharedcufffile.pkl","rb")
        self.file = pickle.load(fp1)
        fpt1 = open("build.pkl","rb")
        self.buildfile = pickle.load(fpt1)
        fptt1 = open("bowtieout.pkl","rb")
        self.bowtie = pickle.load(fptt1)
        #fptr = open("bowtieout.pkl","rb")
        #self.bowtout = pickle.load(fptr)
        fptr1 = open("botout.pkl","rb")
        self.botout = pickle.load(fptr1)

        self.strin=" "
        self.bias = " "
        self.gtfile1= " "
        self.maskfil= " "


        self.parent = parent
        self.groupBox_4.hide()
        self.refgrp.hide()
        self.framesh.hide()
       # self.groupBox_2.hide()
        self.groupBox.hide()
        #self.groupBox_5.hide()
        self.groupBox_31.hide()
        self.connect(self.refannotcmb, SIGNAL('activated(QString)'), self.onIndexChange)
        self.connect(self.biascmb, SIGNAL('activated(QString)'), self.onIndexChange2)
        self.connect(self.seqcmb, SIGNAL('activated(QString)'), self.showscr)
        self.connect(self.advcufoptcmb, SIGNAL('activated(QString)'), self.nextshow)
        #self.connect(self.comboBox_13, SIGNAL('activated(QString)'), self.showscr1)
        self.subrefanpusk.clicked.connect(self.selectFile)
        self.subrefanpusk1.clicked.connect(self.selectF)
        self.maskpush.clicked.connect(self.selectFl)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.changeText)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText1)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL('valueChanged(int)'), self.changeText2)
        QtCore.QObject.connect(self.horizontalSlider_4, QtCore.SIGNAL('valueChanged(int)'), self.changeText3)
        QtCore.QObject.connect(self.horizontalSlider_5, QtCore.SIGNAL('valueChanged(int)'), self.changeText4)
        QtCore.QObject.connect(self.horizontalSlider_6, QtCore.SIGNAL('valueChanged(int)'), self.changeText5)
        self.connect(self.subrefancmb, SIGNAL('activated(QString)'), self.runindex)
        self.connect(self.subrefcomb, SIGNAL('activated(QString)'), self.runindex)
        self.connect(self.maskcmb, SIGNAL('activated(QString)'), self.runindex1)


        self.connect(self.comboBox, SIGNAL('activated(QString)'), self.rnashow)
        self.connect(self.tilingtxt, SIGNAL('activated(QString)'), self.tiling)
        self.connect(self.multireadcmb, SIGNAL('activated(QString)'), self.multiread)
        self.connect(self.lengthcorcmb, SIGNAL('activated(QString)'), self.lengthc)

        self.connect(self.libinpcmb, SIGNAL('activated(QString)'), self.libfun)
        self.strin = " "+"--library-type"+" "+"fr-unstranded"
        self.execute.clicked.connect(self.executeop)


        self.ok.clicked.connect(self.okclicked)

    def tiling(self):
        self.st=self.tilingtxt.currentText()
        if self.st=="Yes":
            self.strin += " "+"--no-faux-reads"+" "+" "+"True"
        else:
            self.strin +=" "+"--no-faux-reads"+" "+" "+"False"

    def libfun(self):
        self.std = self.libinpcmb.currentText()
        if self.std:
            self.strin += " "+"--library-type"+" "+self.std
        else:
            self.strin += " "+"--library-type"+" "+"fr-unstranded"

    def runindex(self):
        self.gtfile = self.subrefancmb.currentText()
        self.gtf= self.subrefcomb.currentText()
        if self.gtfile:
            self.gtfile1 = " "+"-G"+" "+self.gtfile
        elif self.gtf:
            self.gtfile1 = " "+"-G"+" "+self.gtf

    def runindex1(self):
        self.maskfil = self.maskcmb.currentText()
        self.maskfil = " "+"-M"+" "+self.maskfil
        self.strin += " "+self.maskfil+" "








    def lengthc(self):
        self.stc=self.lengthcorcmb.currentText()
        if self.stc == "Cufflinks Effective Length Correction":
            self.strin += " "+"--no-effective-length-correction"+" "+"False"
        else:
            self.strin += " "+"--no-effective-length-correction"+" "+"True"

        if self.stc== "No Length Correction at all (use raw counts)":
            self.strin += " "+"--no-length-correction"+" "+"True"
        else:
            self.strin += " "+"--no-length-correction"+" "+"False"

    def selectFile(self):
        self.subrefancmb.addItem(QtGui.QFileDialog.getOpenFileName())


    def selectF(self):
        self.subrefcomb.addItem(QtGui.QFileDialog.getOpenFileName())

    def selectFl(self):
        self.maskcmb.addItem(QtGui.QFileDialog.getOpenFileName())



    def multiread(self):
        self.st= self.multireadcmb.currentText()
        if self.st=="Yes":
            self.strin +=" "+"-u"+" "+"True"
        else:
            self.strin +=" "+"-u"+" "+"False"

    def rnashow(self):
        self.st = self.comboBox.currentText()
        if self.st =="Yes":
            self.strin += " " +"--compatible-hits-norm"+" "+"True"
        else:
            self.strin += " " +"--compatible-hits-norm"+" "+"False"

    def changeText1(self, value):
        if value:
            self.z = value
            self.maxintrontxt.setText(str(self.z))
        else:
            self.z = "300000"

    def changeText5(self, value):
        if value:
            self.z1 = float(value)/10000
            self.fracavgtxt.setText(str(self.z1))
        else:
            self.z1 = "0.1"




    def changeText(self, value):
        if value:
            self.z1 = float(value)/10000
            self.minisoformtxt.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def changeText3(self, value):
        if value:
            self.z1 = float(value)/10000
            self.alphatxt.setText(str(self.z1))
        else:
            self.z1 = "0.001"

    def changeText4(self, value):
        if value:
            self.z1 = float(value)/10000
            self.percenttxt.setText(str(self.z1))
        else:
            self.z1 = "0.09"




    def changeText2(self, value):
        if value:
            self.z11 = float(value)/10000
            self.mrnatxt.setText(str(self.z11))
        else:
            self.z11 = "0.15"

    def onIndexChange(self):
                self.str1 = self.refannotcmb.currentText()
                #self.groupBox_2.hide()
                self.framesh.hide()
                if self.str1 == "No":
                    self.bias = "0"
                    self.refgrp.hide()
                    self.groupBox.hide()
                    self.frame1.setGeometry(QtCore.QRect(10, 310, 711, 51))
                    self.frame2.setGeometry(QtCore.QRect(10, 380, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 750, 75, 27))
                        #self.yesnext.show()
                       #self.parnext.hide()
                elif self.str1 == "Use reference annotation":
                    self.bias = "1"
                    self.refgrp.show()
                    self.groupBox.hide()
                    self.frame1.setGeometry(QtCore.QRect(10, 450, 711, 141))
                    self.frame2.setGeometry(QtCore.QRect(10, 530, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 850, 75, 27))
                elif self.str1 == "Use reference annotation as guide":
                    self.bias = "2"
                    self.refgrp.hide()
                    self.groupBox.show()
                    self.frame1.setGeometry(QtCore.QRect(10, 590, 711, 141))
                    self.frame2.setGeometry(QtCore.QRect(10, 660, 711, 1541))
                    self.execute.setGeometry(QtCore.QRect(600, 950, 75, 27))

    def onIndexChange2(self):
                self.str1 = self.biascmb.currentText()

                        #self.yesnext.show()
                       #self.parnext.hide()
                if self.str1 == "Yes":


                   # self.frame1.setGeometry(QtCore.QRect(10, 450, 711, 141))


                    if self.bias == "1":
                        print(self.bias)
                        #self.groupBox_2.show()
                        self.framesh.show()

                        #self.groupBox_2.setGeometry(QtCore.QRect(10, 610, 731, 161))

                        #self.groupBox_2.show()
                        self.frame2.setGeometry(QtCore.QRect(10, 680, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 1050, 75, 27))
                    elif self.bias == "2":
                        print(self.bias)
                        #self.groupBox_2.show()
                        self.framesh.show()
                        #self.groupBox_2.setGeometry(QtCore.QRect(10, 610, 731, 161))

                        #self.groupBox_3.show()
                        self.frame2.setGeometry(QtCore.QRect(10, 800, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 1200, 75, 27))
                        self.connect(self.seqcmb, SIGNAL('activated(QString)'), self.showscr)

                    else:

                        self.framesh.show()
                        #self.groupBox_3.show()
                        self.frame2.setGeometry(QtCore.QRect(10, 530, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 850, 75, 27))
                elif self.str1 == "No":
                    if self.bias == "1":
                    #print(self.str1)
                        self.framesh.hide()
                        self.groupBox_2.hide()
                        self.groupBox_3.hide()
                        self.frame2.setGeometry(QtCore.QRect(10, 540, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 750, 75, 27))
                    elif self.bias == "2":
                    #print(self.str1)
                        self.framesh.hide()
                        self.groupBox_2.hide()
                        self.groupBox_3.hide()
                        self.frame2.setGeometry(QtCore.QRect(10, 660, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 950, 75, 27))
                    else:
                        self.framesh.hide()
                        self.groupBox_2.hide()
                        self.groupBox_3.hide()

                    #self.frame1.setGeometry(QtCore.QRect(10, 310, 711, 51))
                        self.frame2.setGeometry(QtCore.QRect(10, 380, 711, 1541))
                        self.execute.setGeometry(QtCore.QRect(600, 750, 75, 27))

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

    def showscr1(self):
                self.str2 = self.comboBox_13.currentText()
                if self.str2 == "Specify job resource parameters":
                    #self.groupBox_.hide()
                    self.groupBox_5.show()
                else:
                    self.groupBox_5.hide()
                    #self.groupBox_31.show()

    def executeop(self):
        quit_msg1 = "Processing Please Wait Some Minutes"
        reply3 = QtGui.QMessageBox.question(self, 'Message',
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

        self.file1 ="ourpro1.sam.sorted"
        proc = subprocess.Popen([self.buildfile, ""],stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        proc = subprocess.Popen([self.bowtie, ""],stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if self.botout == "yes":
            print(self.botout)
            proc = subprocess.Popen(["gedit"+" "+self.file, ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()


            proc = subprocess.Popen(["sort -k 3,3 -k 4,4n "+" "+self.file+" >"+ self.file1, ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            if self.gtfile1:
                proc = subprocess.Popen(["cufflinks" +" "+ self.gtfile1+" "+self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
            else:
                proc = subprocess.Popen(["cufflinks" +" "+ self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()

            quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            self.outfile="transcripts.gtf"

            if reply3 == QtGui.QMessageBox.Yes:
                proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
        else:
            proc = subprocess.Popen(["sort -k 3,3 -k 4,4n "+" "+self.file+" >"+ self.file1, ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            if self.gtfile1:
                proc = subprocess.Popen(["cufflinks" +" "+ self.gtfile1+" "+self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
            else:
                proc = subprocess.Popen(["cufflinks" +" "+ self.stri1+" "+self.file1 , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
            quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            self.outfile="transcripts.gtf"

            if reply3 == QtGui.QMessageBox.Yes:
                proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()




def main():
	app=QtGui.QApplication(sys.argv)
	form=Cuffl()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


