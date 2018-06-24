#!/usr/bin/env python3

from param import parameter

class Moves:

	def __init__(self, block):
		self.block = block
		self.param = parameter()
	
	def canRoamTo(self):
		position = self.block.getPosition()
		if self.block.getKey() == self.param.BLACK_PAWN:
			return self.blackPawnMove(position)
		elif self.block.getKey() == self.param.WHITE_PAWN:
			return self.whitePawnMove(position)
		elif self.block.getKey() == self.param.BLACK_ELEPHANT or self.block.getKey() == self.param.WHITE_ELEPHANT:
			return self.elephantMove(position)
		elif self.block.getKey() == self.param.BLACK_HORSE or self.block.getKey() == self.param.WHITE_HORSE:
			return self.horseMove(position)
		elif self.block.getKey() == self.param.BLACK_CAMEL or self.block.getKey() == self.param.WHITE_CAMEL:
			return self.camelMoves(position)
		elif self.block.getKey() == self.param.BLACK_QUEEN or self.block.getKey() == self.param.WHITE_QUEEN:
			return self.queenMove(position)
		elif self.block.getKey() == self.param.BLACK_KING or self.block.getKey() == self.param.WHITE_KING:
			return self.kingMove(position)

	def blackPawnMove(self, position):
		maxMoves = []
		if self.block.isFirstTurn():
			for i in range(2):
				maxMoves.append((position[0] +i+1, position[1]))
		else:
			maxMoves.append((position[0] +1, position[1]))
		return maxMoves
	
	def whitePawnMove(self, position):
		maxMoves = []
		if self.block.isFirstTurn():
			for i in range(2):
				maxMoves.append((position[0] +i-1, position[1]))
		else:
			maxMoves.append((position[0] -1, position[1]))
		return maxMoves

	def elephantMove(self, position):
		maxMoves = []
		for i in range(8):
			if (position[0], i) != position:
				maxMoves.append((position[0], i))
		for j in range(8):
			if (j, position[1]) != position:
				maxMoves.append((j, position[1]))
		return maxMoves

	def horseMove(self, position):
		maxMoves = []
		if position[0] +2 >= 0 and position[1] +1 >= 0 and position[0] +2 < 8 and position[1] +1 < 8:
			maxMoves.append((position[0] +2,  position[1] +1))
		if position[0] +2 >= 0 and position[1] -1 >= 0 and position[0] +2 < 8 and position[1] -1 < 8:
			maxMoves.append((position[0] +2,  position[1] -1))
		if position[0] -2 >= 0 and position[1] +1 >= 0 and position[0] -2 < 8 and position[1] +1 < 8:
			maxMoves.append((position[0] -2,  position[1] +1))
		if position[0] -2 >= 0 and position[1] -1 >= 0 and position[0] -2 < 8 and position[1] -1 < 8:
			maxMoves.append((position[0] -2,  position[1] -1))
		if position[0] +1 >= 0 and position[1] +2 >= 0 and position[0] +1 < 8 and position[1] +2 < 8:
			maxMoves.append((position[0] +1,  position[1] +2))
		if position[0] -1 >= 0 and position[1] +2 >= 0 and position[0] -1 < 8 and position[1] +2 < 8:
			maxMoves.append((position[0] -1,  position[1] +2))
		if position[0] +1 >= 0 and position[1] -2 >= 0 and position[0] +1 < 8 and position[1] -2 < 8:
			maxMoves.append((position[0] +1,  position[1] -2))
		if position[0] -1 >= 0 and position[1] -2 >= 0 and position[0] -1 < 8 and position[1] -2 < 8:
			maxMoves.append((position[0] -1,  position[1] -2))
		return maxMoves

	def camelMoves(self, position):
		maxMoves = []
		i = 1
		while position[0] +i < 8 and position[1] +i < 8:
			maxMoves.append((position[0] +i, position[1] +i))
			i = i +1
		i = 1
		while position[0] -i >= 0 and position[1] -i >= 0:
			maxMoves.append((position[0] -i, position[1] -i))
			i = i +1
		i = 1
		while position[0] +i < 8 and position[1] -i >= 0:
			maxMoves.append((position[0] +i, position[1] -i))
			i = i +1
		i = 1
		while position[0] -i >= 0 and position[1] +i < 8:
			maxMoves.append((position[0] -i, position[1] +i))
			i = i +1
		return maxMoves

	def queenMove(self, position):
		maxMoves = []
		if position[0] +1 < 8:
			maxMoves.append((position[0] +1, position[1]))
		if position[0] -1 >= 0:
			maxMoves.append((position[0] -1, position[1]))
		if position[1] +1 < 8:
			maxMoves.append((position[0], position[1] +1))
		if position[0] -1 >= 0:
			maxMoves.append((position[0], position[1] -1))
		if position[0] +1 < 8 and position[1] +1 < 8:
			maxMoves.append((position[0] +1, position[1] +1))
		if position[0] -1 >= 0 and position[1] -1 >= 0:
			maxMoves.append((position[0] -1, position[1] -1))
		if position[0] +1 < 8 and position[1] -1 >= 0:
			maxMoves.append((position[0] +1, position[1] -1))
		if position[0] -1 >= 0 and position[1] +1 < 8:
			maxMoves.append((position[0] -1, position[1] +1))
		return maxMoves

	def kingMove(self, position):
		return self.elephantMove(position) + self.camelMoves(position)
