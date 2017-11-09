from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import cuffnormgui
import subprocess
import cuff
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge

import allignment
import pickle

#import images
from subprocess import call
from subprocess import Popen, PIPE
import os


class Cuffnorm(QtGui.QMainWindow,cuffnormgui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None): # initialization and linking
        super(Cuffnorm, self).__init__( parent)
        self.setupUi(self)
        self.frame1.hide()
        self.groupBox_4.hide()
        self.string = " "
        self.stri1=" "
        self.lib=" "
        self.std= " "
        self.out = " "
        self.sam1= " "
        self.sam2=" "
        self.outd= " "
        self.fl = " "
        self.connect(self.biascmb, SIGNAL('activated(QString)'), self.onIndexChange2)
        self.selfile.clicked.connect(self.selectFl)
        self.mulfile.clicked.connect(self.multifilegtf)
        self.connect(self.subrefcomb, SIGNAL('activated(QString)'), self.showscr)
        self.connect(self.spyes, SIGNAL('activated(QString)'), self.output)
        self.connect(self.libinpcmb, SIGNAL('activated(QString)'), self.libfun)
        self.connect(self.biascmb1, SIGNAL('activated(QString)'), self.compat)
        self.Execute.clicked.connect(self.executeop)
        self.printyes.clicked.connect(self.printop)
       # self.helpyes.clicked.connect(self.usage)
        self.suppyes.clicked.connect(self.memo2)
        self.servyes.clicked.connect(self.memo3)
        self.connect(self.refannotcmb, SIGNAL('activated(QString)'), self.sambam)
        self.subrefanpush11.clicked.connect(self.selectsamfile)
        self.subrefanpush111.clicked.connect(self.selectsamorbamorcxb)
        self.mulfile51.clicked.connect(self.multisam)
        self.mulfile5.clicked.connect(self.multisamorbamorcxb)


       # self.subrefanpush11.clicked.connect(self.sambamfile)
       # self.subrefanpush111.clicked.connect(self.sambamfile1)
        self.subrefanpushok.clicked.connect(self.samok)
        self.subrefanpushp.clicked.connect(self.insertrep)

    def onIndexChange2(self):
        self.st = self.biascmb.currentText()
        if self.st == "Yes":
            self.groupBox_4.show()
            self.Execute.setGeometry(QtCore.QRect(560, 950, 98, 27))
        else:
            self.groupBox_4.hide()
            self.Execute.setGeometry(QtCore.QRect(560, 500, 98, 27))


    def insertrep(self):# code for insert pushbutton which are in sam or bam options
        self.name = self.ovrtoltxt11.text()
        self.name1 = self.ovrtoltxt111.text()
        self.rep = self.subrefcomb11.currentText()
        self.rep1 = self.subrefcomb111.currentText()
        self.string += " "+"-L"+" "+self.name+","+self.name1+" "+self.rep+" "+self.rep1+" "
        self.ovrtoltxt11.clear()
        self.ovrtoltxt111.clear()
        self.subrefcomb11.clear()
        self.subrefcomb111.clear()

    def samok(self):
        self.frame1.hide()
        self.frame.show()

    def selectsamfile(self):  # code for select single sam or bam or cxb
            self.fl = QtGui.QFileDialog.getOpenFileName()
            if self.fl:
                sta1 = ".sam"
                sta2 = ".bam"
                sta3 = ".cxb"

                if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                    self.subrefcomb11.addItem(self.fl)
                    self.sam2 = self.subrefcomb11.currentText()
                else:
                    quit_msg = "Error! Please select proper file"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                      quit_msg, QtGui.QMessageBox.Ok)
                    self.selectsamfile()
            if not self.fl:
                quit_msg = "There is nothing to load"
                reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                  quit_msg, QtGui.QMessageBox.Ok)

    def multisam(self):  # code for select multiple sam or bam or cxb
        self.fl = QtGui.QFileDialog.getOpenFileName()
        if self.fl:
            sta1 = ".sam"
            sta2 = ".bam"
            sta3 = ".cxb"

            if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                quit_msg = "Do you want to select any other file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.subrefcomb11.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.subrefcomb11.count()
                    self.file3 = self.subrefcomb11.itemText(0)
                    self.file1 = self.subrefcomb11.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb11.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam2 += " " + self.file3
                    self.multisam()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.subrefcomb11.count()
                    self.file3 = self.subrefcomb11.itemText(0)
                    self.file1 = self.subrefcomb11.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb11.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam2 += " " + self.file3


            else:
                quit_msg = "Error! Please select proper file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multisam()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def selectsamorbamorcxb(self): # code for select single sam or bam or cxb
        self.fl = QtGui.QFileDialog.getOpenFileName()
        if self.fl:
            sta1 = ".sam"
            sta2 = ".bam"
            sta3 = ".cxb"
            if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                self.subrefcomb111.addItem(self.fl)
                self.sam1 = self.subrefcomb111.currentText()
            else:
                quit_msg = "Error! Please select proper file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.selectsamorbamorcxb()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multisamorbamorcxb(self): # code for select multiple sam or bam or cxb
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".sam"
            sta2 = ".bam"
            sta3 = ".cxb"

            if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                quit_msg = "Do you want to select any other file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.subrefcomb111.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.subrefcomb111.count()
                    self.file3 = self.subrefcomb111.itemText(0)
                    self.file1 = self.subrefcomb111.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb111.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam1 += " " + self.file3
                    self.multisamorbamorcxb()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.subrefcomb111.count()
                    self.file3 = self.subrefcomb111.itemText(0)
                    self.file1 = self.subrefcomb111.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb111.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam1 += " " + self.file3


            else:
                quit_msg = "Error! Please select proper file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multisamorbamorcxb()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def sambam(self):
        self.sam = self.refannotcmb.currentText()
        if self.sam == "SAM/BAM" or self.sam == "Cuffquant(CXB)":
            self.frame1.show()
            self.frame.hide()



    def printop(self):
        self.string += " " + "--version" + " "

    #def usage(self):
     #   self.stri += " " + "-h" + " "

    def memo2(self): #log-friendly quiet processing (no progress bar)
        self.string += " " + " -q" + " "

    def memo3(self): #do not contact server to check for update availability
        self.string += " " + "--no-update-check" + " "

    def selectFl(self): # code for single gtf file
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.builselcom.addItem(self.fl)
                self.string += " " + self.builselcom.currentText()


            else:
                quit_msg = "Error! Please select proper file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.selectFl()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multifilegtf(self):  # multiple GTF files
                self.fl = QtGui.QFileDialog.getOpenFileName()

                if self.fl:
                    sta1 = ".gtf"
                    st1 = ".gff"

                    if sta1 in self.fl or st1 in self.fl:
                        quit_msg = "Do you want to select any other file(press yes if you want)"
                        reply = QtGui.QMessageBox.question(self, 'Message',
                                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                        self.builselcom.addItem(self.fl)
                        if reply == QtGui.QMessageBox.Yes:

                            num1 = self.builselcom.count()
                            self.file3 = self.builselcom.itemText(0)
                            self.file1 = self.builselcom.itemText(num1)
                            for i in range(num1 - 1):
                                self.file2 = self.builselcom.itemText(i + 1)
                                self.file3 += "," + self.file2
                            self.file3 += self.file1

                            self.multifilegtf()

                        elif reply == QtGui.QMessageBox.No:
                            self.readfl2 = " "
                            num1 = self.builselcom.count()
                            self.file3 = self.builselcom.itemText(0)
                            self.file1 = self.builselcom.itemText(num1)
                            for i in range(num1 - 1):
                                self.file2 = self.builselcom.itemText(i + 1)
                                self.file3 += "," + self.file2
                            self.file3 += self.file1



                    else:
                        quit_msg = "Error! Please select Proper file(I,e file in the form of(gtf)"
                        reply = QtGui.QMessageBox.warning(self, 'Error',
                                                          quit_msg, QtGui.QMessageBox.Ok)
                        self.multifilegtf()
                else:
                    quit_msg = "There is nothing to load"
                    reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                      quit_msg, QtGui.QMessageBox.Ok)


                    # print(self.gtffile)

    def compat(self):# code for hits
        self.com = self.biascmb1.currentText()
        if self.com == "Compatible Hits":
            self.string += " "+"--compatible-hits-norm"+" "+"True"
        else:
            self.string += " "+"--total-hits-norm"+" "+"True"

    def showscr(self): # code for library norm method
        self.str1= self.subrefcomb.currentText()
        self.lib = " "+" --library-norm-method"+" "+self.str1+" "

    def libfun(self): # code for library type
        self.std = self.libinpcmb.currentText()
        if self.std:
            self.string += " "+"--library-type"+" "+self.std
        else:
            self.string += " "+"--library-type"+" "+"fr-unstranded"

    def output(self): #Format for output tables
        self.str1= self.spyes.currentText()
        self.out = " "+" --output-format"+" "+self.str1+" "

    def executeop(self): # code for running cuffnorm
        outd = self.outdirtxt.text()
        thrd = self.thrdtxt.text()
        if thrd:
            self.string += " " + "-p" + " " + thrd + " "
            self.stri1 = self.string
        if outd:
            self.outd = outd
            self.string += " " + "-o" + " " + outd + " "
            self.stri1 = self.string
        else:
            self.outd = "/home/amrata/PycharmProjects/bowtieuser/cuffnormout"
            self.string += " "+"-o"+" "+"/home/amrata/PycharmProjects/bowtieuser/cuffnormout"
            self.stri1 = self.string
        if not self.lib:
            self.string += " " + " --library-norm-method" + " " + "geometric" + " "
            self.stri1 = self.string
        if not self.std:
            self.string += " " + "--library-type" + " " + "fr-unstranded"
            self.stri1 = self.string
        if not self.out:
            self.string = " " + " --output-format" + " " +"Simple Table"
            self.stri1 = self.string

        if self.fl == " ":  # This is the code When the user does not select the GTF file
            quit_msg = "Please select the GTF File"
            reply = QtGui.QMessageBox.warning(self, 'warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
        if self.sam1 == " " or self.sam2 ==" ":  # This is the code When the user does not select the SAM or BAM file
            quit_msg = "Please select the SAM or BAM file "
            reply = QtGui.QMessageBox.warning(self, 'warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
        else:  # Execution of Cuffnorm
            quit_msg = "Processing Please wait"
            QtGui.QMessageBox.information(self, 'Message', quit_msg)

            proc = subprocess.Popen(["cuffnorm" + " " + self.stri1, ""], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            #p1=proc.stdout.readlines()
            print(self.stri1)
            #print(p1)
            print(out)
            print(err)
            f = open("error1", "w")
            f.write(str(err))
            f.close()
            f = open("error1", "r")
            self.txt = f.read(5)
            self.txt1 = f.read(10)
            f.close()
            if not self.txt1:

                quit_msg1 = "Successfully created"
                reply3 = QtGui.QMessageBox.information(self, 'Message',
                                            quit_msg1, QtGui.QMessageBox.Ok)
                quit_msg1 = "if you want to See the  Output?  (Press Yes if you want)"
                reply3 = QtGui.QMessageBox.question(self, 'Message',
                                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply3 == QtGui.QMessageBox.Yes:
                    pd = QtGui.QFileDialog.getOpenFileNames(self, "output", self.outd)
                    for i in pd:
                        proc = subprocess.Popen(["gedit" + " " + i, ""], stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()

                self.close()
            elif self.txt1:  # if error is there
                quit_msg = "Error! Please check whether you provide proper value or not"
                reply = QtGui.QMessageBox.warning(self, 'Message',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.txt = " "
                self.txt1 = " "


def main():
	app=QtGui.QApplication(sys.argv)
	form=Cuffnorm()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


