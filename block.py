#!/usr/bin/env python3

import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel


class Block(QLabel):
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)
        self.setFixedHeight(80)
        self.setFixedWidth(80)
        self.setAlignment(Qt.AlignCenter)
        self.show()

    def setKey(self, key):
        self.key = key

    def setOccupied(self, what):
        self.occupied = what

    def setPosition(self, position):
        self.position = position

    def setFirstTurn(self, what):
        self.firstTurn = what

    def setColor(self, color):
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
