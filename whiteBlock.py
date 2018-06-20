#!/usr/bin/env python3

from block import Block

class WhiteBlock(Block):
    def __init__(self):
        Block.__init__(self)
        self.setStyleSheet('background: white')