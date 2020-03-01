from PyQt5 import QtWidgets,QtMultimedia,QtCore
from mainwindow import Ui_MainWindow
import sys
import os
QMediaPlayer=QtMultimedia.QMediaPlayer
QMediaContent=QtMultimedia.QMediaContent

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.player = QMediaPlayer(self)
        self.ui.setupUi(self)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.ui.mute.clicked.connect(self.mute)
        self.ui.play.clicked.connect(self.play)
        self.ui.pause.clicked.connect(self.pause)
        self.ui.stop.clicked.connect(self.stop)
        self.ui.volume.valueChanged.connect(self.update_value)
        self.ui.browser.clicked.connect(self.getfile)
    def mute(self):
        if self.ui.mute.text()=="Mute":
            self.player.setMuted(True)
            self.ui.mute.setText("Unmute")
        else:
            self.player.setMuted(False)
            self.ui.mute.setText("Mute")
    def play(self):
        self.player.play()
        self.ui.statusBar.showMessage("play")
    def pause(self):
        self.player.pause()
        self.ui.statusBar.showMessage("pause")
    def stop(self):
        self.player.stop()
        self.ui.statusBar.showMessage("stop")
    def update_value (self,value):
        self.player.setVolume(self.ui.volume.value())
    def update_duration (self,dur):
        self.ui.progressBar.setRange(0,dur)
    def update_position (self,pos):
        self.ui.progressBar.setValue(pos)
    def getfile (self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "")
        sound = QMediaContent(QtCore.QUrl.fromLocalFile(filename[0]))
        self.player.setMedia(sound)




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()