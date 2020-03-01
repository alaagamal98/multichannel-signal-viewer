from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import sys
from scipy.io import wavfile
from scipy.fftpack import fft,rfft,fftfreq
import numpy as np
import pandas as pd


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.p1 = 0  
        self.ui.browser.clicked.connect(self.getfiles)
        # self.ui.verticalSlider.valueChanged.connect(self.humming)
        

    def getfiles(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
            "(*.wav )")
        self.FFS(fileName)

    def FFS(self,fn):
        path = fn[0]
        self.samplerate, self.data = wavfile.read(path)
   
        self.data = self.data[:,0]
      
        # convert gain to db 
        datafft = fft(self.data)
        #Get the absolute value of real and complex component:
        fftabs = abs(datafft)
      
        # convert to dB
        mags = 20*np.log10(fftabs)
        # normalise to 0 dB max
        mags -= max(mags)

        #Get the absolute value of real and complex component:     
        self.samples_length =self.data.shape[0]
        self.freqs = np.fft.fftfreq(self.samples_length,1/self.samplerate)
        self.plot(self.freqs,mags)



    def plot(self,freqs,mags):

        
        self.ui.graphicsView.setXRange(0, self.samplerate/2)

        # self.ui.graphicsView.setLogMode(True,None)
       
        self.ui.graphicsView.showGrid(True)

       
        self.ui.graphicsView.plot(freqs[:int(freqs.size/2)],mags[:int(freqs.size/2)])

        self.divideTo10bands(mags[:int(freqs.size/2)])

    

    def divideTo10bands(self,all_data):
        bandsno = int(0.1 * all_data.size * 0.5)
 
        bands =[all_data[i * bandsno:(i + 1) * bandsno] for i in range((len(all_data) + bandsno - 1) // bandsno )]
        self.humming(bands)
        print(type(bands[0]))
    
    def humming(self,data):
        # print(data)
        pos = self.ui.verticalSlider.value()
        data[0] = [int(x) * int(pos) for x in data[0]]
        alldata = [element for sublist in data for element in sublist]
        print(alldata)
        self.ui.graphicsView.plot(self.freqs[:int(self.freqs.size/2)],alldata[:int(self.freqs.size/2)]) 








    
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