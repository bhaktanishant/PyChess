#!/usr/bin/env python3

import sys
from PySide2.QtWidgets import QFrame, QLabel
from PySide2.QtCore import Qt

class Block(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setAlignment(Qt.AlignCenter)
        self.show()

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setPosition(self, i, j):
        self.position = (i, j)
    
    def getPosition(self):
        return self.position