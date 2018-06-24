#!/usr/bin/env python3
from block import Block

class BlackBlock(Block):
    def __init__(self, parent=None):
        Block.__init__(self, parent)
        self.setStyleSheet('background: #FBB77E')