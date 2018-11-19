from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGroupBox, QVBoxLayout, QGridLayout, QSizePolicy, QLCDNumber

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.createGridButtonLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.createDisplay())
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridButtonLayout(self):

        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()

        layout.setColumnStretch(0,5)
        layout.setColumnStretch(1, 5)
        layout.setColumnStretch(2, 5)
        layout.setColumnStretch(3, 5)
        layout.setColumnStretch(4, 5)
#------------------------------------------------------------------------------------
        button = QPushButton('MC')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 0, 0, 1, 1)

        button = QPushButton('MR')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 0, 1, 1, 1)

        button = QPushButton('MS')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 0, 2, 1, 1)

        button = QPushButton('M+')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 0, 3, 1, 1)

        button = QPushButton('M-')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 0, 4, 1, 1)

        button = QPushButton('←')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 0, 1, 1)

        button = QPushButton('CE')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 1, 1, 1)

        button = QPushButton('C')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 2, 1, 1)

        button = QPushButton('±')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 3, 1, 1)

        button = QPushButton('√')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 1, 4, 1, 1)

        button = QPushButton('7')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 2, 0, 1, 1)

        button = QPushButton('8')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 2, 1, 1, 1)

        button = QPushButton('9')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 2, 2, 1, 1)

        button = QPushButton('/')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 2, 3, 1, 1)

        button = QPushButton('%')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 2, 4, 1, 1)

        button = QPushButton('4')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 3, 0, 1, 1)

        button = QPushButton('5')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 3, 1, 1, 1)

        button = QPushButton('6')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 3, 2, 1, 1)

        button = QPushButton('*')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 3, 3, 1, 1)

        button = QPushButton('1/x')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 3, 4, 1, 1)

        button = QPushButton('1')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 4, 0, 1, 1)

        button = QPushButton('2')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 4, 1, 1, 1)

        button = QPushButton('3')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 4, 2, 1, 1)

        button = QPushButton('-')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 4, 3, 1, 1)

        button = QPushButton('=')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 4, 4, -1, 1)

        button = QPushButton('0')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 5, 0, 1, 2)

        button = QPushButton(',')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 5, 2, 1, 1)

        button = QPushButton('+')
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        layout.addWidget(button, 5, 3, 1, 1)
#----------------------------------------------------------------------------------
        self.horizontalGroupBox.setLayout(layout)


    def createDisplay(self):
        lcdNumber = QLCDNumber()
        lcdNumber.setMode(QLCDNumber.Dec)
        lcdNumber.setFixedHeight(50)
        return lcdNumber

