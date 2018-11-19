import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtCore import QSize
from Calculator import basicWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.width = 200
        self.height = 200
        self.setMinimumSize(QSize(200,250))
        self.setMaximumSize(QSize(500,675))
        self.setWindowTitle("Kalkulator")

        self.createMenuBar()

    def createMenuBar(self):
        options = ['&Widok', '&Edycja', '&Pomoc']
        menuBar = self.menuBar()
        for opt in options:
            menuBar.addMenu(opt)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    central_widget = basicWindow()
    mainWin.setCentralWidget(central_widget)
    mainWin.show()
    sys.exit( app.exec_() )



