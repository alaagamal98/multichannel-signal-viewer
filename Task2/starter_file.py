from PyQt5 import QtWidgets,QtMultimedia,QtCore
from mainwindow import Ui_MainWindow
import sys
QMediaPlayer=QtMultimedia.QMediaPlayer
QMediaContent=QtMultimedia.QMediaContent

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.player =  QMediaPlayer(self) 
        self.ui.setupUi(self) 
        self.ui.play.clicked.connect(self.player.play)
        self.ui.pause.clicked.connect(self.player.pause)
        self.ui.stop.clicked.connect(self.player.stop)
        self.ui.browser.clicked.connect(self.getfile)
    def getfile (self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "")
        print(filename)
        sound = QMediaContent(QtCore.QUrl.fromLocalFile(filename[0]))
        self.player.setMedia(sound)
        # if filename:
        #     self.player(
        #         QMediaContent(
        #             self.QUrl.fromLocalFile(filename)
        #         )
        #     )                                                                                                                                                                                                                             


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()