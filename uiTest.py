from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QLabel, QFileDialog, QSpinBox, QDoubleSpinBox, QCheckBox, QComboBox, QLineEdit, QAction
import sys

class UI(QMainWindow):
    fileOpen = False
    fname = tuple
    
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("untitled.ui", self)

        self.tab = self.findChild(QTabWidget, 'tabb')
        self.label = self.findChild(QLabel, 'label')
        self.new = self.findChild(QAction, 'actionNew')
        self.open = self.findChild(QAction, 'actionOpen')
        self.save = self.findChild(QAction, 'actionSave')
        self.file = self.findChild(QComboBox, 'File')
        self.name = self.findChild(QLineEdit, 'name')
        self.brightness = self.findChild(QSpinBox, 'Brightness')
        self.speed = self.findChild(QSpinBox, 'Speed')
        self.tri = self.findChild(QCheckBox, 'Tri')
        self.wallt = self.findChild(QSpinBox, 'Wallet')
        self.coordYb = self.findChild(QSpinBox, 'Ybig')
        self.coordYs = self.findChild(QSpinBox, 'Ysmall')
        self.coordXb = self.findChild(QSpinBox, 'Xbig')
        self.coordXs = self.findChild(QSpinBox, 'Xsmall')
        self.hearts = self.findChild(QSpinBox, 'Hearts')
        self.health = self.findChild(QDoubleSpinBox, 'Health')
        self.rupees = self.findChild(QSpinBox, 'Rupees')
        self.map = self.findChild(QComboBox, 'Map')
        self.room = self.findChild(QSpinBox, 'room')
        self.anm = self.findChild(QComboBox, 'SpwnAnm')
        self.customize = self.findChild(QCheckBox, 'customize')

        self.tab.hide()
        self.new.triggered.connect(self.reset)
        self.open.triggered.connect(self.Open)
        self.save.triggered.connect(self.Save)
        self.file.currentIndexChanged.connect(self.reload)
        self.health.lineEdit().setReadOnly(True)
        self.map.currentIndexChanged.connect(self.mapInfo)
        self.customize.clicked.connect(self.chucked)
        self.show()
    def reset(self):
        self.name.setText('')
        self.brightness.setValue(2)
        self.speed.setValue(2)
        self.tri.setChecked(False)
        self.wallt.setValue(0)
        self.hearts.setValue(3)
        self.health.setValue(3)
        self.map.setCurrentIndex(0)
        self.mapInfo()
        self.customize.setChecked(False)
        self.chucked()
        self.rupees.setValue(0)
    def Open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open .sav File', '', 'mGBA Save Files (*.sav);; All Files (*)')
        if fname[0]:
            self.fileOpen = True
            self.fname = fname
            self.reload()
            self.new.setEnabled(True)
            self.save.setEnabled(True)
            self.tab.show()
            self.health.setEnabled(True)
    def reload(self):
        if self.fileOpen == True:
            sav = self.file.currentIndex()*1280
            file = open(self.fname[0], 'r+b')
            file.seek(200 + sav)
            if file.read(8) == b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF':
                return
            file.seek(326 + sav)
            self.rupee(file)
            file.seek(301 + sav)
            health = ord(file.read(1)) / 8
            file.seek(300 + sav)
            self.hearts.setValue(int(ord(file.read(1))/8))
            file.seek(258 + sav)
            name = file.read(6)
            man = name[::-1]
            name = man.rstrip(bytes.fromhex('00'))
            man = name.decode()
            file.seek(271 + sav)
            bam = file.read(1)
            self.maap(bam)
            file.seek(129 + sav)
            trii = file.read(1)
            if trii == bytes.fromhex('00'):
                self.tri.setChecked(False)
            elif trii == bytes.fromhex('01'):
                self.tri.setChecked(True)
            file.seek(303 + sav)
            self.wallt.setValue(ord(file.read(1)))
            file.seek(132 + sav)
            self.brightness.setValue(ord(file.read(1)) + 1)
            self.speed.setValue(ord(file.read(1)) + 1)
            self.name.setText(man)
            self.health.setValue(health)
            
    def mapInfo(self):
        if self.map.currentIndex() == 0:
            self.coordYb.setValue(0)
            self.coordYs.setValue(24)
            self.coordXb.setValue(1)
            self.coordXs.setValue(248)
            self.anm.setCurrentIndex(0)
        elif self.map.currentIndex() == 1:
            self.coordYb.setValue(3)
            self.coordYs.setValue(24)
            self.coordXb.setValue(1)
            self.coordXs.setValue(248)
            self.anm.setCurrentIndex(0)
        elif self.map.currentIndex() == 2:
            self.coordYb.setValue(0)
            self.coordYs.setValue(24)
            self.coordXb.setValue(1)
            self.coordXs.setValue(248)
            self.anm.setCurrentIndex(0)
        elif self.map.currentIndex() == 3:
            self.coordYb.setValue(3)
            self.coordYs.setValue(24)
            self.coordXb.setValue(1)
            self.coordXs.setValue(248)
        else: pass
    def rupee(self, file):
        bigR = ord(file.read(1))
        smallR = ord(file.read(1))
        if bigR == 0:
            smallR
        elif bigR == 1:
            smallR += 256
        elif bigR == 2:
            smallR += 512
        elif bigR == 3:
            smallR += 768
        self.rupees.setValue(smallR)
    def chucked(self):
        if self.customize.isChecked() == True:
            self.coordYb.setEnabled(True)
            self.coordYs.setEnabled(True)
            self.coordXb.setEnabled(True)
            self.coordXs.setEnabled(True)
            self.anm.setEnabled(True)
        elif self.customize.isChecked() == False:
            self.coordYb.setEnabled(False)
            self.coordYs.setEnabled(False)
            self.coordXb.setEnabled(False)
            self.coordXs.setEnabled(False)
            self.anm.setEnabled(False)
    def maap(self,bam):
        self.room.setValue(1)
        room = False
        self.map.setCurrentIndex(ord(bam))
        mop = self.map.currentIndex()
        if self.map.currentIndex() != (0 or 2 or 4 or 7 or 10 or 12 or 15 or 16 or 20 or 21 or 22 or 23 or 26 or 49 or 56 or 68 or 69 or 73 or 74 or 77 or 81 or 87 or 89 or 95 or 111 or 113 or 119 or 127 or 129 or 135 or 139 or 140 or 141 or 143):
            room = True
        if room == True:
            if mop == 1:
                self.room.setMaximum(2)
            elif mop == 3:
                self.room.setMaximum(10)
            elif mop == 5:
                self.room.setMaximum(6)
            elif mop == 6:
                self.room.setMaximum(5)
            elif mop == 8:
                self.room.setMaximum(3)
            elif mop == 9:
                self.room.setMaximum(2)
            elif mop == 11:
                self.room.setMaximum(2)
        else: self.room.setMaximum(1)
    def Save(self):
        def CalculateChecksum(filenumber : int) -> int:
            gameState = data[0x34 + (filenumber * 0x10):0x34 + (filenumber * 0x10) + 0x04]
            gameData = data[0x80 + (filenumber * 0x500):0x80 + (filenumber * 0x500) + 0x500]
            shortcheck = partial_check(gameState)
            longcheck = partial_check(gameData)

            combined = (shortcheck + longcheck) & 0xFFFF
            upper = combined << 16
            lower = ~combined & 0xFFFF

            lower += 1
            combined = upper + lower
            return combined

        def undo_reverse(data: bytes) -> bytes:
            data = bytearray(data)
            for i in range(0, len(data), 8):
                data[i:i + 8] = int.from_bytes(data[i:i + 8], 'big').to_bytes(8, 'little')
            return bytes(data)

        def partial_check(data: bytes) -> int:
            pos = 0
            remaining = len(data)
            sum = 0
            while remaining > 0:
                sum += (data[pos] | (data[pos + 1] << 8)) ^ remaining
                pos += 2
                remaining -= 2
            sum &= 0xFFFF
            return sum
        
        file = open(self.fname[0], 'r+b')
        input_file = file
        filename = self.name.text()
        filenameSpace = 6 - len(filename)
        xtraSpace = filenameSpace * "0"
        input_file.seek(258 + ((self.file.currentIndex())*1280))
        input_file.write(bytes([00,00,00,00,00,00]))
        input_file.seek(258 + ((self.file.currentIndex())*1280))
        filenumbuh = self.file.currentIndex()
        if filenameSpace > 0:
            input_file.write(int(xtraSpace).to_bytes(filenameSpace, byteorder='little'))
        input_file.write(bytes(filename[::-1], 'ascii'))
        input_file.seek(132 + (filenumbuh*1280))
        input_file.write((self.brightness.value() - 1).to_bytes())
        input_file.seek(133 + (filenumbuh*1280))
        input_file.write((self.speed.value() - 1).to_bytes())
        Tri = int(self.tri.isChecked())
        input_file.seek(129 + (filenumbuh*1280))
        input_file.write(int(Tri).to_bytes())
        hearts = self.hearts.value()
        hearts *= 8
        input_file.seek(300 + (filenumbuh*1280))
        input_file.write(int(hearts).to_bytes())
        health = self.health.value()
        health *= 8
        input_file.seek(301 + (filenumbuh*1280))
        input_file.write(int(health).to_bytes())
        rupees = self.rupees.value()
        input_file.seek(326 + (filenumbuh*1280))
        if rupees > 255 and rupees < 512:
            input_file.write(bytes([1]))
            rupees -= 256
        elif rupees > 511 and rupees < 768:
            input_file.write(bytes([2]))
            rupees -= 512
        elif rupees > 767 and rupees < 1024:
            input_file.write(bytes([3]))
            rupees -= 768
        else: input_file.write(bytes([0]))
        input_file.write((rupees).to_bytes())
        input_file.seek(264)
        input_file.write((self.coordYb.value()).to_bytes())
        input_file.seek(265)
        input_file.write((self.coordYs.value()).to_bytes())
        input_file.seek(266)
        input_file.write((self.coordXb.value()).to_bytes())
        input_file.seek(267)
        input_file.write((self.coordXs.value()).to_bytes())
        input_file.seek(268 + (filenumbuh*1280))
        input_file.write((self.anm.currentIndex()).to_bytes())
        input_file.seek(270 + (filenumbuh*1280))
        input_file.write((self.room.value() - 1).to_bytes())
        input_file.seek(271 + (filenumbuh*1280))
        input_file.write((self.map.currentIndex()).to_bytes())
        #Ezlo = int(input('Enter 8 for hatless or 38 for hat: '))
        #input_file.seek(729)
        #input_file.write((Ezlo).to_bytes())
        filenumber = self.file.currentIndex()
        input_file.seek(0)
        data = input_file.read()
        data = undo_reverse(data)
        CalculateChecksum((filenumber))
        newchecksum = CalculateChecksum((filenumber))
        input_file.seek(48+(filenumbuh*16))
        input_file.write(((newchecksum & 4294901760) >> 16).to_bytes(8))
        input_file.seek(48+(filenumbuh*16))
        input_file.write((newchecksum & 0xFFFF).to_bytes(8))
        input_file.seek(54+(filenumbuh*16))
        big_byte = int.from_bytes(input_file.read(2))
        input_file.seek(52+(filenumbuh*16))
        input_file.write((65536-big_byte).to_bytes(2))
        input_file.seek(48+(filenumbuh*16))
        input_file.write(bytes([77, 67, 90, 51]))
        if filenumbuh == 0:
            input_file.seek(52)
            fourtofive=input_file.read(2)
            input_file.seek(54)
            sixtoseven=input_file.read(2)
            input_file.seek(52)
            input_file.write(sixtoseven)
            input_file.seek(54)
            input_file.write(fourtofive)
        elif filenumbuh == 1:
            input_file.seek(68)
            fourtofive=input_file.read(2)
            input_file.seek(70)
            sixtoseven=input_file.read(2)
            input_file.seek(68)
            input_file.write(sixtoseven)
            input_file.seek(70)
            input_file.write(fourtofive)
        elif filenumbuh == 2:
            input_file.seek(84)
            fourtofive=input_file.read(2)
            input_file.seek(86)
            sixtoseven=input_file.read(2)
            input_file.seek(84)
            input_file.write(sixtoseven)
            input_file.seek(86)
            input_file.write(fourtofive)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
