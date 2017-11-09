from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import cuffcomparegui
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


class Cuffcomp(QtGui.QMainWindow,cuffcomparegui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Cuffcomp, self).__init__( parent)
        self.setupUi(self)
        #self.frame1.hide()
        self.groupBox.hide()
        #self.groupBox_2.hide()


        self.string=" "
        self.str1=" "
        self.str2=" "
        self.fl=" "

        self.connect(self.refannotcmb, SIGNAL('activated(QString)'), self.onIndexChange)

        self.subrefanpush1.clicked.connect(self.selectFl)
        self.selfile.clicked.connect(self.selectF)
        self.mulfile.clicked.connect(self.multifilegtf)
        self.mulfile1.clicked.connect(self.multifile1)

        self.spyes.clicked.connect(self.ignore)
        self.spyes1.clicked.connect(self.ignore1)
        self.asyes.clicked.connect(self.discard)

        self.connect(self.inp, SIGNAL('activated(QString)'), self.showscr1)
        self.Execute.clicked.connect(self.execute)






    def onIndexChange(self): # code for showing reference annotation option
        self.str1 = self.refannotcmb.currentText()
        if self.str1 == "Yes":
            self.groupBox.show()
            self.groupBox.focusPolicy()
            #self.frame1.setGeometry(QtCore.QRect(10, 380, 811, 541))
            self.frame2.setGeometry(QtCore.QRect(10, 380, 811, 541))
            self.Execute.setGeometry(QtCore.QRect(650, 870, 98,27))
        else:
            self.groupBox.hide()
           # self.frame1.setGeometry(QtCore.QRect(10, 170, 811, 541))
            self.frame2.setGeometry(QtCore.QRect(10, 170, 811, 541))
            self.Execute.setGeometry(QtCore.QRect(650, 700, 98,27))

    def onIndexChange2(self):
        self.str2 = self.biascmb.currentText()
        if self.str2=="Yes":
            self.framesh.show()
            self.groupBox_3.show()

        else:
            self.framesh.hide()
            self.Execute.setGeometry(QtCore.QRect(650,750, 98,27))
            #self.Execute.move(650,750)





    def selectF(self):  # select single GTF file
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
                quit_msg = "Error! Please select Proper Mask file(I,e file in the form of(gtf/gff)"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifilegtf()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multifile1(self):  # code for selectin multiple GTF files for Mask operations
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".gtf"
            st1 = ".gff"

            if sta1 in self.fl or st1 in self.fl:
                quit_msg = "Do you want to select any other file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.subrefcomb.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.subrefcomb.count()
                    self.file3 = self.subrefcomb.itemText(0)
                    self.file1 = self.subrefcomb.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1

                    self.multifile1()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.subrefcomb.count()
                    self.file3 = self.subrefcomb.itemText(0)
                    self.file1 = self.subrefcomb.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcomb.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1



            else:
                quit_msg = "Error! Please select Proper Mask file(I,e file in the form of(gtf/gff)"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multifile1()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def selectFl(self): # selecting single GTF files
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.subrefcomb.addItem(self.fl)
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


    def ignore(self): # consider only reference transcripts
        self.string+=" "+"-R"+" "

    def ignore1(self): # conside only input transcripts
        self.string+=" "+"-Q"+" "

    def showscr1(self): # code for discard single exon transfrag
        self.txt = self.inp.currentText()
        if self.txt == "Discard single-exon transfrag and reference transcripts":
            self.string += " "+"-M"+" "
        elif self.txt == "Discard single-exon reference transcripts":
             self.string += " "+"-N"+" "
        else:
            self.string += " "

    def discard(self): #include the "contained" transcripts in the .combined.gtf file
        self.string+=" "+"-C"+" "

    def execute(self): #code for running cufcompare
        self.exon = self.skip.toPlainText()
        self.trans = self.textEdit1.toPlainText()
        if self.exon:
            self.string += " "+"-e"+" "+self.exon
        else:
            self.string += " "+"-e"+" "+"100"
        if self.trans:
            self.string += " "+"-d"+" "+self.exon
        else:
            self.string += " "+"-d"+" "+"100"
        if self.fl == " ":  # This is the code When the user does not select the GTF file
            quit_msg = "Please select the GTF File"
            reply = QtGui.QMessageBox.warning(self, 'warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

        else:  # Execution of Cuffcompare
            quit_msg = "Processing Please wait"
            QtGui.QMessageBox.information(self, 'Message', quit_msg)
            proc = subprocess.Popen(["cuffcompare" +" "+ self.string+ " "+"-o"+" "+" /home/amrata/PycharmProjects/bowtieuser/Cuffcompare" , ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
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

                    relevant_path = os.getcwd()
                    included_extenstions = ['.combined.gtf', '.loci', '.stats', '.tracking', '.transcripts.gtf.tmap']
                    pd = [fn for fn in os.listdir(relevant_path)
                                  if any(fn.endswith(ext) for ext in included_extenstions)]
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
	form=Cuffcomp()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


