import sys
import csv
import pandas as pd
import pyqtgraph as pg
from gui import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore,QtGui,uic
import numpy as np    
from random import randint       
from threading import Timer

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.channel1.hide()
        self.ui.checkbox1.hide()
        self.ui.slider1.hide()   
        self.ui.channel2.hide()
        self.ui.checkbox2.hide()
        self.ui.slider2.hide()
        self.ui.channel3.hide()
        self.ui.checkbox3.hide()
        self.ui.slider3.hide()
        self.ui.channel4.hide()
        self.ui.checkbox4.hide()
        self.ui.slider4.hide()
        self.ui.channel5.hide()
        self.ui.checkbox5.hide()
        self.ui.slider5.hide()
        self.data1 = []
        self.time1 = []
        self.i_1 = 0
        self.data2 = []
        self.time2 = []
        self.i_2 = 0
        self.data3 = []
        self.time3 = []
        self.i_3 = 0
        self.data4 = []
        self.time4 = []
        self.i_4 = 0
        self.data5 = []
        self.time5 = []
        self.i_5 = 0
        self.p1=0
        self.p2=0
        self.p3=0
        self.p4=0
        self.p5=0
        self.f1 = 0 
        self.f2 = 0
        self.f3 =0 
        self.f4 = 0
        self.f5 =0
        self.g1 =0
        self.j1 =0
        self.k1 =0
        self.h1 =0
        self.g2 =0
        self.j2 =0
        self.k2 =0
        self.h2 =0
        self.g3 =0
        self.j3 =0
        self.k3 =0
        self.h3 =0
        self.g4 =0
        self.j4 =0
        self.k4 =0
        self.h4 =0
        self.g5 =0
        self.j5 =0
        self.k5 =0
        self.h5 =0
        self.z1=0
        self.z2=0
        self.z3=0
        self.z4=0
        self.z5=0
        self.i=0
        self.j=0
        self.ui.channel1.setXRange(0,5)
        self.ui.channel2.setXRange(0,5)
        self.ui.channel3.setXRange(0,5)    
        self.ui.channel4.setXRange(0,5)  
        self.ui.channel5.setXRange(0,5)  
        self.ui.actionChannel_1.triggered.connect(self.choose)
        self.ui.actionChannel_2.triggered.connect(self.choose2)
        self.ui.actionChannel_3.triggered.connect(self.choose3)
        self.ui.actionChannel_4.triggered.connect(self.choose4)
        self.ui.actionChannel_5.triggered.connect(self.choose5)
        self.ui.checkbox1.clicked.connect(self.flags1)
        self.ui.checkbox2.clicked.connect(self.flags2)
        self.ui.checkbox3.clicked.connect(self.flags3)
        self.ui.checkbox4.clicked.connect(self.flags4)
        self.ui.checkbox5.clicked.connect(self.flags5)
        self.ui.slider1.setMaximum(1)
        self.ui.slider1.setMinimum(0)
        self.pen1 = pg.mkPen(color=(255, 0, 0))
        self.pen2 = pg.mkPen(color=(0, 255, 0))
        self.pen3 = pg.mkPen(color=(0, 0, 255))
        self.pen4 = pg.mkPen(color=(100, 100, 100))
        self.pen5 = pg.mkPen(color=(150, 200, 25))
        self.ui.actionExit.triggered.connect(exit)
            
    def choose(self):
        self.f1 = 1
        self.getfiles()
    def choose2(self):
        self.f2 = 1
        self.getfiles2()
    def choose3(self):
        self.f3 = 1
        self.getfiles3()
    def choose4(self):
        self.f4 = 1
        self.getfiles4()  
    def choose5(self):
        self.f5 = 1
        self.getfiles5()          

    def getfiles(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*.xls);;(*.txt) ", options=options) 
        self.read_data(fname)  
    def getfiles2(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*.xls);;(*.txt) ", options=options) 
        self.read_data2(fname)
    def getfiles3(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*.xls);;(*.txt) ", options=options) 
        self.read_data3(fname)  
    def getfiles4(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*.xls);;(*.txt) ", options=options) 
        self.read_data4(fname)
    def getfiles5(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*.xls);;(*.txt) ", options=options) 
        self.read_data5(fname)               

    def read_data(self,fname):

        path = fname[0]
        

        if fname[1] == "(*.csv)":
            self.data1 = pd.read_csv(path)
            steptime = 0
            self.time1 = []
            for self.i in range (len(self.data1)):
                self.time1.append(steptime)
                steptime = steptime+ 0.001
            
        #convert data fram into list of lists
            dataset = self.data1.values.tolist()
        #convert list of list into list
            self.data1 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*.xls)":
            steptime = 0
            self.time1 = []
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data1 = pd.read_excel(open(path, 'rb'))
            for self.i in range (len(self.data)):
                self.time1.append(steptime)
                steptime = steptime+ 0.001
                
        #convert data fram into list of lists
            dataset = self.data1.values.tolist()
        #convert list of list into list
            self.data1 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
            steptime = 0
            self.time1 = []
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data1.append(float(str[0]))
                    self.time1.append(steptime)
                    steptime = steptime + 0.001
                 
        self.chan(self.time1,self.data1)             
    def read_data2(self,fname):

        path = fname[0]
        
        self.time2 = []
        if fname[1] == "(*.csv)":
            self.data2 = pd.read_csv(path)
            steptime = 0
            for self.i in range (len(self.data2)):
                self.time2.append(steptime)
                steptime = steptime+ 0.001
            
        #convert data fram into list of lists
            dataset = self.data2.values.tolist()
        #convert list of list into list
            self.data2 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*.xls)":
            steptime = 0
            self.time2 = []
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data2 = pd.read_excel(open(path, 'rb'))
            for self.i in range (len(self.data2)):
                self.time2.append(steptime)
                steptime = steptime+ 0.001
                
        #convert data fram into list of lists
            dataset = self.data2.values.tolist()
        #convert list of list into list
            self.data2 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
            steptime = 0
            self.time2 = []
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data2.append(float(str[0]))
                    self.time2.append(steptime)
                    steptime = steptime + 0.001                  
            

        self.chan2(self.time2,self.data2)
    def read_data3(self,fname):

        path = fname[0]
        self.time3 = []

        if fname[1] == "(*.csv)":
            self.data3 = pd.read_csv(path)
            steptime = 0
            for self.i in range (len(self.data3)):
                self.time3.append(steptime)
                steptime = steptime+ 0.001
            
        #convert data fram into list of lists
            dataset = self.data3.values.tolist()
        #convert list of list into list
            self.data3 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*.xls)":
            steptime = 0
            self.time3 = []

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data3 = pd.read_excel(open(path, 'rb'))
            for self.i in range (len(self.data3)):
                self.time3.append(steptime)
                steptime = steptime+ 0.001
                
        #convert data fram into list of lists
            dataset = self.data3.values.tolist()
        #convert list of list into list
            self.data3 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
            steptime = 0
            self.time3 = []
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data3.append(float(str[0]))
                    self.time3.append(steptime)
                    steptime = steptime + 0.001                  
            

        self.chan3(self.time3,self.data3)
    def read_data4(self,fname):

        path = fname[0]
        self.time4 = []
        

        if fname[1] == "(*.csv)":
            self.data4 = pd.read_csv(path)
            steptime = 0
            for self.i in range (len(self.data4)):
                self.time4.append(steptime)
                steptime = steptime+ 0.001
            
        #convert data fram into list of lists
            dataset = self.data4.values.tolist()
        #convert list of list into list
            self.data4 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*.xls)":
            steptime = 0
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data4 = pd.read_excel(open(path, 'rb'))
            for self.i in range (len(self.data4)):
                self.time4.append(steptime)
                steptime = steptime+ 0.001
                
        #convert data fram into list of lists
            dataset = self.data4.values.tolist()
        #convert list of list into list
            self.data4 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
            steptime = 0
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data4.append(float(str[0]))
                    self.time4.append(steptime)
                    steptime = steptime + 0.001                  
            

        self.chan4(self.time4,self.data4) 
    def read_data5(self,fname):

        path = fname[0]
        self.time5 = []

        if fname[1] == "(*.csv)":
            self.data5 = pd.read_csv(path)
            steptime = 0
            for self.i in range (len(self.data5)):
                self.time5.append(steptime)
                steptime = steptime+ 0.001
            
        #convert data fram into list of lists
            dataset = self.data5.values.tolist()
        #convert list of list into list
            self.data5 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*.xls)":
            steptime = 0
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data5 = pd.read_excel(open(path, 'rb'))
            for self.i in range (len(self.data5)):
                self.time5.append(steptime)
                steptime = steptime+ 0.001
                
        #convert data fram into list of lists
            dataset = self.data5.values.tolist()
        #convert list of list into list
            self.data5 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
            steptime = 0
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data5.append(float(str[0]))
                    self.time5.append(steptime)
                    steptime = steptime + 0.001                  
            

        self.chan5(self.time5,self.data5)       

    def chan (self,time,data):
        self.data_line =self.ui.channel1.plot(time, data,pen=self.pen1)
        self.ui.channel1.plotItem.getViewBox().setAutoPan(x=True)
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(10)
        self.timer1.timeout.connect(lambda:self.update_plot_data(self.data_line,time,data))
        self.timer1.start()
        self.ui.channel1.show()
        self.ui.checkbox1.show()
        self.ui.slider1.show()
        self.ui.slider1.valueChanged.connect(self.slider_1)
    def chan2 (self,time,data):
        self.data_line2 =self.ui.channel2.plot(time, data,pen=self.pen2)
        self.ui.channel2.plotItem.getViewBox().setAutoPan(x=True)
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(10)
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.data_line2,time,data))
        self.timer2.start()
        self.ui.channel2.show()
        self.ui.checkbox2.show()
        self.ui.slider2.show()
        self.ui.slider2.valueChanged.connect(self.slider_2)
    def chan3 (self,time,data):
        self.data_line3 =self.ui.channel3.plot(time, data,pen=self.pen3)
        self.ui.channel3.plotItem.getViewBox().setAutoPan(x=True)
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(10)
        self.timer3.timeout.connect(lambda:self.update_plot_data3(self.data_line3,time,data))
        self.timer3.start()
        self.ui.channel3.show()
        self.ui.checkbox3.show()
        self.ui.slider3.show()
        self.ui.slider3.valueChanged.connect(self.slider_3)
    def chan4 (self,time,data):
        self.data_line4 =self.ui.channel4.plot(time, data,pen=self.pen4)
        self.ui.channel4.plotItem.getViewBox().setAutoPan(x=True)
        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(10)
        self.timer4.timeout.connect(lambda:self.update_plot_data4(self.data_line4,time,data))
        self.timer4.start()
        self.ui.channel4.show()
        self.ui.checkbox4.show()
        self.ui.slider4.show() 
        self.ui.slider4.valueChanged.connect(self.slider_4)
    def chan5 (self,time,data):
        self.data_line5 =self.ui.channel5.plot(time, data,pen=self.pen5)
        self.ui.channel5.plotItem.getViewBox().setAutoPan(x=True)
        self.timer5 = QtCore.QTimer()
        self.timer5.setInterval(10)
        self.timer5.timeout.connect(lambda:self.update_plot_data5(self.data_line5,time,data))
        self.timer5.start()
        self.ui.channel5.show()
        self.ui.checkbox5.show()
        self.ui.slider5.show()
        self.ui.slider5.valueChanged.connect(self.slider_5)

    def update_plot_data(self,data_line,time,data):
        x = time[0:self.i_1]  # Add a new value 1 higher than the last.
            # self.datalist = self.datalist[1:]  # Remove the first 
        y = data[0:self.i_1]  # Add a new random value.
        self.i_1 = self.i_1 +1 
        data_line.setData(x, y)   
    def update_plot_data2(self,data_line,time,data):
        x = time[0:self.i_2]  # Add a new value 1 higher than the last.
            # self.datalist = self.datalist[1:]  # Remove the first 
        y = data[0:self.i_2]  # Add a new random value.
        self.i_2 = self.i_2 +1 
        data_line.setData(x, y) 
    def update_plot_data3(self,data_line,time,data):
        x = time[0:self.i_3]  # Add a new value 1 higher than the last.
            # self.datalist = self.datalist[1:]  # Remove the first 
        y = data[0:self.i_3]  # Add a new random value.
        self.i_3 = self.i_3 +1 
        data_line.setData(x, y)
    def update_plot_data4(self,data_line,time,data):
        x = time[0:self.i_4]  # Add a new value 1 higher than the last.
            # self.datalist = self.datalist[1:]  # Remove the first 
        y = data[0:self.i_4]  # Add a new random value.
        self.i_4 = self.i_4 +1 
        data_line.setData(x, y)
    def update_plot_data5(self,data_line,time,data):
        x = time[0:self.i_5]  # Add a new value 1 higher than the last.
            # self.datalist = self.datalist[1:]  # Remove the first 
        y = data[0:self.i_5]  # Add a new random value.
        self.i_5 = self.i_5 +1 
        data_line.setData(x, y)                    
    
    def flags1 (self):
        self.j1 = 0
        self.k1 = 0
        
        if self.ui.checkbox1.isChecked() == True :
            self.g1 = 0
            
            if self.z1 == 0:
                self.z1 = 1 
                self.control1()
            elif self.z1 == 1:
                self.control1()      
        elif self.ui.checkbox1.isChecked() == False :
            self.z1 = 0  
            self.discontrol1()
    def flags2 (self):
        self.k2 = 0
        self.f2 = 0
        if self.ui.checkbox2.isChecked():
            if self.z2 == 0:
                self.z2 = 1 
                self.control2()
            elif self.z2 == 1:
                self.control2()  
            
        elif self.ui.checkbox2.isChecked() == False :
            self.z2 = 0  
            self.discontrol2() 
    def flags3 (self):
        self.j3 = 0
        self.k3 = 0
        if self.ui.checkbox3.isChecked():
            if self.z3 == 0:
                self.z3 = 1 
                self.control3()
            elif self.z3 == 1:
                self.control3()  
        elif self.ui.checkbox3.isChecked() == False :
            self.z3 = 0  
            self.discontrol3()
    def flags4 (self):
        self.j4 = 0
        self.k3 = 0
        if self.ui.checkbox4.isChecked():
            if self.z4 == 0:
                self.z4 = 1 
                self.control4()
            elif self.z4 == 1:
                self.control4()  
        elif self.ui.checkbox4.isChecked() == False :
            self.z4 = 0  
            self.discontrol4
    def flags5 (self):
        self.k5 = 0
        self.j5 = 0
        if self.ui.checkbox5.isChecked():
            if self.z5 == 0:
                self.z5 = 1 
                self.control5()
            elif self.z5 == 1:
                self.control5()  
        elif self.ui.checkbox5.isChecked() == False :
            self.z5 = 0  
            self.discontrol5()                              
    
    def control1 (self):
        self.ui.play.clicked.connect(self.timer1.start)
        self.ui.pause.clicked.connect(self.timer1.stop)
        self.ui.delete_2.clicked.connect(self.clear1)
        self.ui.zoomin.clicked.connect(self.zoomin1)
        self.ui.zoomout.clicked.connect(self.zoomout1)  

    def control2 (self):
        self.ui.play.clicked.connect(self.timer2.start)
        self.ui.pause.clicked.connect(self.timer2.stop)
        self.ui.delete_2.clicked.connect(self.clear2)
        self.ui.zoomin.clicked.connect(self.zoomin2)
        self.ui.zoomout.clicked.connect(self.zoomout2)
    def control3 (self):
        self.ui.play.clicked.connect(self.timer3.start)
        self.ui.pause.clicked.connect(self.timer3.stop)
        self.ui.delete_2.clicked.connect(self.clear3)
        self.ui.zoomin.clicked.connect(self.zoomin3)
        self.ui.zoomout.clicked.connect(self.zoomout3)
    def control4 (self):
        self.ui.play.clicked.connect(self.timer4.start)
        self.ui.pause.clicked.connect(self.timer4.stop)
        self.ui.delete_2.clicked.connect(self.clear4)
        self.ui.zoomin.clicked.connect(self.zoomin4)
        self.ui.zoomout.clicked.connect(self.zoomout4)
    def control5 (self):
        self.ui.play.clicked.connect(self.timer5.start)
        self.ui.pause.clicked.connect(self.timer5.stop)
        self.ui.delete_2.clicked.connect(self.clear5)
        self.ui.zoomin.clicked.connect(self.zoomin5)
        self.ui.zoomout.clicked.connect(self.zoomout5)                 
    
    def discontrol1 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect() 

    def discontrol2 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect()

    def discontrol3 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect()

    def discontrol4 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect( )
    def discontrol5 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect() 
         
    def zoomin1 (self):
        self.g1 = self.g1 + 1
        if (self.h1 == 0):

            self.k1 = 5-self.g1 *0.1
        else:
            self.k1 = self.h1 - self.g1 *0.1
        self.k1 =  5 - self.g1 * 0.1
        self.ui.channel1.setXRange(0,self.k1)


    def zoomin2 (self):
        self.g2 = self.g2+1
        if (self.h2 == 0):

            self.k2 = 5-self.g2 *0.1
        else:
            self.k2 = self.h2 - self.g2 *0.1
       
        self.ui.channel2.setXRange(0,self.k2)

    def zoomin3 (self):
        self.g3 = self.g3+1
        if (self.h3 == 0):

            self.k3 = 5-self.g3 *0.1
        else:
            self.k3 = self.h3 - self.g3 *0.1
       
        self.ui.channel3.setXRange(0,self.k3)
    
    def zoomin4 (self):
        self.g4 = self.g4+1
        if (self.h4 == 0):

            self.k4 = 5-self.g4 *0.1
        else:
            self.k4 = self.h4 - self.g4 *0.1
       
        self.ui.channel4.setXRange(0,self.k4)
    
    def zoomin5 (self):
        self.g5 = self.g5+1
        if (self.h5 == 0):

            self.k5 = 5-self.g5 *0.1
        else:
            self.k5 = self.h5 - self.g5 *0.1
        self.ui.channel5.setXRange(0,self.k5)                
          
    def zoomout1 (self):
        self.j1 = self.j1+1
        if self.k1 == 0 :
            self.h1 = 5+self.j1 *0.1
        else:
            self.h1 = self.k1 + self.j1 * 0.1

        self.ui.channel1.setXRange(0,self.h1)
        
    def zoomout2 (self):
        self.j2 = self.j2+1
        if self.k2 == 0 :
            self.h2 =5+self.j2 *0.1
        else:
            self.h2 = self.k2 + self.j2 * 0.1
     
        self.ui.channel2.setXRange(0,self.h2)

    def zoomout3 (self):
        self.j3 = self.j3+1
        if self.k3 == 0 :
            self.h3 = 5+self.j3 *0.1
        else:
            self.h3 = self.k3 + self.j3* 0.1

        self.ui.channel3.setXRange(0,self.h3)


    def zoomout4 (self):
        self.j4 = self.j4+1
        if self.k4 == 0 :
            self.h4 = 5 +self.j4 *0.1
        else:
            self.h4 = self.k4 + self.j4 * 0.1
        
        self.ui.channel4.setXRange(0,self.h4)
    def zoomout5 (self):
        self.j5 = self.j5+1
        if self.k5 == 0 :
            self.h5 = 5+self.j5 *0.1
        else:
            self.h5 = self.k5 + self.j5 * 0.1
      
        self.ui.channel5.setXRange(0,self.h5)

    def clear1 (self):
        self.ui.channel1.clear()
        self.data1 = []
        data1 = self.data1
        self.time1 = []
        time1 = self.time1
        self.i_1 =0
        self.i=0
        self.j=0
        self.ui.channel1.hide()
        self.ui.slider1.hide()
        self.ui.checkbox1.hide()
        self.f1 = 0
        self.timer1 = None  
        self.ui.checkbox1.setChecked(False)  

    def clear2 (self):
        self.ui.channel2.clear()
        self.data2 = []
        self.time2 = []
        self.i_2 =0
        self.i=0
        self.j=0
        self.ui.channel2.hide()
        self.ui.slider2.hide()
        self.ui.checkbox2.hide()
        self.timer2 = None  
        self.ui.checkbox2.setChecked(False)   
    def clear3 (self):
        self.ui.channel3.clear()
        self.data3 = []
        self.time3 = []
        self.i_3 =0
        self.i=0
        self.j=0
        self.ui.channel3.hide()
        self.ui.slider3.hide()
        self.ui.checkbox3.hide()
        self.f3 = 0
        self.timer3 = None
        self.ui.checkbox3.setChecked(False)

    def clear4 (self):
        self.ui.channel4.clear()
        self.data4 = []
        self.time4 = []
        self.i_4 =0
        self.i=0
        self.j=0
        self.ui.channel4.hide()
        self.ui.slider4.hide()
        self.ui.checkbox4.hide()
        self.f4 = 0
        self.timer4 = None
        self.ui.checkbox4.setChecked(False)

    def clear5 (self):
        self.ui.channel5.clear()
        self.data5 = []
        self.time5 = []
        self.i_5 =0
        self.i=0
        self.j=0
        self.ui.channel5.hide()
        self.ui.slider5.hide()
        self.ui.checkbox5.hide()
        self.f5 = 0
        self.timer5 = None
        self.ui.checkbox5.setChecked(False)

    def slider_1(self):
            pos= self.ui.slider1.value()
            self.ui.channel1.setXRange(pos-5,pos)
            self.ui.slider1.setMaximum(14+self.p1)    
    def slider_2(self):
            pos= self.ui.slider2.value()
            self.ui.channel2.setXRange(pos-5,pos)
            self.ui.slider2.setMaximum(14+self.p2)
    def slider_3(self):
            pos= self.ui.slider3.value()
            self.ui.channel3.setXRange(pos-5,pos)
            self.ui.slider3.setMaximum(14+self.p3)
    def slider_4(self):
            pos= self.ui.slider4.value()
            self.ui.channel4.setXRange(pos-5,pos)
            self.ui.slider4.setMaximum(14+self.p4)
    def slider_5(self):
            pos= self.ui.slider5.value()
            self.ui.channel5.setXRange(pos-5,pos)
            self.ui.slider5.setMaximum(14+self.p5)        
                                                     
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() 
    window.show()
    sys.exit(app.exec_())