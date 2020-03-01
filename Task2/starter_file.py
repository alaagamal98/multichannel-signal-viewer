from PyQt5 import QtWidgets
from mainui import Ui_MainWindow
import sys
from scipy.io import wavfile
from scipy.fftpack import fft,rfft
import numpy as np
import pandas as pd


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.sliders = [self.ui.verticalSlider,self.ui.verticalSlider_2,self.ui.verticalSlider_3,self.ui.verticalSlider_4,self.ui.verticalSlider_5,self.ui.verticalSlider_6,self.ui.verticalSlider_7,self.ui.verticalSlider_8,self.ui.verticalSlider_9,self.ui.verticalSlider_10]
        
        self.p1 = 0  
        self.ui.browser.clicked.connect(self.getfiles)
        # self.ui.verticalSlider.valueChanged.connect(self.humming)
        self.pos = self.ui.verticalSlider.value()


    def getfiles(self):
        path,extention = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
            "(*.wav )")
        self.read_file(path)

    def read_file(self,path):
        self.samplerate, self.data = wavfile.read(path)
        self.Timedomain(self.data,self.samplerate)

    def Timedomain(self,data,samplerate):
        self.ui.graphicsView.setXRange(0,samplerate)
        self.ui.graphicsView.showGrid(True)
        self.ui.graphicsView.setYRange(min(data[:,0]),max(data[:,0]))
        self.ui.graphicsView.plot(data[:,0])



    

    def FFS(self,fn):
      
        self.data = self.data[:,0]
        # convert gain to db 
        window = np.hanning(1024)
        self.data = self.data[0:1024] * window
        #fft
        mags = abs(rfft(self.data))
        # convert to dB
        mags = 20*np.log10(mags)
        # normalise to 0 dB max
     
        mags -= max(mags)
        #Get the absolute value of real and complex component:     
        self.samples_length =self.data.shape[0]
        self.freqs = np.fft.fftfreq(self.samples_length,1/self.samplerate)
        self.plot(self.freqs,mags)



    def plot(self,freqs,mags):

        
        self.ui.graphicsView.setXRange(0, self.samplerate/2)
       
        self.ui.graphicsView.showGrid(True)

       
        self.ui.graphicsView.plot(freqs[:int(freqs.size/2)],mags[:int(freqs.size/2)])
        self.all_data = mags[:int(freqs.size/2)]
        self.divideTo10bands()

    

    def divideTo10bands(self):
        
        bandsno = int(0.1 * self.all_data.size * 0.5)
 
        bands =[self.all_data[i * bandsno:(i + 1) * bandsno] for i in range((len(self.all_data) + bandsno - 1) // bandsno )]
        return(bands)
        # print(type(bands[0]))
    
    def humming(self):
        data = self.divideTo10bands()
        self.pos = self.ui.verticalSlider.value()
        hamm = np.hamming(self.all_data.size)
        # # data[0] = [int(x) * int(self.pos) for x in data[0]]
        # alldata = [element for sublist in data for element in sublist]
         # convert to dB
        mags = 20*np.log10(data)
        # normalise to 0 dB max
        mags -= max(mags)

        self.ui.graphicsView_2.setXRange(0, self.samplerate/2)

        # self.ui.graphicsView.setLogMode(True,None)
       
        self.ui.graphicsView_2.showGrid(True)

        self.ui.graphicsView_2.plot(self.freqs[:int(self.freqs.size/2)],mags[:int(self.freqs.size/2)]) 









    
    # def sliders(self):
    #     self.bands = self.divideTo10bands(self.all_data)
    #     pos = self.ui.verticalSlider.value()
    #     self.bands[1][0] = [x + pos for x in self.bands[1][0]]

    #     self.ui.graphicsView.plot(self.bands.iloc[0][:int(self.freqs.size/2)],self.bands.iloc[1][:int(self.freqs.size/2)]) 

    #     print(pos)
    #     self.ui.verticalSlider.setMaximum(1+self.p1) 


        
             
        
    
   



       
               
            





    
   





def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()