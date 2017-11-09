from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
import os
from os.path import isfile, join
import cuffmergegui
import subprocess
import allignment
import pickle
import cuff
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge
from subprocess import Popen, PIPE


class Cuffm(QtGui.QMainWindow,cuffmergegui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Cuffm, self).__init__( parent)
        self.setupUi(self)
        fp1 = open("sharedcufffile.pkl", "rb")
        self.file = pickle.load(fp1)
        fp2 = open("sharedcufffile.pkl", "rb")
        self.file = pickle.load(fp2)
        self.stri=" "
        self.stri1=" "
        self.strp=" "
        self.strw=" "
        self.temp=" "
        self.txt1=" "
        self.file1=" "
        self.file2=" "
        self.file3=" "  #Initializing the variables.


        self.grpref.hide()
        self.grphis.hide()
        self.grplocal.hide()
        self.grpseq.hide()
        self.grpadd.hide()
        self.grpuse.hide()    #Initially GroupBox must be hide


        self.connect(self.cmbref,SIGNAL('activated(QString)'), self.reference)
#        self.connect(self.cmbgtfi,SIGNAL('activated(QString)'), self.gtffile)
#        self.connect(self.cmbgtf,SIGNAL('activated(QString)'), self.gtf)
        self.connect(self.cmbseq,SIGNAL('activated(QString)'), self.sequ)
        self.connect(self.cmbsour,SIGNAL('activated(QString)'), self.source)
#        self.connect(self.cmbadd,SIGNAL('activated(QString)'), self.addgtf)
                                                          #Providing the link to ComboBox when ComboBox is pressed
        #self.ok.clicked.connect(self.oka)
        self.sin.clicked.connect(self.raw)
        self.Execute.clicked.connect(self.executeop)
        self.bckf.clicked.connect(self.backf)
        self.mul.clicked.connect(self.multi)
        self.add.clicked.connect(self.addg)
#        self.addp.clicked.connect(self.addpush)
#        self.sinp.clicked.connect(self.filep)
#        self.addpu.clicked.connect(self.addpus)
                                                            #Providing the link to Push Button when Push Button is pressed
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText)

    def reference(self):
        #It is used to display the Reference Annotation option.
        txt = self.cmbref.currentText()
        if txt == "Yes":
            self.grpref.show()
            self.grpfra.setGeometry(QtCore.QRect(10, 270, 841, 200))
            self.Execute.setGeometry(QtCore.QRect(500, 500, 75, 27))
        elif txt == "No":
            self.grpref.hide()
            self.grpfra.setGeometry(QtCore.QRect(10, 200, 841, 200))
            #self.grpfra.setGeometry(QtCore.QRect(10, 270, 841, 131))
            self.Execute.setGeometry(QtCore.QRect(500, 380, 75, 27))


    def raw(self):
        #Code for selecting the Reference Annotation File
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.cmbgtfi.addItem(self.fl)
               # self.readfl1 = self.cmbgtfi.currentText()
                txt = self.cmbgtfi.currentText()
                self.stri +=" "+"-g"+" "+txt
                self.stri1 = self.stri
            else:               #When user does not select the Reference Annotation file
                quit_msg = "Error! Please select the Reference Annotation file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)

        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)




    #def gtf(self):
       # self.file1 = self.cmbgtf.currentText()
       # self.strp = " "+self.file1+" "

    #def gtffile(self):
     #    txt = self.cmbgtfi.currentText()
      #   self.stri +=" "+"-g"+" "+txt
       #  self.stri1 = self.stri


   # def gfile(self):
         #txt2 = self.cmbgtfil.currentText()
         #self.stri +=" "+"-g"+" "+txt2
         #self.strp +=" "+txt2+" "

    def addg(self):
        #Code for Accepting the multiple Transcripts file
       self.fl = (QtGui.QFileDialog.getOpenFileName())
       if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                quit_msg = "Do you want to select any other transcripts file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',

                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.cmbadd.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:
                    num = self.cmbadd.count()
                    self.file3 = self.cmbadd.itemText(0)
                    self.file1 = self.cmbadd.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbadd.itemText(i + 1)
                        self.file3 += " " + self.file2 + " "
                    self.file3 += self.file1
                    self.strp += " " + self.file3 + " "
                    self.addg()
                elif reply == QtGui.QMessageBox.No:
                    num = self.cmbadd.count()
                    self.file3 = self.cmbadd.itemText(0)
                    self.file1 = self.cmbadd.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbadd.itemText(i + 1)
                        self.file3 += " " + self.file2 + " "
                    self.file3 += self.file1
                    self.strp += " " + self.file3 + " "
                    #print(self.strp)
                ##if reply == QtGui.QMessageBox.Yes:
                  # self.txt1 = self.cmbadd.currentText()
                  # self.strp += " "+self.txt1+" "
                   #print(self.strp)
                   #self.addg()
                #elif reply == QtGui.QMessageBox.No:
                 #  self.txt1 = self.cmbadd.currentText()
                  # self.strp += " "+self.txt1+" "
            else:
                quit_msg = "Error! Please select the transcripts file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.addg()
       if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
    def addpush(self):
        self.grpadd.show()
        self.frame.hide()

    def closep(self):
        self.grpadd.hide()
        #self.grpaddg.hide()
        self.frame.show()

    def filep(self):
         self.cmbgtfil.addItem(QtGui.QFileDialog.getOpenFileName())
         self.temp = self.cmbgtfil.currentText()
         if not self.temp:
            quit_msg = "Error! Please select the read file "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                 quit_msg, QtGui.QMessageBox.Ok)

    def addpus(self):
        self.addpu.setGeometry(QtCore.QRect(10, 200, 230, 27))
        self.clos.setGeometry(QtCore.QRect(500, 200, 70, 27))
        self.grpaddg.show()

    def sequ(self):
        txt = self.cmbseq.currentText()
        if txt == "Yes":
            self.grpseq.show()
            self.frame.hide()
        elif txt == "No":
            self.grpseq.hide()
            self.frame.show()

    def backf(self):
        self.grpseq.hide()
        self.frame.show()

    def source(self):
        txt = self.cmbsour.currentText()
        if txt == "Locally cached":
            self.grplocal.show()
            self.grphis.hide()
        elif txt == "History":
            self.grphis.show()
            self.grplocal.hide()


    def changeText(self, value):
        if value:
            self.z1 = float(value)/10000
            self.iso.setText(str(self.z1))
        else:
            self.z1 = "0.05"

    def oka(self):
        self.grpref.hide()
        self.frame.show()

    def multi(self):
        #Code for accepting the transcripts file
       self.fl = (QtGui.QFileDialog.getOpenFileName())
       if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.cmbgtf.addItem(self.fl)
                self.txt1 = self.cmbgtf.currentText()
                self.strp = " "+self.txt1+" "
                #print(self.strp)

            else:
                quit_msg = "Error! Please select the transcripts file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multi()
       if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
    def executeop(self):
        #code for executing Cuffmerge when Execute button is pressed. It will set the default value.
        isof = self.iso.text()
        if isof:
            self.stri += " "+"--min-isoform-fraction"+" "+isof+" "
            self.stri1 = self.stri
        maxr = self.max.text()
        if maxr:
            self.stri += " "+"-p"+" "+maxr
            self.stri1 = self.stri
        else:
            self.stri += " "+"-p"+" "+"1"
            self.stri1 = self.stri
        #self.file1 ="/home/user/PycharmProjects/tophat/tophat_out/accepted_hits.bam"
        ## proc.wait()

        fp2 = open("assembly_GTF_list.txt", "w")     #Multiple transcripts files are put into this text file
        fp2.write(self.strp)
        fp2.close()
        self.gtf = "assembly_GTF_list.txt"
        if self.strp ==" ":                 #When user does not select GTF file
           quit_msg = "Please select the GTF File"
           reply = QtGui.QMessageBox.warning(self, 'warning',
                                      quit_msg, QtGui.QMessageBox.Ok)
        else:                                            #Execution of cuffmerge
           quit_msg1 = "Processing Please Wait Some Minutes"
           reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Ok)
           proc = subprocess.Popen(["cuffmerge" +" "+ self.stri1+" "+ self.gtf , ""],stdout=subprocess.PIPE, shell=True)
           (out, err) = proc.communicate()
           #print("cuffmerge" +" "+ self.stri1+" "+self.gtf , "")
           quit_msg1 = "if you want to See the Final Output?  (Press Yes if you want)"
           reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
           self.outfile="/home/user/PycharmProjects/tophat/merged_asm/merged.gtf"     #It displays the path of cuffmerge output


           if reply3 == QtGui.QMessageBox.Yes:
                proc = subprocess.Popen(["gedit" +" "+self.outfile , ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
           self.close()





def main():
	app=QtGui.QApplication(sys.argv)
	form=Cuffm()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()
