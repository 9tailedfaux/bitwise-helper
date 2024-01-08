from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QRadioButton, QGroupBox, QVBoxLayout, 
    QLabel, QHBoxLayout, QDialog, QWidget)
import sys
import re

class Window(QMainWindow):

    sample = 0
    mask = 0
    result = 0

    def __init__(self):
        super().__init__()

        centralWidget = QWidget()

        mainLayout = QVBoxLayout(centralWidget)

        sampleBox = BinHexBox("Sample", self.updateSample)
        maskBox = BinHexBox("Mask", self.updateMask)
        self.finalResult = Result()

        mainLayout.addWidget(sampleBox)
        mainLayout.addWidget(maskBox)
        mainLayout.addWidget(self.finalResult)

        self.setCentralWidget(centralWidget)

        self.setMinimumWidth(600)
        self.setWindowTitle("Bitwise Helper")
        self.show()

    def updateSample(self, sample):
        self.sample = sample
        self.recalculate()

    def updateMask(self, mask):
        self.mask = mask
        self.recalculate()

    def recalculate(self):
        self.result = self.sample & self.mask
        self.finalResult.setResult(bin(self.result))

class Result(QGroupBox):
    def __init__(self, title = "Result", parent = None):
        super().__init__(title, parent)

        self.resultLabel = QLabel()
        self.resultLabel.setText("0")

        layout = QHBoxLayout()

        layout.addWidget(self.resultLabel)

        self.setLayout(layout)

    def setResult(self, result):
        self.resultLabel.setText(result)

class BinHexBox(QGroupBox):

    binaryMode = True
    bits = 8
    pattern = re.compile("^[01]+$")

    def __init__(self, title, onChange, parent = None):
        super().__init__(title, parent)
        
        self.onChange = onChange

        eightBitRadio = QRadioButton("8 bits")
        eightBitRadio.clicked.connect(self.set8bit)
        sixteenBitRadio = QRadioButton("16 bits")
        sixteenBitRadio.clicked.connect(self.set16bit)
        thirtyTwoBitRadio = QRadioButton("32 bits")
        thirtyTwoBitRadio.clicked.connect(self.set32bit)
        eightBitRadio.setChecked(True)
        bitRadios = QWidget()
        bitRadiosLayout = QVBoxLayout(bitRadios)
        bitRadiosLayout.addWidget(eightBitRadio)
        bitRadiosLayout.addWidget(sixteenBitRadio)
        bitRadiosLayout.addWidget(thirtyTwoBitRadio)

        binRadio = QRadioButton("Binary")
        binRadio.clicked.connect(self.setBinary)
        hexRadio = QRadioButton("Hex")
        hexRadio.clicked.connect(self.setHex)
        binRadio.setChecked(True)
        binHexRadios = QWidget()
        binHexRadiosLayout = QVBoxLayout(binHexRadios)
        binHexRadiosLayout.addWidget(binRadio)
        binHexRadiosLayout.addWidget(hexRadio)

        self.binHexLabel = QLabel("0b");
        self.binHexEnter = QLineEdit();
        self.binHexEnter.setMaxLength(self.bits)
        self.binHexEnter.textEdited.connect(self.localOnChange)

        layout = QHBoxLayout()

        layout.addWidget(bitRadios)
        #layout.addWidget(binHexRadios)
        layout.addWidget(self.binHexLabel)
        layout.addWidget(self.binHexEnter)

        self.setLayout(layout)

    def localOnChange(self):
        if self.pattern.match(self.binHexEnter.text()):
            self.onChange(int(self.binHexEnter.text()))

    def recalculateMaxLength(self):
        self.binHexEnter.setMaxLength(self.bits)

    def setBinary(self):
        self.binaryMode = True
        self.binHexLabel.setText("0b")

    def setHex(self):
        self.binaryMode = False
        self.binHexLabel.setText("0x")

    def set8bit(self):
        self.bits = 8
        self.recalculateMaxLength()

    def set16bit(self):
        self.bits = 16
        self.recalculateMaxLength()

    def set32bit(self):
        self.bits = 32
        self.recalculateMaxLength()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())