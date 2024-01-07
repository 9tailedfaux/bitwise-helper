from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QRadioButton, QGroupBox, QVBoxLayout, 
    QLabel, QHBoxLayout, QDialog, QWidget)
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        centralWidget = QWidget()

        maskBox = BinHexBox("Mask", centralWidget)

        self.setCentralWidget(centralWidget)

        #self.changeStyle('Windows')
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("Bitwise Helper")
        self.show()

class BinHexBox(QGroupBox):

    binaryMode = True

    def __init__(self, title, parent):
        super().__init__(title, parent)

        binRadio = QRadioButton("Binary")
        binRadio.clicked.connect(self.setBinary)
        hexRadio = QRadioButton("Hex")
        hexRadio.clicked.connect(self.setHex)
        binRadio.setChecked(True)

        self.binHexLabel = QLabel("0b");
        self.binHexEnter = QLineEdit();

        layout = QHBoxLayout()

        layout.addWidget(binRadio)
        layout.addWidget(hexRadio)
        layout.addWidget(self.binHexLabel)
        layout.addWidget(self.binHexEnter)

        self.setLayout(layout)

    def setBinary(self):
        binaryMode = True
        self.binHexLabel.setText("0b")

    def setHex(self):
        binaryMode = False
        self.binHexLabel.setText("0x")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())