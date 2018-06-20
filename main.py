#!/usr/bin/env python3

import sys, os
from blackBlock import BlackBlock
from whiteBlock import WhiteBlock
from PySide2.QtWidgets import QApplication, QWidget, QGridLayout
from PySide2.QtGui import QPixmap

class Board(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Chess")
        drawableDir = os.getcwd() + "/res/drawable/"
        self.BLACK_PAWN = drawableDir + "black_pawn.png"
        self.BLACK_ELEPHANT = drawableDir + "black_elephant.png"
        self.BLACK_HORSE = drawableDir + "black_horse.png"
        self.BLACK_CAMEL = drawableDir + "black_camel.png"
        self.BLACK_KING = drawableDir + "black_king.png"
        self.BLACK_QUEEN = drawableDir + "black_queen.png"
        self.WHITE_PAWN = drawableDir + "white_pawn.png"
        self.WHITE_ELEPHANT = drawableDir + "white_elephant.png"
        self.WHITE_HORSE = drawableDir + "white_horse.png"
        self.WHITE_CAMEL = drawableDir + "white_camel.png"
        self.WHITE_KING = drawableDir + "white_king.png"
        self.WHITE_QUEEN = drawableDir + "white_queen.png"
        self.initUI()

    def initUI(self):
        gridLayout = QGridLayout()
        gridLayout.setMargin(0)
        gridLayout.setSpacing(0)
        blackTurn = True
        blocks = []
        pixMap = QPixmap()
        for i in range(8):
            for j in range(8):
                if(blackTurn):
                    block = BlackBlock()
                else:
                    block = WhiteBlock()
                if j != 7:
                    blackTurn = not blackTurn
                if (i == 0 and j == 0) or (i == 0 and j == 7):
                    block = self.setKey(block, pixMap, self.BLACK_ELEPHANT)
                if (i == 0 and j == 1) or (i == 0 and j == 6):
                    block = self.setKey(block, pixMap, self.BLACK_HORSE)
                if (i == 0 and j == 2) or (i == 0 and j == 5):
                    block = self.setKey(block, pixMap, self.BLACK_CAMEL)
                if (i == 0 and j == 3):
                    block = self.setKey(block, pixMap, self.BLACK_QUEEN)
                if (i == 0 and j == 4):
                    block = self.setKey(block, pixMap, self.BLACK_KING)
                if i == 1:
                    block = self.setKey(block, pixMap, self.BLACK_PAWN)
                gridLayout.addWidget(block, i, j)
                blocks.append(block)

        self.setLayout(gridLayout)
        self.show()

    def setKey(self, block, pixMap, key):
        pixMap.load(key)
        block.setPixmap(pixMap.scaled(50, 50))
        block.setKey(key)
        return block

def main():
    app = QApplication(sys.argv)
    yoo = Board()
    app.exec_()

if __name__ == '__main__':
    main()