from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QSpinBox, QDoubleSpinBox, QCheckBox, QTabWidget, QComboBox, QLineEdit, QAction
import string
import sys

class UI(QMainWindow):
    fileOpen = False
    fname = tuple
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("untitled.ui", self)

        self.new = self.findChild(QAction, 'actionNew')
        self.open = self.findChild(QAction, 'actionOpen')
        self.file = self.findChild(QComboBox, 'File')
        self.name = self.findChild(QLineEdit, 'name')
        self.brightness = self.findChild(QSpinBox, 'Brightness')
        self.speed = self.findChild(QSpinBox, 'Speed')
        self.tri = self.findChild(QCheckBox, 'Tri')
        self.coordYb = self.findChild(QSpinBox, 'Ybig')
        self.coordYs = self.findChild(QSpinBox, 'Ysmall')
        self.coordXb = self.findChild(QSpinBox, 'Xbig')
        self.coordXs = self.findChild(QSpinBox, 'Xsmall')
        self.health = self.findChild(QDoubleSpinBox, 'Health')
        self.rupees = self.findChild(QSpinBox, 'Rupees')
        self.map = self.findChild(QComboBox, 'Map')
        self.anm = self.findChild(QComboBox, 'SpwnAnm')
        self.customize = self.findChild(QCheckBox, 'customize')

        self.new.triggered.connect(self.reset)
        self.open.triggered.connect(self.Open)
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
            
    def reload(self):
        if self.fileOpen == True:
            sav = self.file.currentIndex()*1280
            file = open(self.fname[0], 'r+b')
            file.seek(326 + sav)
            self.rupee(file)
            file.seek(301 + sav)
            health = ord(file.read(1)) / 8
            file.seek(258 + sav)
            name = file.read(6)
            man = name[::-1]
            name = man.rstrip(bytes.fromhex('00'))
            man = name.decode()
            file.seek(270 + sav)
            bam = file.read(2)
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
            self.coordYb.setValue(131)
            self.coordYs.setValue(54)
            self.coordXb.setValue(0)
            self.coordXs.setValue(8)
            self.anm.setCurrentIndex(0)
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
        if bam == b'\x00\x02':
            self.map.setCurrentIndex(0)
        elif bam == b'\x06\x03':
            self.map.setCurrentIndex(1)
        elif bam == b'\x00\x0A':
            self.map.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
