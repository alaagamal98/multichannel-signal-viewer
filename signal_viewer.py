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
                #iterations for Updating

        self.data1 = []
        self.i_1 = 0
        self.data2 = []
      
        self.i_2 = 0
        self.data3 = []
    
        self.i_3 = 0
        self.data4 = []
       
        self.i_4 = 0
        self.data5 = []
       
        self.i_5 = 0
        #Slider
        self.p1=0
        self.p2=0
        self.p3=0
        self.p4=0
        self.p5=0
        #Flags
        self.f1 = 0 
        self.f2 = 0
        self.f3 =0 
        self.f4 = 0
        self.f5 =0

        #Zooming
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

        #Checkboxs
        self.z1=0
        self.z2=0
        self.z3=0
        self.z4=0
        self.z5=0

        #Read Data iterations
        self.i=0
        self.j=0


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
    
        self.pen1 = pg.mkPen(color=(255, 0, 0))
        self.pen2 = pg.mkPen(color=(0, 255, 0))
        self.pen3 = pg.mkPen(color=(0, 0, 255))
        self.pen4 = pg.mkPen(color=(100, 100, 100))
        self.pen5 = pg.mkPen(color=(150, 200, 25))
        self.ui.actionExit.triggered.connect(exit)
            
    def choose(self):
        if self.f1==0:
            self.f1 = 1
       
            self.getfiles()
    def choose2(self):
        if self.f2==0:
            self.f2 = 1
            self.getfiles2()
    def choose3(self):
        if self.f3==0:
            self.f3 = 1
            self.getfiles3()
    def choose4(self):
        if self.f4==0:
            self.f4 = 1
            self.getfiles4()  
    def choose5(self):
        if self.f5==0:
            self.f5 = 1
            self.getfiles5()          

    def getfiles(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*xlsx);;(*.txt) ", options=options) 

        if(fname[0]!=''):
            self.read_data(fname) 
        else:
            pass 
    def getfiles2(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*xlsx);;(*.txt) ", options=options) 
        if(fname[0]!=''):
            self.read_data2(fname) 
        else:
            pass 
    def getfiles3(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*xlsx);;(*.txt) ", options=options) 
        if(fname[0]!=''):
            self.read_data3(fname) 
        else:
            pass 
    def getfiles4(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*xlsx);;(*.txt) ", options=options)
        if(fname[0]!=''):
            self.read_data4(fname) 
        else:
            pass 
    def getfiles5(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ;;(*xlsx);;(*.txt) ", options=options) 
        if(fname[0]!=''):
            self.read_data5(fname) 
        else:
            pass               

    def read_data(self,fname):

       
      

        path = fname[0]

        if fname[1] == "(*.csv)":
            self.data1 = pd.read_csv(path)           
        #convert data frame into list of lists
            dataset = self.data1.values.tolist()
        #convert list of list into list
            self.data1 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*xlsx)":
         
            
            self.data1 = pd.read_excel(open(path, 'rb'))
           
        #convert data frame into list of lists
            dataset = self.data1.values.tolist()
        #convert list of list into list
            self.data1 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
          
          
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data1.append(float(str[0]))
                   
                 
        self.chan(self.data1)             
    def read_data2(self,fname):

        path = fname[0]
        
       
        if fname[1] == "(*.csv)":
            self.data2 = pd.read_csv(path)
    
          
        #convert data fram into list of lists
            dataset = self.data2.values.tolist()
        #convert list of list into list
            self.data2 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*xlsx)":
          
        
            self.data2 = pd.read_excel(open(path, 'rb'))
        
        #convert data fram into list of lists
            dataset = self.data2.values.tolist()
        #convert list of list into list
            self.data2 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
        
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data2.append(float(str[0]))
        self.chan2(self.data2)    
                            
    def read_data3(self,fname):

        path = fname[0]
   

        if fname[1] == "(*.csv)":
            self.data3 = pd.read_csv(path)
          
        #convert data fram into list of lists
            dataset = self.data3.values.tolist()
        #convert list of list into list
            self.data3 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*xlsx)":
            self.data3 = pd.read_excel(open(path, 'rb'))
          
        #convert data fram into list of lists
            dataset = self.data3.values.tolist()
        #convert list of list into list
            self.data3 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
         
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")       
                    self.data3.append(float(str[0]))

        self.chan3(self.data3)
    def read_data4(self,fname):

        path = fname[0]
      

        if fname[1] == "(*.csv)":
            self.data4 = pd.read_csv(path)
           
        #convert data fram into list of lists
            dataset = self.data4.values.tolist()
        #convert list of list into list
            self.data4 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*xlsx)":
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data4 = pd.read_excel(open(path, 'rb'))
           
        #convert data fram into list of lists
            dataset = self.data4.values.tolist()
        #convert list of list into list
            self.data4 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
           
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data4.append(float(str[0]))
                               
            

        self.chan4(self.data4) 
    def read_data5(self,fname):

        path = fname[0]
       
       

        if fname[1] == "(*.csv)":
            self.data5 = pd.read_csv(path)
           
        #convert data fram into list of lists
            dataset = self.data5.values.tolist()
        #convert list of list into list
            self.data5 = [self.j for self.i in dataset for self.j in self.i]
        
    
        elif fname[1] == "(*xlsx)":
            

            # df = read_excel(file_name, sheet_name = )f file") 
        
            self.data5 = pd.read_excel(open(path, 'rb'))
            
        #convert data fram into list of lists
            dataset = self.data5.values.tolist()
        #convert list of list into list
            self.data5 = [self.j for self.i in dataset for self.j in self.i]
            
        

        else:
            # data = open(path, "r").read()
           
            with open(path) as fileobject:
                for line in fileobject:
                    str = line.split("\n")
                    self.data5.append(float(str[0]))
                  

        self.chan5(self.data5)       

    def chan (self,data):
     
        self.data_line =self.ui.channel1.plot(data,pen=self.pen1)
        self.ui.channel1.plotItem.getViewBox().setAutoPan(x=True)
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(10)
        self.timer1.timeout.connect(lambda:self.update_plot_data(self.data_line,data))
        self.timer1.start()
        self.ui.channel1.show()

        self.ui.checkbox1.show()
        self.ui.slider1.show()
        self.ui.slider1.valueChanged.connect(self.slider_1)
        self.ui.channel1.setXRange(0,0.03*len(data))
    def chan2 (self,data):
        self.data_line2 =self.ui.channel2.plot(data,pen=self.pen2)
        self.ui.channel2.plotItem.getViewBox().setAutoPan(x=True)
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(10)
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.data_line2,data))
        self.timer2.start()
        self.ui.channel2.show()
        self.ui.checkbox2.show()
        self.ui.slider2.show()
        self.ui.slider2.valueChanged.connect(self.slider_2)
        self.ui.channel2.setXRange(0,0.03*len(data))
    def chan3 (self,data):
        self.data_line3 =self.ui.channel3.plot( data,pen=self.pen3)
        self.ui.channel3.plotItem.getViewBox().setAutoPan(x=True)
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(10)
        self.timer3.timeout.connect(lambda:self.update_plot_data3(self.data_line3,data))
        self.timer3.start()
        self.ui.channel3.show()
        self.ui.checkbox3.show()
        self.ui.slider3.show()
        self.ui.slider3.valueChanged.connect(self.slider_3)
        self.ui.channel3.setXRange(0,0.03*len(data))
    def chan4 (self,data):
        self.data_line4 =self.ui.channel4.plot( data,pen=self.pen4)
        self.ui.channel4.plotItem.getViewBox().setAutoPan(x=True)
        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(10)
        self.timer4.timeout.connect(lambda:self.update_plot_data4(self.data_line4,data))
        self.timer4.start()
        self.ui.channel4.show()
        self.ui.checkbox4.show()
        self.ui.slider4.show() 
        self.ui.slider4.valueChanged.connect(self.slider_4)
        self.ui.channel4.setXRange(0,0.03*len(data))
    def chan5 (self,data):
        self.data_line5 =self.ui.channel5.plot(data,pen=self.pen5)
        self.ui.channel5.plotItem.getViewBox().setAutoPan(x=True)
        self.timer5 = QtCore.QTimer()
        self.timer5.setInterval(10)
        self.timer5.timeout.connect(lambda:self.update_plot_data5(self.data_line5,data))
        self.timer5.start()
        self.ui.channel5.show()
        self.ui.checkbox5.show()
        self.ui.slider5.show()
        self.ui.slider5.valueChanged.connect(self.slider_5)
        self.ui.channel5.setXRange(0,0.03*len(data))


    def update_plot_data(self,data_line,data):
       
        y = data[0:self.i_1]  # Add a new random value.
        self.i_1 = self.i_1 +1 
        data_line.setData(y)   

    def update_plot_data2(self,data_line,data):
        
        y = data[0:self.i_2]  # Add a new random value.
        self.i_2 = self.i_2 +1 
        data_line.setData( y) 
    def update_plot_data3(self,data_line,data):
     
        y = data[0:self.i_3]  # Add a new random value.
        self.i_3 = self.i_3 +1 
        data_line.setData(y)
    def update_plot_data4(self,data_line,data):
     
        y = data[0:self.i_4]  # Add a new random value.
        self.i_4 = self.i_4 +1 
        data_line.setData(y)
    def update_plot_data5(self,data_line,data):
     
        y = data[0:self.i_5]  # Add a new random value.
    
        data_line.setData(y) 
        self.i_5 = self.i_5 +1               
    
    def flags1 (self):
 
        if self.ui.checkbox1.isChecked() == True :
          
            
            self.z1 = 1 
            self.control1()
     
        elif self.ui.checkbox1.isChecked() == False :
            self.z1 = 0  
            self.discontrol1()
    def flags2 (self):

        if self.ui.checkbox2.isChecked():
            self.z2 = 1 
            self.control2()
 
            
        elif self.ui.checkbox2.isChecked() == False :
            self.z2 = 0  
            self.discontrol2() 
    def flags3 (self):
 
        if self.ui.checkbox3.isChecked():
            self.z3 = 1 
            self.control3()
      
        elif self.ui.checkbox3.isChecked() == False :
            self.z3 = 0  
            self.discontrol3()
    def flags4 (self):
 
        if self.ui.checkbox4.isChecked():
           
            self.z4 = 1 
            self.control4()
           
        elif self.ui.checkbox4.isChecked() == False :
            self.z4 = 0  
            self.discontrol4()
    def flags5 (self):
     
        if self.ui.checkbox5.isChecked():
            self.z5 = 1 
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
        self.ui.zoomout.clicked.disconnect()
    def discontrol5 (self):
        self.ui.play.clicked.disconnect()
        self.ui.pause.clicked.disconnect()
        self.ui.delete_2.clicked.disconnect()
        self.ui.zoomin.clicked.disconnect()
        self.ui.zoomout.clicked.disconnect() 
         
    def zoomin1 (self):
        self.g1 = self.g1 + 100
        if (self.h1 == 0):

            self.k1 = 4000-self.g1 *0.5
        else:
            self.k1 = self.h1 - self.g1 *0.5
        self.ui.channel1.setXRange(0,self.k1)


    def zoomin2 (self):
        self.g2 = self.g2+100
        if (self.h2 == 0):

            self.k2 = 4000-self.g2 *0.5
        else:
            self.k2 = self.h2 - self.g2 *0.5
       
        self.ui.channel2.setXRange(0,self.k2)

    def zoomin3 (self):
        self.g3 = self.g3+100
        if (self.h3 == 0):

            self.k3 = 4000-self.g3 *0.5
        else:
            self.k3 = self.h3 - self.g3 *0.5
       
        self.ui.channel3.setXRange(0,self.k3)
    
    def zoomin4 (self):
        self.g4 = self.g4+100
        if (self.h4 == 0):

            self.k4 = 4000-self.g4 *0.5
        else:
            self.k4 = self.h4 - self.g4 *0.5
       
        self.ui.channel4.setXRange(0,self.k4)
    
    def zoomin5 (self):
        self.g5 = self.g5+100
        if (self.h5 == 0):

            self.k5 = 4000-self.g5 *0.5
        else:
            self.k5 = self.h5 - self.g5 *0.5
        self.ui.channel5.setXRange(0,self.k5)                
          
    def zoomout1 (self):
        self.j1 = self.j1+100
        if self.k1 == 0 :
            self.h1 = 4000+self.j1 *0.5
        else:
            self.h1 = self.k1 + self.j1 * 0.5

        self.ui.channel1.setXRange(0,self.h1)
        
    def zoomout2 (self):
        self.j2 = self.j2+100
        if self.k2 == 0 :
            self.h2 =4000+self.j2 *0.5
        else:
            self.h2 = self.k2 + self.j2 * 0.5
     
        self.ui.channel2.setXRange(0,self.h2)

    def zoomout3 (self):
        self.j3 = self.j3+100
        if self.k3 == 0 :
            self.h3 = 4000+self.j3 *0.5
        else:
            self.h3 = self.k3 + self.j3* 0.5

        self.ui.channel3.setXRange(0,self.h3)


    def zoomout4 (self):
        self.j4 = self.j4+100
        if self.k4 == 0:
            self.h4 = 4000 +self.j4 *0.5
        else:
            self.h4 = self.k4 + self.j4 * 0.5
        
        self.ui.channel4.setXRange(0,self.h4)
    def zoomout5 (self):
        self.j5 = self.j5+100
        if self.k5 == 0 :
            self.h5 = 4000+self.j5 *0.5
        else:
            self.h5 = self.k5 + self.j5 * 0.5
      
        self.ui.channel5.setXRange(0,self.h5)

    def clear1 (self):
        self.ui.channel1.clear()
        self.data1 = []
       

        self.i_1 =0

        self.ui.channel1.hide()
        self.ui.slider1.hide()
        self.ui.checkbox1.hide()
        self.f1 = 0
        self.timer1 = None  
        self.ui.checkbox1.setChecked(False)  
        self.z1 = 0  

    def clear2 (self):
        self.ui.channel2.clear()
        self.data2 = []
      
      
        self.i_2 =0
        self.ui.channel2.hide()
        self.ui.slider2.hide()
        self.ui.checkbox2.hide()
        self.f2 =0
        self.timer2 = None  
        self.ui.checkbox2.setChecked(False)
        self.z2 = 0  
   
    def clear3 (self):
        self.ui.channel3.clear()
        self.data3 = []
       
       
        self.i_3 =0
        self.ui.channel3.hide()
        self.ui.slider3.hide()
        self.ui.checkbox3.hide()
        self.f3 = 0
        self.timer3 = None
        self.ui.checkbox3.setChecked(False)
        self.z3 = 0  

    def clear4 (self):
        self.ui.channel4.clear()
        self.data4 = []
       
       
        self.i_4 =0
        self.ui.channel4.hide()
        self.ui.slider4.hide()
        self.ui.checkbox4.hide()
        self.f4 = 0
        self.timer4 = None 
       
        self.ui.checkbox4.setChecked(False)
        self.z4 = 0  

    def clear5 (self):
        self.ui.channel5.clear()
        self.data5 = []
       
       
        self.i_5 =0

        self.ui.channel5.hide()
        self.ui.slider5.hide()
        self.ui.checkbox5.hide()
        self.f5 = 0
        self.timer5 = None
      
        self.ui.checkbox5.setChecked(False)
        self.z5 = 0  

    def slider_1(self):
            pos= self.ui.slider1.value()
            self.ui.channel1.setXRange(pos-(len(self.data1)/30),pos)
            self.ui.slider1.setMaximum(len(self.data1))    
    def slider_2(self):
            pos= self.ui.slider2.value()
            self.ui.channel2.setXRange(pos-(len(self.data2)/30),pos)
            self.ui.slider2.setMaximum(len(self.data2))
    def slider_3(self):
            pos= self.ui.slider3.value()
            self.ui.channel3.setXRange(pos-(len(self.data3)/30),pos)
            self.ui.slider3.setMaximum(len(self.data3))
    def slider_4(self):
            pos= self.ui.slider4.value()
            self.ui.channel4.setXRange(pos-(len(self.data4)/30),pos)
            self.ui.slider4.setMaximum(len(self.data4))
    def slider_5(self):
            pos= self.ui.slider5.value()
            self.ui.channel5.setXRange(pos-(len(self.data5)/30),pos)
            self.ui.slider5.setMaximum(len(self.data5))        
                                                     
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() 
    window.show()
    sys.exit(app.exec_())