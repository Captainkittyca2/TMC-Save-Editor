from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QSpinBox, QDoubleSpinBox, QCheckBox, QTabWidget, QComboBox, QLineEdit, QAction
import string
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("untitled.ui", self)

        self.new = self.findChild(QAction, 'actionNew')
        self.open = self.findChild(QAction, 'actionOpen')
        self.name = self.findChild(QLineEdit, 'name')
        self.tri = self.findChild(QCheckBox, 'Tri')
        self.coordYb = self.findChild(QSpinBox, 'Ybig')
        self.coordYs = self.findChild(QSpinBox, 'Ysmall')
        self.coordXb = self.findChild(QSpinBox, 'Xbig')
        self.coordXs = self.findChild(QSpinBox, 'Xsmall')
        self.health = self.findChild(QDoubleSpinBox, 'Health')
        self.map = self.findChild(QComboBox, 'Map')
        self.anm = self.findChild(QComboBox, 'SpwnAnm')
        self.customize = self.findChild(QCheckBox, 'customize')

        self.new.triggered.connect(self.reset)
        self.open.triggered.connect(self.Open)
        self.health.lineEdit().setReadOnly(True)
        self.map.currentIndexChanged.connect(self.mapInfo)
        self.customize.clicked.connect(self.chucked)
        self.show()
    def reset(self):
        self.name.setText('')
        self.tri.setChecked(False)
        self.health.setValue(3)
        self.coordYb.setValue(0)
        self.coordYs.setValue(24)
        self.coordXb.setValue(1)
        self.coordXs.setValue(248)
        self.map.setCurrentIndex(0)
        self.anm.setCurrentIndex(0)
        self.customize.setChecked(False)
        self.coordYb.setEnabled(False)
        self.coordYs.setEnabled(False)
        self.coordXb.setEnabled(False)
        self.coordXs.setEnabled(False)
        self.anm.setEnabled(False)
    def Open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open .sav File', '', 'mGBA Save Files (*.sav);; All Files (*)')

        if fname:
            file = open(fname[0], 'r+b')
            file.seek(301)
            health = ord(file.read(1)) / 8
            file.seek(258)
            name = file.read(6)
            man = name[::-1]
            name = man.rstrip(bytes.fromhex('00'))
            man = name.decode()
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()
