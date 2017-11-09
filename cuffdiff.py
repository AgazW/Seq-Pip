from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE
import cuffdiffgui
import cuff
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge

import subprocess
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import allignment
import pickle

#import images
from subprocess import call
import os


class Cuffdiff(QtGui.QMainWindow,cuffdiffgui.Ui_MainWindow):

    closed = QtCore.pyqtSignal()

    def __init__(self, parent=None): # initiazation and linking
        super(Cuffdiff, self).__init__( parent)
        self.setupUi(self)
        #self.frame.hide()
        self.frame1.hide()


        self.groupBox_4.hide()
        self.advancegrp.hide()
        self.valu = 0
        self.y =170
        self.string = " "
        self.time= " "
        self.lib = " "
        self.std= " "
        self.lib1 = " "
        self.mult= " "
        self.stringout= " "
        self.sam2= " "
        self.sam1=" "
        self.fl=" "
        self.outd=" "
        #self.advgrp.hide()
        self.connect(self.advcufoptcmb, SIGNAL('activated(QString)'), self.onIndexChange)
        self.connect(self.advcufoptcmb1, SIGNAL('activated(QString)'), self.onIndexChange2)
        self.connect(self.subrefcomb, SIGNAL('activated(QString)'), self.showscr)
        self.connect(self.dispcomb, SIGNAL('activated(QString)'), self.showscr1)
        #self.connect(self.refa#, SIGNAL('activated(QString)'), self.onIndexChange)
       # self.connect(self.biascmb, SIGNAL('activated(QString)'), self.onIndexChange2)
        #self.connect(self.seqcmb, SIGNAL('activated(QString)'), self.showscr)
        self.selfile.clicked.connect(self.selectFl)
        self.mulfile4.clicked.connect(self.multifile)
        self.mulfile.clicked.connect(self.multifilegtf)
        self.mulfile5.clicked.connect(self.multifile1)
        self.subrefanpushgrp1.clicked.connect(self.selectsamfile)
        self.subrefanpushgrp2.clicked.connect(self.selectsamorbamorcxb)
        self.mulfile1.clicked.connect(self.multisam)
        self.mulfile3.clicked.connect(self.multisamorbamorcxb)
        self.subrefanpushp.clicked.connect(self.addgroup)
        #self.connect(self.multireadcmb, SIGNAL('activated(QString)'), self.show1)
        #self.connect(self.multireadcmb1, SIGNAL('activated(QString)'), self.show2)
        self.connect(self.lengthcorcmb, SIGNAL('activated(QString)'), self.lengthc)
        self.connect(self.libinpcmb, SIGNAL('activated(QString)'), self.libfun)
        self.connect(self.maskcmb, SIGNAL('activated(QString)'), self.runindex1)
        self.connect(self.hitscmb, SIGNAL('activated(QString)'), self.compat)
        self.connect(self.inpcmb, SIGNAL('activated(QString)'), self.sambam)
        self.biaspus.clicked.connect(self.biasop)
        #self.subrefanpushgrp1.clicked.connect(self.sambamfile)
        #self.subrefanpushgrp2.clicked.connect(self.sambamfile1)
        self.subrefanpushok.clicked.connect(self.samok)
        self.subrefanpushp.clicked.connect(self.insertrep)
        self.diffno.clicked.connect(self.memo)
        self.isoyes.clicked.connect(self.memo1)
        self.suppyes.clicked.connect(self.memo2)
        self.servyes.clicked.connect(self.memo3)
        self.Poiyes.clicked.connect(self.memo4)
        self.tabyes.clicked.connect(self.memo5)


        self.printyes.clicked.connect(self.printop)
       # self.helpyes.clicked.connect(self.usage)

        self.asyes11.clicked.connect(self.onIndexChangeop)
        self.asno11.clicked.connect(self.onIndexChangeop1)
        self.yes1.clicked.connect(self.tim)
        self.no1.clicked.connect(self.tim1)
        self.execute.clicked.connect(self.executeop)


        self.ok.clicked.connect(self.okclicked)
         #self.string += " "+" --library-norm-method"+" "+"geometric"


    def onIndexChange(self): # code for showing advance option frame
        self.str1 = self.advcufoptcmb.currentText()
        if self.str1=="Yes":
            self.groupBox_4.show()
            self.advgrp.move(10,1070)
            self.execute.move(600,1350)
        else:
            self.groupBox_4.hide()
            self.advgrp.move(10,940)
            self.execute.move(600,1230)

    def biasop(self): # code for selectin reference anotation used fro bias correction
            self.fl = (QtGui.QFileDialog.getOpenFileName())
            if self.fl:
                sta1 = ".fa"

                if sta1 in self.fl:
                    self.biastxtcor.addItem(self.fl)
                    self.readfl2 = self.biastxtcor.currentText()
                    self.strin += " " + "-b" + " " + self.readfl2

                else:
                    quit_msg = "Error! Please select proper genome file"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                      quit_msg, QtGui.QMessageBox.Ok)
                    self.selectFl1()
            if not self.fl:
                quit_msg = "There is nothing to load"
                reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                  quit_msg, QtGui.QMessageBox.Ok)

    def printop(self): # for printing version
        self.string += " " + "--version" + " "

    def multifile(self): # code for selecting multiple reference annotations for bias correction
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

    def multifile1(self): # code for selectin multiple GTF files for Mask operations
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
                        self.msk = " " + "-M" + " " + self.file3
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
                        self.msk += " " + "-M" + " " + self.file3


                else:
                    quit_msg = "Error! Please select Proper Mask file(I,e file in the form of(gtf/gff)"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                      quit_msg, QtGui.QMessageBox.Ok)
                    self.multifile1()
            else:
                quit_msg = "There is nothing to load"
                reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                  quit_msg, QtGui.QMessageBox.Ok)



                #def usage(self):
        #self.string += " " + "-h" + " "

    def multifilegtf(self): # multiple GTF for Mask files
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".gtf"
            st1 = ".gff"

            if sta1 in self.fl or st1 in self.fl:
                quit_msg = "Do you want to select any other Mask file(press yes if you want)"
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

                    self.multifile1()

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
                self.multifile1()
        else:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)

    def selectsamfile(self): # code for selecting sam or bam files
            self.fl = QtGui.QFileDialog.getOpenFileName()
            if self.fl:
                sta1 = ".sam"
                sta2 =".bam"
                sta3= ".cxb"

                if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                    self.subrefcombgrp1.addItem(self.fl)
                    self.sam2 = self.subrefcombgrp1.currentText()
                else:
                    quit_msg = "Error! Please select proper file"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                      quit_msg, QtGui.QMessageBox.Ok)
                    self.selectsamfile()
            if not self.fl:
                quit_msg = "There is nothing to load"
                reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                  quit_msg, QtGui.QMessageBox.Ok)


# coe for selecting multiplt sam or bam or cxb files
    def multisam(self):
        self.fl = QtGui.QFileDialog.getOpenFileName()
        if self.fl:
            sta1 = ".sam"
            sta2 = ".bam"
            sta3 = ".cxb"

            if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                quit_msg = "Do you want to select any other file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.subrefcombgrp1.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.subrefcombgrp1.count()
                    self.file3 = self.subrefcombgrp1.itemText(0)
                    self.file1 = self.subrefcombgrp1.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcombgrp1.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam2 += " "  + self.file3
                    self.multisam()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.subrefcombgrp1.count()
                    self.file3 = self.subrefcombgrp1.itemText(0)
                    self.file1 = self.subrefcombgrp1.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcombgrp1.itemText(i + 1)
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

    def selectsamorbamorcxb(self): # code for select sam or bam or cxb
            self.fl = QtGui.QFileDialog.getOpenFileName()
            if self.fl:
                sta1 = ".sam"
                sta2 = ".bam"
                sta3 = ".cxb"
                if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                    self.subrefcombgrp2.addItem(self.fl)
                    self.sam1 = self.subrefcombgrp2.currentText()
                else:
                    quit_msg = "Error! Please select proper file"
                    reply = QtGui.QMessageBox.warning(self, 'Error',
                                                      quit_msg, QtGui.QMessageBox.Ok)
                    self.selectsamorbamorcxb()
            if not self.fl:
                quit_msg = "There is nothing to load"
                reply = QtGui.QMessageBox.warning(self, 'Warning',
                                                  quit_msg, QtGui.QMessageBox.Ok)

    def multisamorbamorcxb(self): # code for select multiplt sam or bam or cxb
        self.fl = QtGui.QFileDialog.getOpenFileName()

        if self.fl:
            sta1 = ".sam"
            sta2 = ".bam"
            sta3 = ".cxb"

            if sta1 in self.fl or sta2 in self.fl or sta3 in self.fl:
                quit_msg = "Do you want to select any other file(press yes if you want)"
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.subrefcombgrp2.addItem(self.fl)
                if reply == QtGui.QMessageBox.Yes:

                    num1 = self.subrefcombgrp2.count()
                    self.file3 = self.subrefcombgrp2.itemText(0)
                    self.file1 = self.subrefcombgrp2.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcombgrp2.itemText(i + 1)
                        self.file3 += "," + self.file2
                    self.file3 += self.file1
                    self.sam1 += " " + self.file3
                    self.multisamorbamorcxb()

                elif reply == QtGui.QMessageBox.No:
                    self.readfl2 = " "
                    num1 = self.subrefcombgrp2.count()
                    self.file3 = self.subrefcombgrp2.itemText(0)
                    self.file1 = self.subrefcombgrp2.itemText(num1)
                    for i in range(num1 - 1):
                        self.file2 = self.subrefcombgrp2.itemText(i + 1)
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

    def memo(self): # Don't generate differential analysis files

        self.string += " " + "--no-diff  " + " "

    def memo1(self): #Don't perform isoform switching tests
        self.string += " " + " --no-js-tests   " + " "

    def insertrep(self): # code for insert pushbutton which are in sam or bam options
        self.name = self.ovrtoltxt.text()
        self.name1= self.ovrtoltxt1.text()
        self.rep = self.subrefcombgrp1.currentText()
        self.rep1 = self.subrefcombgrp2.currentText()
        self.string += " "+"-L"+" "+self.name+","+self.name1+" "+self.rep+" "+self.rep1+" "
        print(self.string)
        self.ovrtoltxt.clear()
        self.ovrtoltxt1.clear()
        self.subrefcombgrp1.clear()
        self.subrefcombgrp2.clear()

    def samok(self):
        self.frame1.hide()
        self.frame.show()

    def sambam(self): # for showing frame 1
        self.sam = self.inpcmb.currentText()
        if self.sam == "SAM/BAM" or self.sam=="Cuffquant(CXB)":
            self.frame1.show()
            self.frame.hide()



    def memo2(self): #log-friendly quiet processing (no progress bar)
        self.string += " " + " -q" + " "

    def memo3(self): #do not contact server to check for update availability
        self.string += " " + "--no-update-check" + " "

    def memo4(self): #Deprecated, use --dispersion-method
        self.string += " " + " --poisson-dispersion " + " "

    def memo5(self): #print count tables used to fit overdispersion
        self.string += " " + "--emit-count-tables" + " "

    def addgroup(self):

        self.valu += 1
        self.y +=100
        self.frame1.show()


    def okclicked(self):
        self.advancegrp.hide()
        self.frame.show()

    def compat(self): # cod for hits
        self.com = self.hitscmb.currentText()
        if self.com == "Compatible Hits":
            self.string += " "+"--compatible-hits-norm"+" "+"True"
        else:
            self.string += " "+"--total-hits-norm"+" "+"True"


    def tim(self): # for setting time
        self.time= " "+"-T"+" "+"True"+" "

    def tim1(self):
        self.time= " "+"-T"+" "+"False"+" "

    def onIndexChange2(self):
        self.str2 = self.biascmb.currentText()
        if self.str2=="Yes":
            self.framesh.show()
            self.groupBox_3.show()

        else:
            self.framesh.hide()
            self.Execute.setGeometry(QtCore.QRect(650,1050, 98,27))
            #self.Execute.move(650,750)

    def selectFl(self): # select single GTF file
        self.fl = (QtGui.QFileDialog.getOpenFileName())
        if self.fl:
            sta1 = ".gtf"

            if sta1 in self.fl:
                self.builselcom.addItem(self.fl)
                self.string += " "+ self.builselcom.currentText()


            else:
                quit_msg = "Error! Please select proper file"
                reply = QtGui.QMessageBox.warning(self, 'Error',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                self.selectFl()
        if not self.fl:
            quit_msg = "There is nothing to load"
            reply = QtGui.QMessageBox.warning(self, 'Warning',
                                              quit_msg, QtGui.QMessageBox.Ok)


    def runindex1(self): # for mask file
        self.maskfil = self.maskcmb.currentText()

        self.string += " "+"-M"+" "+self.maskfil

    def libfun(self): # library func
        self.std = self.libinpcmb.currentText()
        if self.std:
            self.string += " "+"--library-type"+" "+self.std
        else:
            self.string += " "+"--library-type"+" "+"fr-unstranded"

    def lengthc(self): #length corection
        self.stc=self.lengthcorcmb.currentText()
        if self.stc == "Standard alength Correction":
            self.string += " "+"--no-effective-length-correction"+" "+"True"
        else:
            self.string += " "+"--no-effective-length-correction"+" "+"False"

        if self.stc== "No Length Correction at all (use raw counts)":
            self.string += " "+"--no-length-correction"+" "+"True"
        else:
            self.string += " "+"--no-length-correction"+" "+"False"


    def onIndexChangeop(self): # for multireads
        self.mult = " "+" -u"+" "+"True"+" "

    def onIndexChangeop1(self):
        self.mult = " "+" -u"+" "+"False"+" "


    def onIndexChange2(self): # for showing advance frame options
        self.str1 = self.advcufoptcmb1.currentText()
        if self.str1=="Yes":
            self.frame.hide()
            self.advancegrp.show()
        else:
            self.advancegrp.hide()
            self.frame.show()

    def showscr(self): # library norm option
        self.str1= self.subrefcomb.currentText()
        self.lib = " "+" --library-norm-method"+" "+self.str1+" "

    def showscr1(self): # for using dispersion
        self.str1= self.dispcomb.currentText()
        self.lib1= " "+" --dispersion-method"+" "+self.str1+" "

    def executeop(self): # for running cuffdiff module
        disc = self.faldtxt.text()
        algn = self.faldtxt1.text()
        frag = self.avgtxt.text()
        dev = self.intdiststddevtxt.text()
        mle = self.maxmletxt.text()
        numfrag = self.numtxt.text()
        maxfrag = self.maxtxt.text()
        asm = self.asamptxt.text()
        minrep = self.minreptxt.text()
        outd = self.outdirtxt.text()
        thrd = self.thrdtxt.text()
        idt = self.idtxt.text()
        skip = self.skiptxt.text()
        fra = self.fragentxsm.text()
        per = self.pergen.text()
        per1 = self.pergen_2.text()
        if per:
            self.string += " " + "--num-frag-assign-draws " + " " + per + " "
            self.stri1 = self.string
        else:
            self.string += " " + "--num-frag-assign-draws " + " " + "50" + " "
            self.stri1 = self.string
        if per1:
            self.string += " " + "--min-reps-for-js-test  " + " " + per1 + " "
            self.stri1 = self.string
        else:
            self.string += " " + "--min-reps-for-js-test  " + " " + "50" + " "
            self.stri1 = self.string
        if fra:
            self.string += " " + "--num-frag-count-draws " + " " + fra+ " "
            self.stri1 = self.string
        else:
            self.string += " " + "--num-frag-count-draws " + " " + "100" + " "
            self.stri1 = self.string
        if skip:
            self.string += " " + "--max-bundle-frags " + " " + skip + " "
            self.stri1 = self.string
        else:
            self.string += " " + "--max-bundle-frags " + " " + "1000000" + " "
            self.stri1 = self.string
        if idt:
            self.string += " " + " -L" + " " + idt + " "
            self.stri1 = self.string
        if thrd:
            self.string += " " + "-p" + " " + thrd + " "
            self.stri1 = self.string
        if outd:
            self.outd= outd
            self.string += " " + "-o" + " " + outd + " "
            self.stri1 = self.string
        else:
            self.outd = "/home/amrata/PycharmProjects/bowtieuser/defaultout"
            self.string += " " + "-o" + " " +"/home/amrata/PycharmProjects/bowtieuser/defaultout"
            self.stri1 = self.string

        if not self.time:
            self.string += " "+"-T"+" "+"False" + " "
            self.stri1 = self.string
        if not self.mult:
            self.string += " "+"-u"+" "+"False"+" "
            self.stri1 = self.string
        if not self.lib:
            self.string += " "+" --library-norm-method"+" "+"geometric"+" "
            self.stri1 = self.string
        if not self.lib1:
            self.string += " "+"--dispersion-method"+" "+"pooled"+" "
            self.stri1 = self.string
        if not self.std:
            self.string += " " + "--library-type" + " " + "fr-unstranded"
            self.stri1 = self.string
        if disc:
            self.string += " "+"--FDR"+" "+disc+" "
            self.stri1 = self.string
        else:
            self.string += " "+"--FDR"+" "+"0.05"+" "
            self.stri1 = self.string
        if algn:
            self.string += " "+"-c"+" "+algn+" "
            self.stri1 = self.string
        else:
            self.string += " "+"-c"+" "+"10"+" "
            self.stri1 = self.string
        if frag:
            self.string += " "+"-m"+" "+frag+" "
            self.stri1 = self.string
        else:
            self.string += " "+"-m"+" "+"200"+" "
            self.stri1 = self.string
        if dev:
            self.string += " "+"-s"+" "+dev+" "
            self.stri1 = self.string
        else:
            self.string += " "+"-s"+" "+"80"+" "
            self.stri1 = self.string
        if mle:
            self.string += " "+"--max-mle-iterations"+" "+ mle+" "
            self.stri1 = self.string
        else:
            self.string += " "+"--max-mle-iterations"+" "+"5000"+" "
            self.stri1 = self.string
        if numfrag:
            self.string += " "+"--num-frag-count-draws "+" "+ numfrag+" "
            self.stri1 = self.string
        else:
            self.string += " "+"--num-frag-count-draws "+" "+"100"+" "
            self.stri1 = self.string
        if maxfrag:
            self.string += " "+"--max-frag-multihits  "+" "+ maxfrag+" "
            self.stri1 = self.string
        else:
            self.string += " "+"--max-frag-multihits  "+" "+"500000"+" "
            self.stri1 = self.string
        if asm:
            self.string += " "+"--num-frag-assign-draws"+" "+ asm+" "
            self.stri1 = self.string
        else:
            self.string += " "+"--num-frag-assign-draws"+" "+"50"+" "
            self.stri1 = self.string
        if minrep:
            self.string += " "+" --min-reps-for-js-test"+" "+ minrep+" "
            self.stri1 = self.string
        else:
            self.string += " "+" --min-reps-for-js-test"+" "+"3"+" "
            self.stri1 = self.string
        if self.fl == " ":  # This is the code When the user does not select the GTF file
            quit_msg = "Please select the GTF File"
            reply = QtGui.QMessageBox.warning(self, 'warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
        if self.sam1 == " " or self.sam2 == " ":  # This is the code When the user does not select the SAM or BAM file
            quit_msg = "Please select the SAM or BAM file "
            reply = QtGui.QMessageBox.warning(self, 'warning',
                                              quit_msg, QtGui.QMessageBox.Ok)
        else:  # Execution of Cuffdiff
            quit_msg = "Processing Please wait"
            QtGui.QMessageBox.information(self, 'Message',quit_msg)

            proc = subprocess.Popen(["cuffdiff" +" "+ self.stri1 , ""],stdout=subprocess.PIPE, shell=True)
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
                reply3 = str(QtGui.QMessageBox.information(self, 'Message',
                                               quit_msg1, QtGui.QMessageBox.Ok))
                quit_msg1 = "if you want to See the  Output?  (Press Yes if you want)"
                reply3 = QtGui.QMessageBox.question(self, 'Message',
                                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply3 == QtGui.QMessageBox.Yes:
                    pd = QtGui.QFileDialog.getOpenFileNames(self, "output",self.outd)
                    for i in pd:
                        proc = subprocess.Popen(["gedit" + " " +i, ""], stdout=subprocess.PIPE, shell=True)
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
	form=Cuffdiff()
	form.show()
	app.exec_()


if __name__=="__main__":
	main()


