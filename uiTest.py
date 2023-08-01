from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QLabel, QFileDialog, QSpinBox, QDoubleSpinBox, QCheckBox, QComboBox, QLineEdit, QAction
import sys

class UI(QMainWindow):
    fileOpen = False
    fname = tuple
    Ae = 0
    Be = 0
    openFile = False
    folenmbr = 0
    
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
        self.heartP = self.findChild(QSpinBox, 'heartPiece')
        self.wallt = self.findChild(QSpinBox, 'Wallet')
        self.quiver = self.findChild(QSpinBox, 'quiver')
        self.bagBomb = self.findChild(QSpinBox, 'bombBag')
        self.coordYb = self.findChild(QSpinBox, 'Ybig')
        self.coordYs = self.findChild(QSpinBox, 'Ysmall')
        self.coordXb = self.findChild(QSpinBox, 'Xbig')
        self.coordXs = self.findChild(QSpinBox, 'Xsmall')
        self.hearts = self.findChild(QSpinBox, 'Hearts')
        self.health = self.findChild(QDoubleSpinBox, 'Health')
        self.rupees = self.findChild(QSpinBox, 'Rupees')
        self.arrow = self.findChild(QSpinBox, 'Arrow')
        self.bomb = self.findChild(QSpinBox, 'Bomb')
        self.map = self.findChild(QComboBox, 'Map')
        self.room = self.findChild(QSpinBox, 'room')
        self.anm = self.findChild(QComboBox, 'SpwnAnm')
        self.customize = self.findChild(QCheckBox, 'customize')
        self.A = self.findChild(QComboBox, 'A')
        self.B = self.findChild(QComboBox, 'B')
        self.sword = self.findChild(QCheckBox, 'sword')
        self.shield = self.findChild(QCheckBox, 'shield')
        self.boots = self.findChild(QCheckBox, 'boots')
        self.gust = self.findChild(QCheckBox, 'gust')
        self.mitts = self.findChild(QCheckBox, 'mitts')
        self.cape = self.findChild(QCheckBox, 'cape')
        self.cane = self.findChild(QCheckBox, 'cane')
        self.lantern = self.findChild(QCheckBox, 'lantern')
        self.ocarina = self.findChild(QCheckBox, 'ocarina')
        self.boomerang = self.findChild(QCheckBox, 'boomerang')
        self.bombs = self.findChild(QCheckBox, 'bombs')
        self.bow = self.findChild(QCheckBox, 'bow')
        self.Bottle1 = self.findChild(QCheckBox, 'Bottle1')
        self.Bottle2 = self.findChild(QCheckBox, 'Bottle2')
        self.Bottle3 = self.findChild(QCheckBox, 'Bottle3')
        self.Bottle4 = self.findChild(QCheckBox, 'Bottle4')
        self.bottle1 = self.findChild(QComboBox, 'bottle1')
        self.bottle2 = self.findChild(QComboBox, 'bottle2')
        self.bottle3 = self.findChild(QComboBox, 'bottle3')
        self.bottle4 = self.findChild(QComboBox, 'bottle4')
        self.oSword = self.findChild(QComboBox, 'oSword')
        self.oShield = self.findChild(QComboBox, 'oShield')
        self.oBow = self.findChild(QComboBox, 'oBow')
        self.oBoom = self.findChild(QComboBox, 'oBoom')
        self.oBomb = self.findChild(QComboBox, 'oBomb')

        self.tab.hide()
        self.file.hide()
        self.new.triggered.connect(self.reset)
        self.open.triggered.connect(self.Open)
        self.save.triggered.connect(self.Save)
        self.file.currentIndexChanged.connect(self.reload)
        self.wallt.valueChanged.connect(self.maxR)
        self.quiver.valueChanged.connect(self.maxA)
        self.bagBomb.valueChanged.connect(self.maxB)
        self.health.lineEdit().setReadOnly(True)
        self.map.currentIndexChanged.connect(self.mapInfo)
        self.customize.clicked.connect(self.chucked)
        self.A.currentIndexChanged.connect(self.Aa)
        self.B.currentIndexChanged.connect(self.Ba)

        self.show()
    def reset(self):
        self.name.setText('')
        self.brightness.setValue(2)
        self.speed.setValue(2)
        self.tri.setChecked(False)
        self.wallt.setValue(0)
        self.quiver.setValue(0)
        self.bagBomb.setValue(0)
        self.hearts.setValue(3)
        self.health.setValue(3)
        self.map.setCurrentIndex(0)
        self.mapInfo()
        self.customize.setChecked(False)
        self.chucked()
        self.rupees.setValue(0)
        self.arrow.setValue(0)
        self.bomb.setValue(0)
        self.A.setCurrentIndex(0)
        self.B.setCurrentIndex(0)
        self.sword.setChecked(False)
        self.shield.setChecked(False)
        self.boots.setChecked(False)
        self.gust.setChecked(False)
        self.mitts.setChecked(False)
        self.cape.setChecked(False)
        self.cane.setChecked(False)
        self.lantern.setChecked(False)
        self.ocarina.setChecked(False)
        self.boomerang.setChecked(False)
        self.bombs.setChecked(False)
        self.bow.setChecked(False)
        self.oSword.setCurrentIndex(0)
        self.oShield.setCurrentIndex(0)
        self.oBow.setCurrentIndex(0)
        self.oBoom.setCurrentIndex(0)
        self.oBomb.setCurrentIndex(0)
        self.Bottle1.setChecked(False)
        self.Bottle2.setChecked(False)
        self.Bottle3.setChecked(False)
        self.Bottle4.setChecked(False)
        self.bottle1.setCurrentIndex(0)
        self.bottle2.setCurrentIndex(0)
        self.bottle3.setCurrentIndex(0)
        self.bottle4.setCurrentIndex(0)
    def Open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Save File', '', 'mGBA or Bizhawk Save Files (*.sav *.SaveRAM);; All Files (*)')
        if fname[0]:
            if self.fileOpen == False:
                self.fileOpen = True
                self.new.setEnabled(True)
                self.save.setEnabled(True)
                self.tab.show()
                self.health.setEnabled(True)
                self.file.show()
            self.fname = fname
            self.reload()
    def reload(self):
        if self.fileOpen == True:
            self.reset()
            self.openFile = True
            sav = self.file.currentIndex()*1280
            file = open(self.fname[0], 'r+b')
            file.seek(200 + sav)
            if file.read(8) == b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF':
                return
            file.seek(326 + sav)
            self.rupee(file)
            file.seek(306 + sav)
            self.Be = int(ord(file.read(1)))
            self.Ae = int(ord(file.read(1)))
            self.Ba()
            self.Aa()
            file.seek(368 + sav)
            self.itemCheck(file)
            file.seek(296 + sav)
            self.quiver.setValue(int(ord(file.read(1))))
            self.bagBomb.setValue(int(ord(file.read(1))))
            self.arrow.setValue(int(ord(file.read(1))))
            self.bomb.setValue(int(ord(file.read(1))))
            self.hearts.setValue(int(ord(file.read(1))/8))
            health = ord(file.read(1)) / 8
            self.heartP.setValue(int(ord(file.read(1))))
            self.wallt.setValue(ord(file.read(1)))
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
            file.seek(132 + sav)
            self.brightness.setValue(ord(file.read(1)) + 1)
            self.speed.setValue(ord(file.read(1)) + 1)
            self.name.setText(man)
            self.health.setValue(health)
            self.openFile = False

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
    def maxR(self):
        if self.wallt.value() == 0:
            self.rupees.setMaximum(100)
        elif self.wallt.value() == 1:
            self.rupees.setMaximum(300)
        elif self.wallt.value() == 2:
            self.rupees.setMaximum(500)
        elif self.wallt.value() == 3:
            self.rupees.setMaximum(999)
        elif self.wallt.value() == 4:
            self.rupees.setMaximum(1279)
    def maxA(self):
        if self.quiver.value() == 0:
            self.arrow.setMaximum(30)
        elif self.quiver.value() == 1:
            self.arrow.setMaximum(50)
        elif self.quiver.value() == 2:
            self.arrow.setMaximum(70)
        elif self.quiver.value() == 3:
            self.arrow.setMaximum(99)
    def maxB(self):
        if self.bagBomb.value() == 0:
            self.bomb.setMaximum(10)
        elif self.bagBomb.value() == 1:
            self.bomb.setMaximum(30)
        elif self.bagBomb.value() == 2:
            self.bomb.setMaximum(50)
        elif self.bagBomb.value() == 3:
            self.bomb.setMaximum(99)
    def chucked(self):
        if self.customize.isChecked() == True:
            self.coordYb.setEnabled(True)
            self.coordYs.setEnabled(True)
            self.coordXb.setEnabled(True)
            self.coordXs.setEnabled(True)
            self.room.setEnabled(True)
            self.anm.setEnabled(True)
        elif self.customize.isChecked() == False:
            self.coordYb.setEnabled(False)
            self.coordYs.setEnabled(False)
            self.coordXb.setEnabled(False)
            self.coordXs.setEnabled(False)
            self.room.setEnabled(False)
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
    def Aa(self):
        if self.openFile == True:
            Ad = self.Ae
            if Ad > 4 and Ad < 22:
                Ad -= 1
            elif Ad == 23:
                Ad -= 2
            elif Ad > 23:
                Ad -= 6
            else: Ad
            self.A.setCurrentIndex(Ad)
        elif self.openFile == False:
            Ad = self.A.currentIndex()
            if Ad > 4 and Ad < 21:
                Ad += 1
            elif Ad == 21:
                Ad += 2
            elif Ad > 21:
                Ad += 6
            else: Ad
            self.Ae = Ad
    def Ba(self):
        if self.openFile == True:
            Bd = self.Be
            if Bd > 4 and Bd < 22:
                Bd -= 1
            elif Bd == 23:
                Bd -= 2
            elif Bd > 23:
                Bd -= 6
            else: Bd
            self.B.setCurrentIndex(Bd)
        elif self.openFile == False:
            Bd = self.B.currentIndex()
            if Bd > 4 and Bd < 21:
                Bd += 1
            elif Bd == 21:
                Bd += 2
            elif Bd > 21:
                Bd += 6
            else: Bd
            self.Be = Bd
    def itemCheck(self, file):
        if self.openFile == True:
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            bam = False
            if 1 in posBin2:
                self.cape.setChecked(True)
            if 3 in posBin2:
                self.boots.setChecked(True)
            if 7 in posBin2:
                self.ocarina.setChecked(True)
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            if 3 in posBin2:
                self.gust.setChecked(True)
            if 5 in posBin2:
                self.cane.setChecked(True)
            if 7 in posBin2:
                self.mitts.setChecked(True)
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            if 1 in posBin2:
                self.boomerang.setChecked(True)
                self.oBoom.setCurrentIndex(1)
            if 3 in posBin2:
                self.shield.setChecked(True)
                self.oShield.setCurrentIndex(0)
            elif 5 in posBin2:
                self.shield.setChecked(True)
                self.oShield.setCurrentIndex(1)
            if 7 in posBin2:
                self.lantern.setChecked(True)
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            if 1 in posBin2:
                self.bombs.setChecked(True)
                self.oBomb.setCurrentIndex(1)
                bam = True
            if 3 in posBin2:
                self.bow.setChecked(True)
                self.oBow.setCurrentIndex(0)
            elif 5 in posBin2:
                self.bow.setChecked(True)
                self.oBow.setCurrentIndex(1)
            if 7 in posBin2:
                self.boomerang.setChecked(True)
                self.oBoom.setCurrentIndex(0)
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            osf = ord(file.read(1))
            if (not posBin2) or (7 in posBin2):
                if osf == 0:
                    self.sword.setChecked(True)
                    self.oSword.setCurrentIndex(4)
                if osf == 5:
                    self.oSword.setCurrentIndex(0)
                    self.sword.setChecked(True)
                if 7 in posBin2 and bam == False:
                    self.bombs.setChecked(True)
                    self.oBomb.setCurrentIndex(0)
                if osf == 21:
                    self.sword.setChecked(True)
                    self.oSword.setCurrentIndex(1)
            if 4 in posBin2:
                if osf == 85:
                    self.sword.setChecked(True)
                    self.oSword.setcurrentIndex(2)
            if 1 in posBin2:
                if osf == 1:
                    self.sword.setChecked(True)
                    self.oSword.setCurrentIndex(3)
            if 5 in posBin2:
                self.sword.setChecked(True)
                self.oSword.setCurrentIndex(4)
            file.seek(382 + (self.folenmbr*1280))
            bin = format(int(ord(file.read(1))), 'b')
            posBin2 = [i for i, digit in enumerate(reversed(bin), 1) if digit == '1']
            if 1 in posBin2:
                self.Bottle1.setChecked(True)
                file.seek(305 + (self.folenmbr*1280))
                bin = int(ord(file.read(1)))
                if bin == 32:
                    self.bottle1.setCurrentIndex(0)
                elif bin > 32:
                    self.bottle1.setCurrentIndex(bin - 33)
            if 3 in posBin2:
                self.Bottle2.setChecked(True)
                file.seek(304 + (self.folenmbr*1280))
                bin = int(ord(file.read(1)))
                if bin == 32:
                    self.bottle2.setCurrentIndex(0)
                elif bin > 32:
                    self.bottle2.setCurrentIndex(bin - 33)
            if 5 in posBin2:
                self.Bottle3.setChecked(True)
                file.seek(319 + (self.folenmbr*1280))
                bin = int(ord(file.read(1)))
                if bin == 32:
                    self.bottle3.setCurrentIndex(0)
                elif bin > 32:
                    self.bottle3.setCurrentIndex(bin - 33)
            if 7 in posBin2:
                self.Bottle4.setChecked(True)
                file.seek(318 + (self.folenmbr*1280))
                bin = int(ord(file.read(1)))
                if bin == 32:
                    self.bottle4.setCurrentIndex(0)
                elif bin > 32:
                    self.bottle4.setCurrentIndex(bin - 33)
        elif self.openFile == False:
            RcPbO = 0b0
            GjCopMm = 0b0
            ShLaMb = 0b0
            RbBLABB = 0b0
            SsWsFs = 0b0
            botte = 0b0
            SwStuff1 = 0
            SwStuff2 = 0
            botte1 = 0
            botte2 = 0
            botte3 = 0
            botte4 = 0
            if self.sword.isChecked() == True:
                if self.oSword.currentIndex() == 0:
                    SwStuff1 += 5
                    SwStuff2 += 6
                elif self.oSword.currentIndex() == 1:
                    SwStuff1 += 21
                    SwStuff2 += 10
                elif self.oSword.currentIndex() == 2:
                    SsWsFs += 8
                    SwStuff1 += 85
                    SwStuff2 += 170
                elif self.oSword.currentIndex() == 3:
                    SsWsFs += 1
                    SwStuff1 += 1
                    SwStuff2 += 2
                else: SsWsFs += 16
            if self.cape.isChecked() == True:
                RcPbO += 0b0001
            if self.boots.isChecked() == True:
                RcPbO += 0b0100
            if self.ocarina.isChecked() == True:
                RcPbO += 0b01000000
            if self.gust.isChecked() == True:
                GjCopMm += 0b0100
            if self.cane.isChecked() == True:
                GjCopMm += 0b00010000
            if self.mitts.isChecked() == True:
                GjCopMm += 0b01000000
            if self.shield.isChecked() == True:
                if self.oShield.currentIndex() == 0:
                    ShLaMb += 0b0100
                else: ShLaMb += 0b00010000
            if self.lantern.isChecked() == True:
                ShLaMb += 0b01000000
            if self.boomerang.isChecked() == True:
                if self.oBoom.currentIndex() == 0:
                    RbBLABB += 0b01000000
                else: ShLaMb += 0b0001
            if self.bombs.isChecked() == True:
                if self.oBomb.currentIndex() == 0:
                    SsWsFs += 0b01000000
                else: RbBLABB += 0b0001
            if self.bow.isChecked() == True:
                if self.oBow.currentIndex() == 0:
                    RbBLABB += 0b0100
                else: RbBLABB += 0b00010000
            if self.Bottle1.isChecked() == True:
                botte += 0b0001
                if self.bottle1.currentIndex() == 0:
                    botte1 += 32
                elif self.bottle1.currentIndex() > 0:
                    botte1 += (33 + self.bottle1.currentIndex())
            if self.Bottle2.isChecked() == True:
                botte += 0b0100
                if self.bottle2.currentIndex() == 0:
                    botte2 += 32
                elif self.bottle2.currentIndex() > 0:
                    botte2 += (33 + self.bottle2.currentIndex())
            if self.Bottle3.isChecked() == True:
                botte += 0b00010000
                if self.bottle3.currentIndex() == 0:
                    botte3 += 32
                elif self.bottle3.currentIndex() > 0:
                    botte3 += (33 + self.bottle3.currentIndex())
            if self.Bottle4.isChecked() == True:
                botte += 0b01000000
                if self.bottle4.currentIndex() == 0:
                    botte4 += 32
                elif self.bottle4.currentIndex() > 0:
                    botte4 += (33 + self.bottle4.currentIndex())
            file.write((RcPbO).to_bytes())
            file.write((GjCopMm).to_bytes())
            file.write((ShLaMb).to_bytes())
            file.write((RbBLABB).to_bytes())
            file.write((SsWsFs).to_bytes())
            file.write((SwStuff1).to_bytes())
            file.seek(376 + (self.folenmbr*1280))
            file.write((SwStuff2).to_bytes())

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
        input_file.write((self.speed.value() - 1).to_bytes())
        Tri = int(self.tri.isChecked())
        input_file.seek(129 + (filenumbuh*1280))
        input_file.write(int(Tri).to_bytes())
        hearts = self.hearts.value()
        hearts *= 8
        health = self.health.value()
        health *= 8
        input_file.seek(296 + (filenumbuh*1280))
        input_file.write(int(self.quiver.value()).to_bytes())
        input_file.write(int(self.bagBomb.value()).to_bytes())
        input_file.write(int(self.arrow.value()).to_bytes())
        input_file.write(int(self.bomb.value()).to_bytes())
        input_file.write(int(hearts).to_bytes())
        input_file.write(int(health).to_bytes())
        input_file.write(int(self.heartP.value()).to_bytes())
        input_file.write(int(self.wallt.value()).to_bytes())
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
        elif rupees > 1023 and rupees < 1280:
            input_file.write(bytes([4]))
            rupees -= 1024
        else: input_file.write(bytes([0]))
        input_file.write((rupees).to_bytes())
        input_file.seek(264 + (filenumbuh*1280))
        input_file.write((self.coordYb.value()).to_bytes())
        input_file.write((self.coordYs.value()).to_bytes())
        input_file.write((self.coordXb.value()).to_bytes())
        input_file.write((self.coordXs.value()).to_bytes())
        input_file.write((self.anm.currentIndex()).to_bytes())
        input_file.seek(270 + (filenumbuh*1280))
        input_file.write((self.room.value() - 1).to_bytes())
        input_file.write((self.map.currentIndex()).to_bytes())
        input_file.seek(306 + (filenumbuh*1280))
        input_file.write((self.Be).to_bytes())
        input_file.write((self.Ae).to_bytes())
        input_file.seek(368 + (filenumbuh*1280))
        self.folenmbr = filenumbuh
        self.itemCheck(file)
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
