#!/usr/bin/env python3

import os
import sys
from functools import partial

from PySide2.QtCore import SIGNAL, QObject, Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QGridLayout, QWidget

from blackBlock import BlackBlock
from moves import Moves
from param import parameter
from whiteBlock import WhiteBlock


class Board(QWidget):

    BLACK_TURN = True

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Chess")
        self.param = parameter()
        self.initUI()

    def initUI(self):
        gridLayout = QGridLayout(self)
        gridLayout.setMargin(0)
        gridLayout.setSpacing(0)
        blackTurn = True
        blocks = {}
        pixMap = QPixmap()
        for i in range(8):
            for j in range(8):
                if(blackTurn):
                    block = BlackBlock(self)
                else:
                    block = WhiteBlock(self)
                if j != 7:
                    blackTurn = not blackTurn
                if (i == 0 and j == 0) or (i == 0 and j == 7):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_ELEPHANT)
                elif (i == 0 and j == 1) or (i == 0 and j == 6):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_HORSE)
                elif (i == 0 and j == 2) or (i == 0 and j == 5):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_CAMEL)
                elif (i == 0 and j == 3):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_QUEEN)
                elif (i == 0 and j == 4):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_KING)
                elif i == 1:
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.BLACK_PAWN)

                elif (i == 7 and j == 0) or (i == 7 and j == 7):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_ELEPHANT)
                elif (i == 7 and j == 1) or (i == 7 and j == 6):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_HORSE)
                elif (i == 7 and j == 2) or (i == 7 and j == 5):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_CAMEL)
                elif (i == 7 and j == 4):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_QUEEN)
                elif (i == 7 and j == 3):
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_KING)
                elif i == 6:
                    block = self.setValues(
                        block, pixMap, (i,  j), self.param.WHITE_PAWN)
                else:
                    block = self.setValues(block, pixMap, (i, j), None)
                gridLayout.addWidget(block, i, j)
                block.mousePressEvent = partial(self.clicked, block, blocks)
                blocks[(i, j)] = block
        self.show()

    def setValues(self, block, pixMap, position, key):
        if key is not None:
            pixMap.load(key)
            block.setPixmap(pixMap.scaled(50, 60))
            block.setKey(key)
            block.setOccupied(True)
            if "black" in key:
                block.setColor("black")
            else:
                block.setColor("white")
        else:
            block.setOccupied(False)
        block.setPosition(position)
        block.setActivated(False)
        block.setFirstTurn(True)
        return block

    def clicked(self, block, blocks, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if not block.haveActivated():
                for value in blocks.values():
                    value.setActivated(False)
                if block.haveOccupied():
                    block.setActivated(True)
                maxMoves = Moves(block, blocks)
                print(maxMoves.canRoamTo())
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yoYoHoneySingh = Board()
    app.exec_()
