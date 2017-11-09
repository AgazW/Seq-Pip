from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT
from PyQt4 import QtCore
import sys
from os import listdir
from os.path import isfile, join
import tophatgui
import subprocess
import pickle
from subprocess import call
from subprocess import Popen, PIPE
import os
import cuff
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge


class Top(QtGui.QMainWindow,tophatgui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Top, self).__init__(parent)
        self.setupUi(self)
        fp = open("shared.pkl","rb")
        self.file = pickle.load(fp)
        #fp1 = open("sharedcuff.pkl","rb")
        #self.cont = pickle.load(fp1)
        #fp1.close()
        filp = open("nocont.pkl", "rb")
        self.nofil = pickle.load(filp)
        filp.close()
        fpt1 = open("build.pkl", "rb")
        self.buildfile = pickle.load(fpt1)
        fpt1.close()

        #self.comboBox_4.hide()
        self.pargp.hide()
        self.grpallow.hide()
        self.grpsup.hide()
        self.grpraw.hide()
        self.grpfus.hide()
        self.grpset.hide()
        self.grpcov.hide()
        self.grpopt.hide()
        self.grpgene.hide()
        self.grpid.hide()
        self.grpcomp.hide()
        self.grppar.hide()
        self.grpali.hide()
        self.grpscr.hide()
        self.grpeff.hide()
        self.grpsin.hide()
        self.grppair.hide()
        self.grppairc.hide()            #Initially GroupBox must be hide


        self.str1 = " "
        self.stri = " "
        self.st = " "
        self.fr = " "
        self.fil = " "
        self.fi = " "
        self.fip = " "
        self.temp =" "
        self.tem =" "
        self.te =" "
        self.ste =" "
        self.fl =" "
        self.readfl1 =" "
        self.txt1=" "
        self.readfl2 =" "            #Initializing the variables.

        #self.anal.connect(self.anal,SIGNAL("currentIndexChanged(int)"),SLOT("onIndexChange(int)"))
        self.connect(self.anal, SIGNAL('activated(QString)'), self.onIndexChange)
        #QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText)
        self.connect(self.libtype, SIGNAL('activated(QString)'), self.library)
        self.connect(self.cmbyes,SIGNAL('activated(QString)'), self.yesbow)
        self.connect(self.cmballow,SIGNAL('activated(QString)'), self.allowin)
        self.connect(self.cmbsup,SIGNAL('activated(QString)'), self.supdata)
        self.connect(self.cmbgene,SIGNAL('activated(QString)'), self.genean)
        self.connect(self.cmbraw,SIGNAL('activated(QString)'), self.rawjun)
        self.connect(self.cmbgemo,SIGNAL('activated(QString)'), self.rawju)
        self.connect(self.cmbjunc,SIGNAL('activated(QString)'), self.rjunc)
        self.connect(self.cmbsupjn,SIGNAL('activated(QString)'), self.supjn)
        self.connect(self.cmbcov,SIGNAL('activated(QString)'), self.cover)
        self.connect(self.cmbmicro,SIGNAL('activated(QString)'), self.micro)
        self.connect(self.cmbfus,SIGNAL('activated(QString)'), self.fusion)
        self.connect(self.cmbset,SIGNAL('activated(QString)'), self.set)
        self.connect(self.cmbpre,SIGNAL('activated(QString)'), self.preset)
        self.connect(self.cmbopt,SIGNAL('activated(QString)'), self.option)
#        self.connect(self.cmbread,SIGNAL('activated(QString)'), self.read)
        self.connect(self.cmbali,SIGNAL('activated(QString)'), self.align)
        self.connect(self.cmbscr, SIGNAL('activated(QString)'), self.score)
        self.connect(self.cmbeff, SIGNAL('activated(QString)'), self.effort)
        self.connect(self.cmbsin, SIGNAL('activated(QString)'), self.single)
        self.connect(self.cmbrepo, SIGNAL('activated(QString)'), self.report)
        self.connect(self.cmbrepoc, SIGNAL('activated(QString)'), self.repo)         #Providing the link to ComboBox when ComboBox is pressed
#        self.connect(self.cmbrna, SIGNAL('activated(QString)'), self.crna)
#        self.connect(self.cmbrnap, SIGNAL('activated(QString)'), self.grna)
#        self.connect(self.cmbrnac, SIGNAL('activated(QString)'), self.rev)
#        self.connect(self.cmbc, SIGNAL('activated(QString)'), self.get)
        self.Execute.clicked.connect(self.onIndexChange1)
        self.back.clicked.connect(self.backframe)
        self.ok.clicked.connect(self.outpyes)
        self.bck.clicked.connect(self.bckframe)
        self.ret.clicked.connect(self.retr)
        self.bk.clicked.connect(self.bckr)
        self.okr.clicked.connect(self.okrr)
        self.true.clicked.connect(self.false)
        self.rawp.clicked.connect(self.raw)
        self.junc.clicked.connect(self.junction)
        self.stri += " " +"--library-type"+" "+"fr-unstranded"
        self.clos.clicked.connect(self.wrt)
        self.bkb.clicked.connect(self.asd)
        self.bkc.clicked.connect(self.rgt)
        self.clo.clicked.connect(self.eat)
       # self.clos.clicked.connect(self.ate)
        self.okg.clicked.connect(self.go)
        self.fileg.clicked.connect(self.frna)
        self.filer.clicked.connect(self.multir)
        self.filec.clicked.connect(self.rrna)
        self.fileb.clicked.connect(self.multipair2)
        self.filep.clicked.connect(self.prna)
        self.filea.clicked.connect(self.multipair1)
        self.yesali.clicked.connect(self.want)
        self.yespre.clicked.connect(self.preserve)
        self.yesso.clicked.connect(self.sort)
        self.nobam.clicked.connect(self.bam)
        self.nocon.clicked.connect(self.convert)       #Providing the link to Push Button when Push Button is pressed
#        self.yesqual.clicked.connect(self.ascii)


        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('valueChanged(int)'), self.changeText1)
        QtCore.QObject.connect(self.horizontalSlider_1, QtCore.SIGNAL('valueChanged(int)'), self.changeText2)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL('valueChanged(int)'), self.changeText3)  #Providing the link to Horizontal Slider
       # self.connect(self.comboBox_3, SIGNAL('activated(QString)'), self.runindex1)
      #  self.connect(self.celfilecom, SIGNAL('activated(QString)'), self.runindex)
        #self.connect(self.verticalScrollBar,SIGNA

    def runindex1(self):

        txt = self.comboBox_3.currentText()
        if txt == "Use a built-in genome":
            self.comboBox_4.show()
            self.celfile_2.hide()
            self.celfilecom.hide()
            mypath ="/home/amrata/PycharmProjects/builinfil"
            onlyfiles = [f for f in tuple(listdir(mypath)) ]
            self.comboBox_4.addItems((onlyfiles))
            self.connect(self.comboBox_4, SIGNAL('activated(QString)'), self.load)
        elif txt == "Use a genome from history":
            self.celfile_2.show()
            self.celfilecom.show()
            self.comboBox_4.hide()

    def load(self):
         pfil = self.comboBox_4.currentText()
         self.pfl = pfil
         str2= "."
         str1 = pfil.find(str2)
         print(str1)
         file =  pfil[:str1]
         self.file = file
         print(file)
         proc = subprocess.Popen(["cp -r /home/amrata/PycharmProjects/builinfil""+self.pfl+ /* "+" "+"/home/amrata/PycharmProjects/builinfil/bowtieuser" , ""],stdout=subprocess.PIPE, shell=True)
         (out, err) = proc.communicate()
         print(out)

    def runindex(self):
        file = self.celfilecom.currentText()
        self.connect(self.celfilecom,SIGNAL('activated(QString)'),self.filevent)
        #self.connect(self.selfilcom,SIGNAL('activated(QString)'),self.filevent1)

    def filevent(self):
            quit_msg = "if you want to Provide the File Name? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                text = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"),self.tr("File Name:"), QtGui.QLineEdit.Normal)
                fil = text[0]
                self.file = fil
                fil1=globals()
                file = self.celfilecom.currentText()
                proc = subprocess.Popen(["bowtie-build" + " "+ file + " "+ fil, ""],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                #self.selfilcom.addItems(str(out))

    def changeText1(self, value):
        if value:
            self.z1 = value
            self.iso.setText(str(self.z1))
        else:
            self.z1 = "0"

    def changeText2(self, value):
        if value:
            self.z1 = value
            self.dur.setText(str(self.z1))
        else:
            self.z1 = "22"

    def want(self):
        self.stri +=" "+"--no-mixed"+" "

    def preserve(self):
        self.stri +=" "+"--keep-tmp"+" "

    def sort(self):
        self.stri +=" "+"--keep-fasta-order"+" "

    def bam(self):
        self.stri +=" "+"--no-sort-bam"+" "

    def convert(self):
        self.stri +=" "+"--no-convert-bam"+" "

    def solexa(self):
         self.stri +=" "+"--solexa-quals"+" "

    def ascii(self):
         self.stri +=" "+"--integer-quals"+" "


    def changeText3(self, value):
        if value:
            self.z1 = (value)
            self.misnum.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def selectFile(self):
                    self.celfilecom.addItem(QtGui.QFileDialog.getOpenFileName())

    def frna(self):
        #It is used to select the fasta file for a single file in single-end.
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.cmbrna.addItem(self.fl)
                self.read = self.cmbrna.currentText()
                self.read1 = "-U"+" "+self.read

            else:                 #When user does not select FASTA file
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.frna()
        if not self.fl:            #When user does not select any file
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
    def multir(self):
        #It is used to set the fasta file for a multiple file in single-end.
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.cmbrna.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.cmbrna.count()
                    self.file3 = self.cmbrna.itemText(0)
                    self.file1 = self.cmbrna.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.cmbrna.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3

                    self.multir()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.cmbrna.count()
                    self.file3 = self.cmbrna.itemText(0)
                    self.file1 = self.cmbrna.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.cmbrna.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3

            else:                              #When user does not select FASTA file
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multir()
        else:
            quit_msg = "There is nothing to load"   #When user does not select any file
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)



    def prna(self):
        #It is used to set the fasta file for a single file in paired-end forward read.
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.cmbrnap.addItem(self.fl)
                self.readfl1 = self.cmbrnap.currentText()
                print(self.readfl1)
            else:                  #When user does not select fasta  file
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.prna()
        if not self.fl:             #When user does not select any file
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
    def multipair1(self):
        #It is used to set the fasta file for a multiple file in paired-end forward reads.
        self.fl= QtGui.QFileDialog.getOpenFileName()
        if self.fl:

            sta2 = ".fq"

            if sta2 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.cmbrnap.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num = self.cmbrnap.count()
                    self.file3 = self.cmbrnap.itemText(0)
                    self.file1 = self.cmbrnap.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbrnap.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl1 = self.file3
                    self.multipair1()
                elif reply == QtGui.QMessageBox.No:
                    num = self.cmbrnap.count()
                    self.file3 = self.cmbrnap.itemText(0)
                    self.file1 = self.cmbrnap.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbrnap.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl1 = self.file3
                else:                #When user does not select any fasta file
                    quit_msg = "Error! Please select the fasta file"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                    self.multipair1()
        else:                 #when user does not select any file
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)


    def rrna(self):
        #It is used to set the fasta file for a single file in paired-end reverse reads.
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".fq"

            if sta1 in self.fl:
                self.cmbrnac.addItem(self.fl)
                self.readfl2 = self.cmbrnac.currentText()
                print(self.readfl2)
            else:           #When user does not select FASTA file
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.rrna()
        if not self.fl:     #When user does not select any file
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def multipair2(self):
        #It is used to set the fasta file for a multiple file in paired-end reverse reads.
        self.fl= QtGui.QFileDialog.getOpenFileName()
        if self.fl:

            sta2 = ".fq"

            if sta2 in self.fl:
                quit_msg = "Do you want to select any other read file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.cmbrnac.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num = self.cmbrnac.count()
                    self.file3 = self.cmbrnac.itemText(0)
                    self.file1 = self.cmbrnac.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbrnac.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3
                    self.multipair2()
                elif reply == QtGui.QMessageBox.No:
                    num = self.cmbrnac.count()
                    self.file3 = self.cmbrnac.itemText(0)
                    self.file1 = self.cmbrnac.itemText(num)
                    for i in range(num - 1):
                        self.file2 = self.cmbrnac.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.readfl2 = self.file3



            else:               #When user does not select fasta file
                quit_msg = "Error! Please select the fasta file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.multipair2()
        else:                   #When user does not select any file
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)




   # def crna(self):
       #self.fil = self.cmbrna.currentText()

   ## self.fi = self.cmbrnap.currentText()

   # def rev(self):
       ### self.fil = self.fi +","+self.fip

    def onIndexChange(self):
                                      #It is used to set the position of comboBox of Default Settings or Full Parameter list.
                self.str1 = self.anal.currentText()
                if self.str1 == "2:Full parameter list":
                    self.pargp.show()
                    #self.frame.hide()
                   #self.grppair.hide()
                   # self.grpsin.hide()
                   # self.grpdef.hide()
                   # self.grpsp.setGeometry(QtCore.QRect(10, 1470, 841, 130))
                   # self.grppar.setGeometry(QtCore.QRect(10, 1510, 841, 130))
                    self.Execute.setGeometry(QtCore.QRect(560,2500,98,27))


                        #self.yesnext.show()
                       #self.parnext.hide()
                elif self.str1 == "1:Default settings only":
                    self.pargp.hide()
                   # self.grpsp.show()
                   # self.grppar.show()
                    #self.grpsp.setGeometry(QtCore.QRect(10, 80, 841, 130))
                    #self.grppar.setGeometry(QtCore.QRect(10, 150, 841, 130))
                    self.Execute.setGeometry(QtCore.QRect(560,300,98,27))



    def yesbow(self):
        if self.str1  == "Yes":
             self.stri += " " +"--bowtie-n"+" "
        else:
             self.stri1 = self.stri

    def align(self):                #Code to display the Tweak alignment option.
        self.txt1 = self.cmbali.currentText()
        if self.txt1 =="Yes":
           self.grpali.show()
           self.frame.hide()

    def score(self):             #Code to display the Tweak Scoring option.
        self.txt1 = self.cmbscr.currentText()
        if self.txt1 =="Yes":
           self.grpscr.show()
           self.frame.hide()

    def go(self):#Code to display the Tweak Effort option.
        self.txt1 = self.cmbeff.currentText()
        if self.txt1 =="Yes":
           self.grpeff.hide()
           self.frame.show()

    def wrt(self):
        self.grpscr.hide()
        self.frame.show()


    def asd(self):
        self.grppair.hide()
        self.frame.show()

    def eat(self):
        self.grpali.hide()
        self.frame.show()

    def rgt(self):
        self.grppairc.hide()
        self.frame.show()

    def effort(self):
        self.grpeff.show()
        self.frame.hide()


    def single(self):
                            #Code to display the option of Single-end and Paired-end
        txt = self.cmbsin.currentText()
        if txt == "Single-end":
           self.grpsin.show()
           self.pargp.hide()
           self.grppair.hide()
           self.grppairc.hide()
           self.grpdef.setGeometry(QtCore.QRect(00, 130, 841, 131))
           self.pargp.setGeometry(QtCore.QRect(0, 220, 841, 2531))
           self.Execute.setGeometry(QtCore.QRect(560,300 , 98, 27))
        elif txt == "Paired-end (as indiviual datasets)":
            self.grppair.show()
            self.frame.hide()
            self.grpsin.hide()
            self.grpdef.setGeometry(QtCore.QRect(00, 60, 841, 131))
            self.pargp.setGeometry(QtCore.QRect(0, 150, 841, 2531))
        elif txt == "Paired-end(as collection)":
            self.grppairc.show()
            self.frame.hide()
            self.grpsin.hide()
            self.grpdef.setGeometry(QtCore.QRect(00, 60, 841, 131))
            self.pargp.setGeometry(QtCore.QRect(0, 150, 841, 2531))


    def changeText(self, value):
        if value:
            self.z1 = (value)
            self.misnum.setText(str(self.z1))
        else:
            self.z1 = "0.1"

    def library(self):
                           #Code to select the Library Type.It takes 3 options
        self.txt = self.libtype.currentText()
        if self.txt == "fr-unstranded":
           self.stri += " " +"--library-type"+" "+"fr-unstranded"+" "
        elif self.txt == "fr-firststrand":
            self.stri += " " +"--library-type"+" "+"fr-firststrand"+" "
        elif self.txt == "fr-secondstrand":
            self.stri += " " +"--library-type"+" "+"fr-secondstrand"+" "

    def allowin(self):
        #it is used to set the "Allow Indel Search". when this comboBox is pressed it shows the option
        txt = self.cmballow.currentText()
        if txt == "Yes":
           self.grpallow.show()
           self.frame.hide()


    def supyes(self):
        #When this comboBox is pressed  will close the Supply Junction.
        self.grpsup.hide()
        self.frame.show()

    def supdata(self):
        #WWhen this comboBox is pressed 'Supply Junction Data' option will be displayed
        txt = self.cmbsup.currentText()
        if txt == "Yes":
            self.grpsup.show()
            self.frame.hide()



    def genean(self):
        #Code to display the option of Gene Annotation Model. It will allow the user to select GTF file
        txt1 = self.cmbgene.currentText()
        if txt1 == "Yes":
             self.grpgene.show()
             self.frame.hide()
             #self.grpsin.hide()
             self.grpraw.hide()

             self.grpuse.setGeometry(QtCore.QRect(10, 150, 841, 130))
             self.grplook.setGeometry(QtCore.QRect(10, 210, 841, 130))

        elif txt1 == "No":
             self.grpuse.show()
             self.grpgene.hide()
             self.grplook.show()

             self.grpuse.setGeometry(QtCore.QRect(10, 70, 841, 130))
             self.grplook.setGeometry(QtCore.QRect(10, 140, 841, 130))

    def rawjun(self):
        #Code to display the option of Raw Junction.It will allow the user to select Junction file
        txt1 = self.cmbraw.currentText()
        if txt1 == "Yes":
              self.grpraw.show()
              self.frame.hide()
              #self.grpsin.hide()
              self.grpraw.setGeometry(QtCore.QRect(10, 200, 841, 130))
              self.grplook.setGeometry(QtCore.QRect(10, 250, 841, 130))

        elif txt1 == "No":
              self.grpraw.hide()
              self.grplook.show()
              self.grplook.setGeometry(QtCore.QRect(10, 200, 841, 130))

    def raw(self):
        #Code to select the Gene Annotation file for a single file
        self.cmbgemo.addItem(QtGui.QFileDialog.getOpenFileName())
        self.temp = self.cmbgemo.currentText()
        if not self.temp:             #When user does not select the GTF file
          quit_msg = "Error! Please select the GTF file "
          reply = QtGui.QMessageBox.question(self, 'Message',
                                 quit_msg, QtGui.QMessageBox.Ok)

    def rjunc(self):
        #Code to select the Raw Junction file  for a single file
        self.cmbjunc.addItem(QtGui.QFileDialog.getOpenFileName())
        self.temp = self.cmbjunc.currentText()
        if not self.temp:
          quit_msg = "Error! Please select the Raw Junction file "
          reply = QtGui.QMessageBox.question(self, 'Message',
                                 quit_msg, QtGui.QMessageBox.Ok)

    def rawju(self):
        #Code for Gene Annotation Model
        txt = self.cmbgemo.currentText()
        self.stri +=" "+"-G"+" "+txt

    def junction(self):
        #Code for Raw Junction
        txt = self.cmbjunc.currentText()
        self.stri +=" "+"-j"+" "+txt

    def supjn(self):
        #Code for Novel junction
         self.stri +=" "+"--no-novel-juncs"+" "

    def report(self):
        txt = self.cmbrepo.currentText()
        if txt == "Yes":
           self.stri +=" "+"--no-discordant"+" "

    def repo(self):
        txt = self.cmbrepoc.currentText()
        if txt == "Yes":
           self.stri +=" "+"--no-discordant"+" "

    def cover(self):
                         #Code to display the option of  'Coverage Search'
        txt = self.cmbcov.currentText()
        if txt == "Yes":
           self.grpcov.show()
           self.frame.hide()
           self.stri +=" "+"--coverage-search"+" "
        elif txt == "No":
           self.stri +=" "+"--no-coverage-search"+" "

    def retr(self):
        self.grpfus.hide()
        self.frame.show()

    def micro(self):
        #the code for Microexon Search
        self.stri +=" "+"--microexon-search"+" "

    def fusion(self):
       #Code to display the option of  'Fusion Search'
        txt = self.cmbfus.currentText()
        if txt == "Yes":
           self.grpfus.show()
           self.frame.hide()



    def set(self):
        #Code to display the option of  'Bowtie Option'
        txt = self.cmbset.currentText()
        if txt == "Yes":
           self.grpset.show()
           self.frame.hide()

    def preset(self):
         #Code to display the option of  'preset Option'
        txt = self.cmbpre.currentText()
        if txt == "Yes":
           self.grpopt.show()
           self.frame.hide()


        elif txt == "No":
            self.grpopt.hide()

    def read(self):
        self.grpid.show()
        self.frame.hide()
        self.grpsp.hide()
        self.grppar.hide()


    def compute(self):
        txt = self.cmbjob.currentText()
        if txt == "Specify job resource parameters":
             self.grpcomp.show()
             self.frame.hide()
             self.grpsp.hide()
             self.grppar.hide()
        else:
            self.grpcomp.hide()

    def outpyes(self):
        self.grpallow.hide()
        self.frame.show()

    def backframe(self):
        self.grpsup.hide()
        self.frame.show()

    def bckframe(self):
        self.grpcov.hide()
        self.frame.show()

    def retr(self):
        self.grpfus.hide()
        self.frame.show()

    def bckr(self):
        self.grpset.hide()
        self.frame.show()
        self.grpopt.hide()

    def okrr(self):
        self.grpid.hide()
        self.frame.show()
        self.grpsp.show()
        self.grppar.hide()

    def false(self):
        self.grpcomp.hide()
        self.frame.show()
        self.grpsp.show()
        self.grppar.hide()


    def option(self):
        #It is the code to set the Preset option
        te = self.cmbopt.currentText()
        if te == "Very Fast":
            self.stri +=" "+"--b2-very-fast"+" "
        elif te == "Fast":
            self.stri +=" "+"--b2-fast"+" "
        elif te == "Sensitive":
            self.stri +=" "+"--b2-sensitive"+" "
        elif te == "Very Sensitive":
            self.stri +=" "+"--b2-very-sensitive"+" "


    def onIndexChange1(self):
              #This the main code to Execute the Tophat. Here, the code is written to set the default values.
                matep = self.mate.text()
                if matep:
                    self.stri += " "+"-r"+" "+matep
                    self.stri1 = self.stri
                else:
                    self.stri += " "+"-r"+" "+"50"
                    self.stri1 = self.stri
                devp = self.dev.text()
                if devp:
                    self.stri += " "+"--mate-std-dev"+" "+devp
                    self.stri1 = self.stri
                else:
                    self.stri += " "+"--mate-std-dev"+" "+"20"
                    self.stri1 = self.stri


                if self.str1  == "2:Full parameter list":
                                #It is used to Execute Tophat when user select the Full Parameter list. It will set default value
                     maxrep = self.maxre.text()
                     maxedit = self.maxed.text()

                     if maxrep:
                            self.stri += " "+"--read-realign-edit-dist"+" "+maxrep
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--read-realign-edit-dist"+" "+"3"
                            self.stri1 = self.stri



                     if maxedit:
                            self.stri += " "+"--read-edit-dist"+" "+maxedit
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--read-edit-dist"+" "+"2"
                            self.stri1 = self.stri
                     final = self.finalr.text()
                     if final:
                            self.stri += " "+"--read-mismatches"+" "+final
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--read-mismatches"+" "+"2"
                            self.stri1 = self.stri
                     anlen = self.anlen.text()
                     if anlen:
                            self.stri += " "+"-a"+" "+anlen
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"-a"+" "+"8"
                            self.stri1 = self.stri
                     maxnum = self.maxnu.text()
                     if maxnum:
                            self.stri += " "+"--splice-mismatches"+" "+maxnum
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--splice-mismatches"+" "+"0"
                            self.stri1 = self.stri
                     minintr = self.minin.text()
                     if minintr:
                            self.stri += " "+"-i"+" "+minintr
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"-i"+" "+"70"
                            self.stri1 = self.stri
                     maxintr = self.maxin.text()
                     if maxintr:
                            self.stri += " "+"-I"+" "+maxintr
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"-I"+" "+"500000"
                            self.stri1 = self.stri
                     maxinleng = self.maxinlen.text()
                     if maxinleng:
                            self.stri += " "+"--max-insertion-length"+" "+maxinleng
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--max-insertion-length"+" "+"3"
                            self.stri1 = self.stri
                     maxdelin = self.maxdel.text()
                     if maxdelin:
                            self.stri += " "+"--max-deletion-length"+" "+maxdelin
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--max-deletion-length"+" "+"3"
                            self.stri1 = self.stri
                     numallo = self.numal.text()
                     if numallo:
                            self.stri += " "+"-g"+" "+numallo
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"-g"+" "+"20"
                            self.stri1 = self.stri
                     spmini = self.spmin.text()
                     if spmini:
                            self.stri += " "+"--min-segment-intron"+" "+spmini
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--min-segment-intron"+" "+"50"
                            self.stri1 = self.stri
                     spmaxi = self.spmax.text()
                     if spmaxi:
                            self.stri += " "+"--max-segment-intron"+" "+spmaxi
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--max-segment-intron"+" "+"500000"
                            self.stri1 = self.stri
                     misnumb = self.misnum.text()
                     if misnumb:
                            self.stri += " "+"--segment-mismatches"+" "+misnumb
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--segment-mismatches"+" "+"2"
                            self.stri1 = self.stri
                     lenread = self.lenre.text()
                     if lenread:
                            self.stri += " "+"--segment-length"+" "+lenread
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--segment-length"+" "+"25"
                            self.stri1 = self.stri
                     mincov = self.covmin.text()
                     if mincov:
                            self.stri += " "+"--min-coverage-intron"+" "+mincov
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--min-coverage-intron"+" "+"50"
                            self.stri1 = self.stri
                     maxcov = self.covmax.text()
                     if maxcov:
                            self.stri += " "+"--max-coverage-intron"+" "+maxcov
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--max-coverage-intron"+" "+"20000"
                            self.stri1 = self.stri
                     lenanc = self.lenan.text()
                     if lenanc:
                            self.stri += " "+"--fusion-anchor-length"+" "+lenanc
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-anchor-length"+" "+"20"
                            self.stri1 = self.stri
                     mdista = self.mdis.text()
                     if mdista:
                            self.stri += " "+"--fusion-min-dist"+" "+mdista
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-min-dist"+" "+"10000000"
                            self.stri1 = self.stri
                     readmis = self.rmis.text()
                     if readmis:
                            self.stri += " "+"--fusion-read-mismatches"+" "+readmis
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-read-mismatches"+" "+"2"
                            self.stri1 = self.stri
                     mulre = self.mulr.text()
                     if mulre:
                            self.stri += " "+"--fusion-multireads"+" "+mulre
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-multireads"+" "+"2"
                            self.stri1 = self.stri
                     mulpa = self.mulp.text()
                     if mulpa:
                            self.stri += " "+"--fusion-multipairs"+" "+mulpa
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-multipairs"+" "+"2"
                            self.stri1 = self.stri
                     fusign = self.fusig.text()
                     if fusign:
                            self.stri += " "+"--fusion-ignore-chromosomes"+" "+fusign
                            self.stri1 = self.stri
                     else:
                            self.stri += " "+"--fusion-ignore-chromosomes"+" "+"0"
                            self.stri1 = self.stri

                     isop = self.iso.text()
                     if isop:
                         self.stri += " "+"--b2-N"+" "+isop
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-N"+" "+"0"
                         self.stri1 = self.stri
                     durp = self.dur.text()
                     if durp:
                         self.stri += " "+"--b2-L"+" "+durp
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-L"+" "+"20"
                         self.stri1 = self.stri
                     govp = self.gov.text()
                     if govp:
                         self.stri += " "+"--b2-i"+" "+govp
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-i"+" "+"S,1,1.25"
                         self.stri1 = self.stri
                     ambp = self.amb.text()
                     if ambp:
                         self.stri += " "+"--b2-n-ceil"+" "+ambp
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-n-ceil"+" "+"L,0,0.15"
                         self.stri1 = self.stri
                     gapp = self.gap.text()
                     if gapp:
                         self.stri += " "+"--b2-gbar"+" "+gapp
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-gbar"+" "+"4"
                         self.stri1 = self.stri
                     pens = self.pen.text()
                     if pens:
                         self.stri += " "+"--b2-mp"+" "+pens
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-mp"+" "+"6,2"
                         self.stri1 = self.stri
                     chas = self.cha.text()
                     if chas:
                         self.stri += " "+"--b2-np"+" "+chas
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-np"+" "+"6"
                         self.stri1 = self.stri
                     opes = self.ope.text()
                     if opes:
                         self.stri += " "+"--b2-rdg"+" "+opes
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-rdg"+" "+"5,3"
                         self.stri1 = self.stri
                     exes = self.exe.text()
                     if exes:
                         self.stri += " "+"--b2-rfg"+" "+exes
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-rfg"+" "+"5,3"
                         self.stri1 = self.stri
                     scrs = self.scr.text()
                     if scrs:
                         self.stri += " "+"--b2-score-min"+" "+scrs
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-score-min"+" "+"L,-0.6,-0.6"
                         self.stri1 = self.stri
                     seeds = self.seed.text()
                     if seeds:
                         self.stri += " "+"--b2-D"+" "+seeds
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-D"+" "+"15"
                         self.stri1 = self.stri
                     res = self.rese.text()
                     if res:
                         self.stri += " "+"--b2-R"+" "+res
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--b2-R"+" "+"2"
                         self.stri1 = self.stri
                     thread = self.the.text()
                     if thread:
                         self.stri += " "+"-p"+" "+thread
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"-p"+" "+"1"
                         self.stri1 = self.stri
                     gapre = self.gapr.text()
                     if gapre:
                         self.stri += " "+"--read-gap-length"+" "+gapre
                         self.stri1 = self.stri
                     else:
                         self.stri += " "+"--read-gap-length"+" "+"2"
                         self.stri1 = self.stri

                     self.opt = self.cmbsin.currentText()
                                        #It is used to Execute the tophat with single-end FASTA file
                     if self.opt=="Single-end":
                           if not self.fl == " ":   # Code for the Execution of Tophat
                              output = "tophat" + " " + self.stri1 + " " + self.file + " " + self.fl
                              fpt1 = open("bowtieout.pkl", "wb")
                              pickle.dump(str(output), fpt1, protocol=2)
                              fpt1.close()

                           elif self.fl == " ":
                               #It is the code for Single-end when the user does not select the FASTA file
                                    quit_msg = "You have not selected any read files Do you want to select the read files "
                                    reply = QtGui.QMessageBox.question(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Yes,
                                                                       QtGui.QMessageBox.No)
                                    if reply == QtGui.QMessageBox.Yes:
                                        self.frna()
                                    else:
                                        quit_msg = "Do you want to Quit from this "
                                        reply = QtGui.QMessageBox.question(self, 'Message',
                                                                           quit_msg, QtGui.QMessageBox.Yes,
                                                                           QtGui.QMessageBox.No)
                                        if reply == QtGui.QMessageBox.Yes:
                                            self.close()
                           if self.nofil == "No":  # code if we mot continue cufflink module when we want bowtie output olny
                               fptt1 = open("bowtieout.pkl", "rb")
                               self.bowtie = pickle.load(fptt1)
                               fptt1.close()
                               quit_msg = "Processing Please wait"
                               reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Default)
                               proc = subprocess.Popen([self.buildfile, ""], stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE,
                                                       shell=True)
                               (out, err) = proc.communicate()
                               print(self.buildfile)
                               print(err)
                               f = open("error1", "w")
                               f.write(str(err))
                               f.close()
                               f = open("error1", "r")
                               self.txt = f.read(5)
                               self.txt1 = f.read(10)
                               f.close()
                               if not self.txt1:  # checking for error
                                   quit_msg = "Successfully created"
                                   reply = QtGui.QMessageBox.information(self, 'Message',
                                                                         quit_msg, QtGui.QMessageBox.Ok)

                                   proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                                   (out, err) = proc.communicate()

                               elif self.txt1:  # if error is there
                                   quit_msg = "is not a valid reference file"
                                   reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                     quit_msg, QtGui.QMessageBox.Ok)
                                   self.txt = " "
                                   self.txt1 = " "

                           else:

                               # if self.cont =="yes" and not self.read== " ":
                               self.top = cuff.Cuffl(self)
                               self.top.closed.connect(self.show)
                               self.top.show()
                               self.close()

                     elif self.opt == "Paired-end (as indiviual datasets)":
                         #It is the code for Paired-end when the user does not select the FASTA file
                            if self.readfl1 ==" " and  self.readfl2== " ":   #When the user does not select FASTA file
                                quit_msg = "Please select the Read File "
                                reply = QtGui.QMessageBox.warning(self, 'warning',
                                                                  quit_msg, QtGui.QMessageBox.Ok)

                            else:
                                self.fl = " "+ self.readfl1 + " " + " "+ self.readfl2
                                output = "tophat" + " " + self.stri1 + " " + self.file + " " + self.fl
                                fpt1 = open("bowtieout.pkl", "wb")
                                pickle.dump(str(output), fpt1, protocol=2)
                                fpt1.close()

                            if self.nofil == "No":  # code if we mot continue cufflink module when we want bowtie output olny
                                    fptt1 = open("bowtieout.pkl", "rb")
                                    self.bowtie = pickle.load(fptt1)
                                    fptt1.close()
                                    quit_msg = "Processing Please wait"
                                    reply = QtGui.QMessageBox.question(self, 'Message', quit_msg,
                                                                       QtGui.QMessageBox.Default)
                                    proc = subprocess.Popen([self.buildfile, ""], stdout=subprocess.PIPE,
                                                            stderr=subprocess.PIPE,
                                                            shell=True)
                                    (out, err) = proc.communicate()
                                    print(self.buildfile)
                                    print(err)
                                    f = open("error1", "w")
                                    f.write(str(err))
                                    f.close()
                                    f = open("error1", "r")
                                    self.txt = f.read(5)
                                    self.txt1 = f.read(10)
                                    f.close()
                                    if not self.txt1:  # checking for error
                                        quit_msg = "Successfully created"
                                        reply = QtGui.QMessageBox.information(self, 'Message',
                                                                              quit_msg, QtGui.QMessageBox.Ok)

                                        proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                                        (out, err) = proc.communicate()

                                    elif self.txt1:  # if error is there
                                        quit_msg = "is not a valid reference file"
                                        reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                          quit_msg, QtGui.QMessageBox.Ok)
                                        self.txt = " "
                                        self.txt1 = " "

                            else:

                                    # if self.cont =="yes" and not self.read== " ":
                                    self.top = cuff.Cuffl(self)
                                    self.top.closed.connect(self.show)
                                    self.top.show()
                                    self.close()




                elif self.str1== "1:Default settings only":
                    #It is used to Execute Tophat when user select the Default Settings Only
                     self.opt = self.cmbsin.currentText()
                     if self.opt=="Single-end":
                          #It is used to Execute the tophat with single-end FASTA file
                           if not self.fl == " ":
                               output = "tophat" + " " + self.stri1 + " " + self.file + " " + self.fl
                               fpt1 = open("bowtieout.pkl", "wb")
                               pickle.dump(str(output), fpt1, protocol=2)
                               fpt1.close()


                           elif self.fl == " ":
                                  #It is the code for Single-end when the user does not select the FASTA file
                                quit_msg = "You have not selected any read files Do you want to select the read files "
                                reply = QtGui.QMessageBox.question(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Yes,
                                                                       QtGui.QMessageBox.No)
                                if reply == QtGui.QMessageBox.Yes:
                                   self.frna()
                                else:
                                   quit_msg = "Do you want to Quit from this "
                                   reply = QtGui.QMessageBox.question(self, 'Message',
                                                                           quit_msg, QtGui.QMessageBox.Yes,
                                                                           QtGui.QMessageBox.No)
                                   if reply == QtGui.QMessageBox.Yes:
                                        self.close()
                                if self.nofil == "No":  # code if we mot continue cufflink module when we want bowtie output olny
                                      fptt1 = open("bowtieout.pkl", "rb")
                                      self.bowtie = pickle.load(fptt1)
                                      fptt1.close()
                                      quit_msg = "Processing Please wait"
                                      reply = QtGui.QMessageBox.question(self, 'Message', quit_msg,
                                                                         QtGui.QMessageBox.Default)
                                      proc = subprocess.Popen([self.buildfile, ""], stdout=subprocess.PIPE,
                                                              stderr=subprocess.PIPE,
                                                              shell=True)
                                      (out, err) = proc.communicate()
                                      print(self.buildfile)
                                      print(err)
                                      f = open("error1", "w")
                                      f.write(str(err))
                                      f.close()
                                      f = open("error1", "r")
                                      self.txt = f.read(5)
                                      self.txt1 = f.read(10)
                                      f.close()
                                      if not self.txt1:  # checking for error
                                          quit_msg = "Successfully created"
                                          reply = QtGui.QMessageBox.information(self, 'Message',
                                                                                quit_msg, QtGui.QMessageBox.Ok)

                                          proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                                          (out, err) = proc.communicate()

                                      elif self.txt1:  # if error is there
                                          quit_msg = "is not a valid reference file"
                                          reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                            quit_msg, QtGui.QMessageBox.Ok)
                                          self.txt = " "
                                          self.txt1 = " "

                                else:

                                      # if self.cont =="yes" and not self.read== " ":
                                      self.top = cuff.Cuffl(self)
                                      self.top.closed.connect(self.show)
                                      self.top.show()
                                      self.close()


                     elif self.opt == "Paired-end (as indiviual datasets)":
                          #It is used to Execute the tophat with Paired-end FASTA file
                            if self.readfl1 ==" " and  self.readfl2== " ":
                                quit_msg = "Please select the Read File "
                                reply = QtGui.QMessageBox.warning(self, 'warning',
                                                                  quit_msg, QtGui.QMessageBox.Ok)

                            else:
                                self.fl = " "+ self.readfl1 + " " + " "+ self.readfl2
                                output = "tophat" + " " + self.stri1 + " " + self.file + " " + self.fl
                                fpt1 = open("bowtieout.pkl", "wb")
                                pickle.dump(str(output), fpt1, protocol=2)
                                fpt1.close()


                     if self.nofil == "No":  # code if we mot continue cufflink module when we want bowtie output olny
                        fptt1 = open("bowtieout.pkl", "rb")
                        self.bowtie = pickle.load(fptt1)
                        fptt1.close()
                        quit_msg = "Processing Please wait"
                        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.Default)
                        proc = subprocess.Popen([self.buildfile, ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                shell=True)
                        (out, err) = proc.communicate()
                        print(self.buildfile)
                        print(err)
                        f = open("error1", "w")
                        f.write(str(err))
                        f.close()
                        f = open("error1", "r")
                        self.txt = f.read(5)
                        self.txt1 = f.read(10)
                        f.close()
                        if not self.txt1:  # checking for error
                            quit_msg = "Successfully created"
                            reply = QtGui.QMessageBox.information(self, 'Message',
                                                                  quit_msg, QtGui.QMessageBox.Ok)

                            proc = subprocess.Popen([self.bowtie, ""], stdout=subprocess.PIPE, shell=True)
                            (out, err) = proc.communicate()

                        elif self.txt1:  # if error is there
                            quit_msg = "is not a valid reference file"
                            reply = QtGui.QMessageBox.warning(self, 'Message',
                                                              quit_msg, QtGui.QMessageBox.Ok)
                            self.txt = " "
                            self.txt1 = " "

                     else:

                        # if self.cont =="yes" and not self.read== " ":
                        self.top = cuff.Cuffl(self)
                        self.top.closed.connect(self.show)
                        self.top.show()
                        self.close()


def main():
	app=QtGui.QApplication(sys.argv)
	form=Top()
	form.show()
	app.exec_()

if __name__=="__main__":
	main()
