from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys
from os import listdir
from os.path import isfile, join
import mainwindow
import subprocess
import bowt
import tophat
from subprocess import Popen, PIPE
import cuff
import cuffquant
import cuffdiff
import cuffcompare
import cuffnorm
import cuffmerge
import pickle



from subprocess import call
import os




class Mainp(QtGui.QMainWindow,mainwindow.Ui_MainWindow):

    def __init__(self,out="", parent=None ):
        super(Mainp, self).__init__(parent)
        self.setupUi(self) # code for initializing all the necessary variable.
        self.option = " "
        self.out = out
        self.align =" "
        self.file=" "


        self.cuff = " "
        self.txt = " "
        self.txt1=" "
        self.frame.hide()
        self.algnoption.hide()
        self.builselcom.hide()
        self.selfilebuil.hide()

        self.frame_2.hide()
        self.connect(self.createind, SIGNAL('activated(QString)'), self.runindex1) # link the runindex1
       # self.connect(self.selfilcom, SIGNAL('activated(QString)'), self.runindex)
        self.selfile.clicked.connect(self.selectFile)
        self.mulfile.clicked.connect(self.selectFile1)
        self.selfilebuil.clicked.connect(self.selectFile2)

        self.bowtie.clicked.connect(self.onIndexChange1) # link onIndexChange1 function
        self.tophat.clicked.connect(self.onIndexChange2)
        self.cuffyes.clicked.connect(self.onIndexChange3)
        self.cuffno.clicked.connect(self.onIndexChange4)
        self.genind.clicked.connect(self.genindop)
        self.allignment.clicked.connect(self.allignmentop)  # link allignmentop function
        self.cufflinks.clicked.connect(self.cufflinksop)
        self.CuffCompare.clicked.connect(self.CuffCompareop)
        self.cuffdif.clicked.connect(self.Cuffdiffop)
        self.cuffquant.clicked.connect(self.Cuffquantop)
        self.Cuffnorm.clicked.connect(self.Cuffnormop)
        self.Cuffmerge.clicked.connect(self.Cuffmergeop)
       # self.C.clicked.connect(self.onIndexChange4)


    def selectFile(self): #code for selecting reference genome file
        self.selfilcom.addItem(QtGui.QFileDialog.getOpenFileName())
        self.file = self.selfilcom.currentText()
        if not self.file:
            quit_msg = "Error! Please select and load the file first"
            reply = QtGui.QMessageBox.warning(self, 'Error',
                                               quit_msg, QtGui.QMessageBox.Ok)
        else:
            st = ".fa"
            st1 = ".fasta" # check whether tha submitted file will be in this format or not.
            st2 =".mfa"
            st3 = ".fna"
            st4=".txt"
            st5 =".zip"
            if st in self.file or st1 in self.file or st2 in self.file or st3 in self.file or st4 in self.file or st5 in self.file:

                    quit_msg = "if you want to Provide the File Name? (Press Yes if you want)"
                    reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                    if reply == QtGui.QMessageBox.Yes:
                        text = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"), self.tr("File Name:"),
                                                  QtGui.QLineEdit.Normal)
                        fil = text[0]
                        self.out = fil
                        file = self.selfilcom.currentText()
                    # imag = QtGui.QPixmap("")
                        build = "bowtie2-build" + " " +"-f"+" "+ file + " " + fil # command for execution to create index

                        fpt = open("build.pkl", "wb") # create file and store the build variable value in this file.
                        pickle.dump(str(build), fpt, protocol=2)
                        fpt.close()
                    # proc = subprocess.Popen(["bowtie2-build" + " "+ file + " "+ fil, ""],stdout=subprocess.PIPE, shell=True)
                    # (out, err) = proc.communicate()
                        print(self.out)
                        outfile = self.out
                        fp = open("shared.pkl", "wb")  # containe the output file name this file will be used futher modules
                        pickle.dump(str(outfile), fp, protocol=2)
                        fp.close()
                        quit_msg = "Do you want to Continue? (Press Yes if you want)"
                        reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                        if reply == QtGui.QMessageBox.Yes:
                            self.align = "No"

                            self.algnoption.show()
                        else:

                            quit_msg = "Processing Please wait"
                            reply = QtGui.QMessageBox.information(self, 'Message',
                                                       quit_msg, QtGui.QMessageBox.Ok)

                            proc = subprocess.Popen([build, ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                            (out, err) = proc.communicate()

                            f = open("error", "w") # file that writes the error message
                            f.write(str(err))
                            f.close()
                            f = open("error", "r")
                            self.txt = f.read(5)
                            self.txt1 = f.read(10) # contains error message till that possition
                            f.close()



                            if not self.txt1: # if not error occure
                                quit_msg = "Successfully created"
                                reply = QtGui.QMessageBox.information(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Ok)
                                self.close()
                            elif self.txt1: # if error is there
                                quit_msg = "is not a valid reference file"
                                reply = QtGui.QMessageBox.warning(self, 'Message',
                                                          quit_msg, QtGui.QMessageBox.Ok)
                                self.txt = " "
                                self.txt1 = " "
                                self.selfilcom.clear()
            else:
                    quit_msg = "Please select Fasta format files only"
                    reply = QtGui.QMessageBox.warning(self, 'Message',
                                                  quit_msg, QtGui.QMessageBox.Ok)
                    self.selfilcom.clear()

    def selectFile1(self): # code for selecting multiple files
        #self.selfilcom.addItem(QtGui.QFileDialog.getOpenFileName())
        self.file3 = (QtGui.QFileDialog.getOpenFileName())
        num = self.selfilcom.count()
        self.file = self.selfilcom.itemText(0)
        self.file1 = self.selfilcom.itemText(num)
        for i in range(num-1):

            self.file2 = self.selfilcom.itemText(i+1)
            self.file += ","+self.file2
        self.file += self.file1
        if not self.file3:
            quit_msg = "Error! Please select and load the file first"
            reply = QtGui.QMessageBox.warning(self, 'Error',
                                              quit_msg, QtGui.QMessageBox.Ok)
        else:
            st = ".fa"
            st1 = ".fasta"
            st2 = ".mfa"
            st3 = ".fna"
            st4 = ".txt"

            if st in self.file3 or st1 in self.file3 or st2 in self.file3 or st3 in self.file3 or st4 in self.file3:

                    quit_msg = "Do you want to select any other file(press yes if you want)"
                    reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.Yes:

                        self.selfilcom.addItem(self.file3)
                        self.selectFile1()


                    elif reply == QtGui.QMessageBox.No:

                        quit_msg = "if you want to Provide the File Name? (Press Yes if you want)"
                        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                        if reply == QtGui.QMessageBox.Yes:
                            text = QtGui.QInputDialog.getText(self, self.tr("QInputDialog"), self.tr("File Name:"),
                                              QtGui.QLineEdit.Normal)
                            fil = text[0]
                            self.out = fil
                #file = self.selfilcom.currentText()
            # imag = QtGui.QPixmap("")
                            build = "bowtie2-build" + " " + self.file + " " + fil

                            fpt = open("build.pkl", "wb")
                            pickle.dump(str(build), fpt, protocol=2)
                            fpt.close()
            # proc = subprocess.Popen(["bowtie2-build" + " "+ file + " "+ fil, ""],stdout=subprocess.PIPE, shell=True)
            # (out, err) = proc.communicate()
            # print(self.out)
                        outfile = self.out
                        fp = open("shared.pkl", "wb")
                        pickle.dump(str(outfile), fp, protocol=2)
                        fp.close()
                        quit_msg = "Do you want to Continue? (Press Yes if you want)"
                        reply = QtGui.QMessageBox.question(self, 'Message',
                                           quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                        if reply == QtGui.QMessageBox.Yes:
                            self.align = "No"

                            self.algnoption.show()
                        else:

                             quit_msg = "Processing Please wait"
                             reply = QtGui.QMessageBox.information(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Ok)

                             proc = subprocess.Popen([build, ""], stdout=subprocess.PIPE, shell=True)
                             (out, err) = proc.communicate()
                             f = open("error", "w")
                             f.write(str(err))
                             f.close()
                             f = open("error", "r")
                             self.txt = f.read(5)
                             self.txt1 = f.read(10)
                             f.close()

                             print(proc)

                             if not self.txt1:
                                 quit_msg = "Successfully created"
                                 reply = QtGui.QMessageBox.information(self, 'Message',
                                                                       quit_msg, QtGui.QMessageBox.Ok)
                                 self.close()
                             elif self.txt1:
                                 quit_msg = "is not a valid reference file"
                                 reply = QtGui.QMessageBox.warning(self, 'Message',
                                                                   quit_msg, QtGui.QMessageBox.Ok)
                                 self.txt = " "
                                 self.txt1 = " "
                                 self.selfilcom.clear()

                                 self.close()
            else:
                    quit_msg = "Please select Fasta format files only"
                    reply = QtGui.QMessageBox.warning(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Ok)

                    self.selectFile1()



    def selectFile2(self):  # code for adding builtin files implementation code is there below
        self.builselcom.addItem(QtGui.QFileDialog.getOpenFileName())



    def CuffCompareop(self):# for showing cuffcompare module
        top = cuffcompare.Cuffcomp(self)
        top.closed.connect(self.show)
        top.show()


    def Cuffnormop(self):# for showing cuffnorm module
        top = cuffnorm.Cuffnorm(self)
        top.closed.connect(self.show)
        top.show()

    def Cuffdiffop(self):# for showing cuffdiff module
        top = cuffdiff.Cuffdiff(self)
        top.closed.connect(self.show)
        top.show()


    def Cuffquantop(self):# for showing cuffquant module
        top = cuffquant.Cuffq(self)
        top.closed.connect(self.show)
        top.show()


    def Cuffmergeop(self):# for showing cuffmerge module
        top = cuffmerge.Cuffm(self)
        top.closed.connect(self.show)
        top.show()




    def cufflinksop(self): # code for cuffflink options
        quit_msg = "Please Select the already alligned SAM / BAM sorted file? (Press Yes if you want)"
        reply = QtGui.QMessageBox.question(self, 'Message',
                                 quit_msg, QtGui.QMessageBox.Ok) # for selecting sam files
        if reply == QtGui.QMessageBox.Ok:
             read = QtGui.QFileDialog.getOpenFileName(self,"pick a file")

             fp2 = open("sharedcufffile.pkl","wb") # file for storing SAM filename
             pickle.dump(str(read), fp2,protocol=2)
             fp2.close()

             filg = "Yes"
             fp1w = open("filegen.pkl","wb") # file that used for directly start from cufflink option only(it doesnot run Bowtie 2 module)
             pickle.dump(str(filg), fp1w,protocol=2)

             fp1w.close()
             top1 = cuff.Cuffl(self)
             top1.closed.connect(self.show)
             top1.show()# to show cufflink module
             #self.close()






    def allignmentop(self): # to show alignment options ( it will show only alignment frame)
        self.scrollArea.hide()
        self.scrollArea_2.hide()
        #self.frame_2.show()
        self.frame.show()
        self.selfile.hide()
        self.mulfile.hide()
        self.createind.hide()
        self.selfilcom.hide()
        self.builselcom.hide()
        self.label_7.hide()
        self.label_5.hide()
        self.align="Yes"

        self.algnoption.show()

    def genindop(self): # code for generate index option
        self.scrollArea.hide()
        self.scrollArea_2.hide()
        self.frame.show()

    def onIndexChange1(self):# code for alignment option (directly start form alignment option)
        if self.align == "Yes":

            quit_msg = "Please Select the already created index File? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                                 quit_msg, QtGui.QMessageBox.Ok)
            if reply == QtGui.QMessageBox.Ok:
                read = str(QtGui.QFileDialog.getOpenFileName(self,"pick a file"))
                self.pfl = read
                str6= ".1.bt2"
                str7 =".2.bt2"
                str4 = ".3.bt2"
                str5 = ".4.bt2"
                str3 =".rev.1.bt2"
                str2 =".rev.2.bt2"
                if str2 in read: # chaeck wheter the file is in this format or not
                    str1 =read.index(str2)
                    file = read[:str1]
                elif str3 in read:
                    str1 = read.index(str3)
                    file = read[:str1]
                elif str4 in read:
                    str1 = read.index(str4)
                    file = read[:str1]
                elif str5 in read:
                    str1 = read.index(str5)
                    file = read[:str1]
                elif str6 in read:
                    str1 = read.index(str6)
                    file = read[:str1]
                elif str7 in read:
                    str1 = read.index(str7)
                    file = read[:str1]
                fp = open("shared.pkl","wb") # store the file name in thsi file
                pickle.dump(str(file), fp, protocol=2)
                fp.close()
            self.option= "bowtie"
            option = "bowtie"
            fp1w = open("file.pkl","wb") # file that indicate this is from bowtie module
            pickle.dump(str(option), fp1w,protocol=2)

            fp1w.close()


            quit_msg1 = "if you want to See the Output of Bowtie?  (Press Yes if you want)"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply3 == QtGui.QMessageBox.Yes:
                cfile="yes"
                fp1 = open("botout.pkl","wb") # file that containe yes for seeing bowtie output
                pickle.dump(str(cfile), fp1,protocol=2)

                fp1.close()
            elif reply3 == QtGui.QMessageBox.No:
                cfile="no"
                fp1 = open("botout.pkl","wb")# file that containe no for seeing bowtie output
                pickle.dump(str(cfile), fp1,protocol=2)

                fp1.close()
            quit_msg = "Do you want to Continue to use cufflinks? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
            quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                    option1 = "Yes"
                    fp1w1 = open("nocont.pkl","wb")# file that containe yes for continue to using cufflinks
                    pickle.dump(str(option1), fp1w1,protocol=2)
                    fp1w1.close()
                    self.frame_2.show()
            else:

                    option1 = "No"
                    fp1w = open("nocont.pkl","wb") # file that containe no for continue to using cufflinks
                    pickle.dump(str(option1), fp1w,protocol=2)
                    fp1w.close()
                    top = bowt.Bowt(self)
                    top.closed.connect(self.show)
                    top.show()


        elif self.align == "No": # code that is not diectly start from alignment it start from creating index file.
            self.option= "bowtie"
            option = "bowtie"
            fp1w = open("file.pkl","wb") #file ondicating bowtie module
            pickle.dump(str(option), fp1w,protocol=2)

            fp1w.close()
            quit_msg1 = "if you want to See the Output of Bowtie?  (Press Yes if you want)"
            reply3 = QtGui.QMessageBox.question(self, 'Message',
                            quit_msg1, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply3 == QtGui.QMessageBox.Yes:
                cfile="yes"
                fp1 = open("botout.pkl","wb") # file that containe yes for seeing bowtie output
                pickle.dump(str(cfile), fp1,protocol=2)

                fp1.close()
            elif reply3 == QtGui.QMessageBox.No:
                cfile="no"
                fp1 = open("botout.pkl","wb") # file that containe no for seeing bowtie output
                pickle.dump(str(cfile), fp1,protocol=2)

                fp1.close()
            quit_msg = "Do you want to Continue to use cufflinks? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                    option1 = "Yes"
                    fp1w1 = open("nocont.pkl","wb")  # file that containe yes for continue to using cufflinks
                    pickle.dump(str(option1), fp1w1,protocol=2)
                    fp1w1.close()
                    self.frame_2.show()
            else:

                    option1 = "No"
                    fp1w = open("nocont.pkl","wb")  # file that containe no for continue to using cufflinks
                    pickle.dump(str(option1), fp1w,protocol=2)
                    fp1w.close()
                    top = bowt.Bowt(self)
                    top.closed.connect(self.show)
                    top.show()




    def onIndexChange2(self):

        if self.align == "Yes":
            quit_msg = "Please Select the already created index File? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.read = str(QtGui.QFileDialog.getOpenFileName(self, "pick a file"))
                self.pfl = self.read
                str6 = ".1.bt2"
                str7 = ".2.bt2"
                str4 = ".3.bt2"
                str5 = ".4.bt2"
                str3 = ".rev.1.bt2"
                str2 = ".rev.2.bt2"
                if str2 in self.read:
                    str1 = self.read.index(str2)
                    file = self.read[:str1]
                elif str3 in self.read:
                    str1 = self.read.index(str3)
                    file = self.read[:str1]
                elif str4 in self.read:
                    str1 = self.read.index(str4)
                    file = self.read[:str1]
                elif str5 in self.read:
                    str1 = self.read.index(str5)
                    file = self.read[:str1]
                elif str6 in self.read:
                    str1 = self.read.index(str6)
                    file = self.read[:str1]
                elif str7 in self.read:
                    str1 = self.read.index(str7)
                    file = self.read[:str1]

                fp = open("shared.pkl", "wb")
                pickle.dump(str(file), fp, protocol=2)
                fp.close()
            self.option = "tophat"
            option = "tophat"
            fp1w = open("file.pkl", "wb")
            pickle.dump(str(option), fp1w, protocol=2)

            fp1w.close()
            cfile = "no"
            fp1 = open("botout.pkl", "wb")
            pickle.dump(str(cfile), fp1, protocol=2)

            fp1.close()
            quit_msg = "Do you want to Continue? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                option1 = "Yes"
                fp1w1 = open("nocont.pkl", "wb")
                pickle.dump(str(option1), fp1w1, protocol=2)
                fp1w1.close()
                self.frame_2.show()
            else:
                option1 = "No"
                fp1w1 = open("nocont.pkl", "wb")
                pickle.dump(str(option1), fp1w1, protocol=2)
                fp1w1.close()
                top = tophat.Top(self)
                #top.closed.connect(self.show)
                top.show()


        elif self.align == "No":
            self.option = "tophat"
            option = "tophat"
            fp1w = open("file.pkl", "wb")
            pickle.dump(str(option), fp1w, protocol=2)

            fp1w.close()

            cfile = "no"
            fp1 = open("botout.pkl", "wb")
            pickle.dump(str(cfile), fp1, protocol=2)

            fp1.close()
            quit_msg = "Do you want to Continue? (Press Yes if you want)"
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                option1 = "Yes"
                fp1w1 = open("nocont.pkl", "wb")
                pickle.dump(str(option1), fp1w1, protocol=2)
                fp1w1.close()
                self.frame_2.show()
            else:
                option1 = "No"
                fp1w1 = open("nocont.pkl", "wb")
                pickle.dump(str(option1), fp1w1, protocol=2)
                fp1w1.close()
                top = tophat.Top(self)
                top.closed.connect(self.show)
                top.show()


    def onIndexChange3(self): # code for cufflinks for continuation but not directly start from cufflink
        self.cuff ="yes"
        cfile = self.cuff
        fp1 = open("nocont.pkl","wb")
        pickle.dump(str(cfile), fp1,protocol=2)
        print(cfile)
        fp1.close()
        filg = "No"
        fp1w = open("filegen.pkl","wb")
        pickle.dump(str(filg), fp1w,protocol=2)

        fp1w.close()

        if self.option == "bowtie":
            top = bowt.Bowt(self)
            top.closed.connect(self.show)
            top.show()

            #.file = self.file
            self.hide()
        elif self.option == "tophat":
            top = tophat.Top(self)
            top.closed.connect(self.show)
            top.show()

            fp1 = open("nocont.pkl","wb")
            pickle.dump(str(cfile), fp1,protocol=2)
            print(cfile)
            fp1.close()

    def onIndexChange4(self): # code for cufflink no module
        self.cuff = "no"
        fp = open("nocont.pkl","wb")
        pickle.dump(str(self.cuff), fp,protocol=2)
        fp.close()
        if self.option == "bowtie":
            top = bowt.Bowt(self)
            
            top.show()

        elif self.option == "tophat":
            top = tophat.Top(self)
           
            top.show()






    def runindex1(self): # code for use builtin index or create reference genome

        txt = self.createind.currentText()
        if txt == "Use a built-in genome index":
            self.builselcom.show()
            self.selfilebuil.show()

            self.selfile.hide()
            self.mulfile.hide()
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

    def load(self): # code for loading built-in index file for our project
         pfil = str(self.builselcom.currentText())
         self.pfl = pfil
         str2= ".bt2"
         print(type(str2))
         print(type(pfil))
         print(pfil)
         str1 = pfil.find(str2)

         file =  pfil[:str1]
         self.file = file
         print(file)
         copyfil ="cp -r /home/amrata/PycharmProjects/builinfil/"+self.pfl+ "/* "+" "+"/home/amrata/PycharmProjects/bowtieuser"
        # proc = subprocess.Popen(["cp -r /home/amrata/PycharmProjects/builinfil/"+self.pfl+ "/* "+" "+"/home/amrata/PycharmProjects/bowtieuser" , ""],stdout=subprocess.PIPE, shell=True)
         #(out, err) = proc.communicate()
         filet=open("build.pkl","wb")
         pickle.dump(str(copyfil),filet,protocol=2)
         filet.close()
         outfile= self.file
         fp = open("shared.pkl","wb")
         pickle.dump(str(outfile), fp , protocol=2)

         self.algnoption.show()
         self.align = "No"





def main():
	app=QtGui.QApplication(sys.argv)
	form=Mainp()
	form.show()
	app.exec_()

if __name__=="__main__":
	main()

