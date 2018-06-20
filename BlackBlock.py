#!/usr/bin/env python3
from Block import Block

class BlackBlock(Block):
    def __init__(self):
        Block.__init__(self)
        self.setStyleSheet('background: #FBB77E')