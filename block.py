#!/usr/bin/env python3

import sys
from PySide2.QtWidgets import QFrame, QLabel
from PySide2.QtCore import Qt

class Block(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setAlignment(Qt.AlignCenter)
        self.show()

    def setKey(self, key=None):
        self.key = key

    def setOccupied(self, what=False):
        self.occupied = what

    def setPosition(self, position=None):
        self.position = position

    def setFirstTurn(self, what=True):
        self.firstTurn = what

    def setColor(self, color=None):
        self.color = color

    def setActivated(self, what):
        self.activated = what

    def haveActivated(self):
        return self.activated
    
    def getColor(self):
        return self.color

    def isFirstTurn(self):
        return self.firstTurn
    
    def getKey(self):
        return self.key
    
    def getPosition(self):
        return self.position

    def haveOccupied(self):
        return self.occupied