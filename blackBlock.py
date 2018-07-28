#!/usr/bin/env python3
from block import Block

class BlackBlock(Block):
    def __init__(self, parent=None):
        Block.__init__(self, parent)
        self.setOriginalBackGround()

    def setActivated(self, what):
        if what:
            self.setBackGround('#BFFFA3')
        else:
            self.setOriginalBackGround()
        self.activated = what

    def setOriginalBackGround(self):
        self.setBackGround('#FBB77E')