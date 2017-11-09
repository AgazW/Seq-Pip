from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import cuffquantgui
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


class Cuffq(QtGui.QMainWindow,cuffquantgui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Cuffq, self).__init__( parent)
        self.setupUi(self)
        fp1 = open("sharedcufffile.pkl", "rb")
        self.file = pickle.load(fp1)
        self.stri=" "
        self.temp=" "
        self.file1=" "
        self.txt1=" "
        self.fle=" "
        self.fl=" "
        self.readfl1=" "
        self.read=" "                 #Initializing the variables.

        self.grplocal.hide()
        self.grphis.hide()
        self.grpcuff.hide()
        self.grpper.hide()
        self.grpset.hide()
#        self.grprep.hide()
        self.grprepli.hide()             #Initially GroupBox must be hide

#        self.connect(self.cmbper,SIGNAL('activated(QString)'), self.perf)
        self.connect(self.cmbseq,SIGNAL('activated(QString)'), self.sequ)
        self.connect(self.cmbapp,SIGNAL('activated(QString)'), self.apply)
        self.connect(self.cmbset,SIGNAL('activated(QString)'), self.set)
        self.connect(self.cmbpar,SIGNAL('activated(QString)'), self.param)
        self.connect(self.cmblib,SIGNAL('activated(QString)'), self.library)
#        self.connect(self.cmbgtf,SIGNAL('activated(QString)'), self.gtf)        #Providing the link to ComboBox when ComboBox is pressed
        #self.connect(self.cmbfile,SIGNAL('activated(QString)'), self.gtffile)
        self.mulyes.clicked.connect(self.muly)
        self.ok.clicked.connect(self.oky)
        self.bck.clicked.connect(self.back)
        self.bckfr.clicked.connect(self.backframe)
        self.Execute.clicked.connect(self.execute)
        self.sing.clicked.connect(self.single)
#        self.rep.clicked.connect(self.repl)
#        self.clo.clicked.connect(self.closep)
        #self.addre.clicked.connect(self.addrep)
        self.fileu.clicked.connect(self.filegt)      #Providing the link to Push Button when Push Button is pressed

    def repl(self):
        self.grprep.show()
        self.frame.hide()

    #def gtffile(self):
        #self.txt1 = self.cmbfile.currentText()
        #self.stri += " "+txt+" "

    def filegt(self):
         #Code for Accepting the SAM or BAM file
        self.fle = (QtGui.QFileDialog.getOpenFileName())
        if self.fle:
            sta1 = ".sam"
            st1 = ".bam"

            if  st1 in self.fle or sta1 in self.fle:
                self.cmbfile.addItem(self.fle)
                self.read = self.cmbfile.currentText()
               # print(self.read)
            else:
                quit_msg = "Error! Please select the SAM or BAM file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.filegt()
        if not self.fle:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
    def muly(self):
        self.stri +=" "+"-u"+" "      #Code to set the Multi-read correct

    def closep(self):
        self.grprep.hide()
        self.grprepli.hide()
        self.frame.show()

    def addrep(self):
        self.grprepli.show()
        self.frame.hide()
        self.addre.setGeometry(QtCore.QRect(10, 200, 230, 27))
        self.clo.setGeometry(QtCore.QRect(500, 200, 230, 27))

    def perf(self):
        txt = self.cmbper.currentText()
        if txt == "Yes":
            self.grpper.show()
            self.frame.hide()
            self.grprep.hide()
        elif txt == "No":
            self.grpper.hide()
            self.frame.show()
            self.grprep.show()

    def sequ(self):
        txt = self.cmbseq.currentText()
        if txt == "Locally cached":
            self.grplocal.show()
            self.grphis.hide()
            self.grprep.hide()
        elif txt == "History":
            self.grphis.show()
            self.grplocal.hide()
            self.grprep.hide()

    def oky(self):
        self.grpper.hide()
        self.frame.show()
        self.grprep.show()

    def apply(self):
        #Code to set the Length Correction. It has 2 option
        txt = self.cmbapp.currentText()
        if txt == "Standrad length correction":
            self.stri = " "+"--no-effective-length-correction"+" "+"False"
        else:
            self.stri = " "+"--no-effective-length-correction"+" "+"True"
        if txt == "No length correction at all(use raw counts)":
           self.stri = " "+"--no-length-correction"+" "+"False"
        else:
            self.stri = " "+"--no-length-correction"+" "+"True"

    def set(self):
        self.grpset.show()
        self.frame.hide()
       # self.grprep.hide()

    def back(self):
        self.grpset.hide()
        self.frame.show()
        #self.grprep.show()

    def param(self):
        #Code to display the option for Additional Parameter for read file
        txt = self.cmbpar.currentText()
        if txt == "Yes":
            self.grpcuff.show()
            self.frame.hide()
           # self.grprep.hide()
        elif txt == "No":
            self.grpcuff.hide()
            self.frame.show()
            #self.grprep.show()

    def library(self):
        #Code to display the Library type option
        txt = self.cmblib.currentText()
        if txt == "ff-firststrand":
            self.stri +=" "+"--library-type"+" "+"ff-firststrand"+" "
        elif txt == "ff-secondstrand":
            self.stri +=" "+"--library-type"+" "+"ff-secondstrand"+" "
        elif txt == "ff-unstranded":
            self.stri +=" "+"--library-type"+" "+"ff-unstranded"+" "
        elif txt == "fr-firststrand":
            self.stri +=" "+"--library-type"+" "+"fr-firststrand"+" "
        elif txt == "fr-secondstrand":
            self.stri +=" "+"--library-type"+" "+"fr-secondstrand"+" "
        elif txt == "fr-unstranded":
            self.stri +=" "+"--library-type"+" "+"fr-unstranded"+" "
        elif txt == "transfrags":
            self.stri +=" "+"--library-type"+" "+"transfrags"+" "



    def backframe(self):
        self.grpcuff.hide()
        self.frame.show()
        #self.grprep.show()

    def single(self):
        #Code for Accepting GTF file
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.cmbgtf.addItem(self.fl)
                self.readfl1 = self.cmbgtf.currentText()
                #print(self.readfl1)
            else:
                quit_msg = "Error! Please select the GTF file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.single()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    #def gtf(self):
        #self.file1 = self.cmbgtf.currentText()

    def execute(self):
        #Code to execute Cuffquant when Execute button is pressed..It will set the default value.
        maxe = self.max.text()
        if maxe:
            self.stri += " "+"--max-mle-iterations"+" "+maxe+" "
            self.stri1 = self.stri
        else:
            self.stri += " "+"--max-mle-iterations"+" "+"5000"+" "
            self.stri1 = self.stri

        loce = self.loc.text()
        if loce:
             self.stri += " "+"--max-bundle-frags  "+" "+loce+" "
             self.stri1 = self.stri
        else:
            self.stri += " "+"--max-bundle-frags  "+" "+"500000"+" "
            self.stri1 = self.stri
        maxr = self.the.text()
        if maxr:
            self.stri += " "+"-p"+" "+maxr
            self.stri1 = self.stri
        else:
            self.stri += " "+"-p"+" "+"1"
            self.stri1 = self.stri
        mater = self.mate.text()
        if maxr:
            self.stri += " "+"-m"+" "+mater
            self.stri1 = self.stri
        else:
            self.stri += " "+"-m"+" "+"200"
            self.stri1 = self.stri
        stdr = self.std.text()
        if stdr:
            self.stri += " "+"-s"+" "+stdr
            self.stri1 = self.stri
        else:
            self.stri += " "+"-s"+" "+"80"
            self.stri1 = self.stri


        if self.fl ==" ":    #This is the code When the user does not select the GTF file
           quit_msg = "Please select the GTF File"
           reply = QtGui.QMessageBox.warning(self, 'warning',
                                      quit_msg, QtGui.QMessageBox.Ok)
        if self.fle== " ":    #This is the code When the user does not select the SAM or BAM file
           quit_msg = "Please select the SAM or BAM file "
           reply = QtGui.QMessageBox.warning(self, 'warning',
                                      quit_msg, QtGui.QMessageBox.Ok)
        else:                #Execution of Cuffquant
            quit_msg1 = "Processing Please Wait Some Minutes"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Ok)
            proc = subprocess.Popen(["cuffquant" +" "+ self.stri1 +" "+ self.fl +" "+ self.fle , ""],stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            quit_msg1 = "Successfully Created"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                                quit_msg1, QtGui.QMessageBox.Ok)
            self.close()
           # print(self.fl)
            #print("cuffquant" +" "+ self.stri1 +" "+ self.fl +" "+ self.fle , "")




def main():
	app=QtGui.QApplication(sys.argv)
	form=Cuffq()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()

