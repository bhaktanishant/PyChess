#!/usr/bin/env python3

from param import parameter

class Moves:

	def __init__(self, block, blocks):
		self.block = block
		self.blocks = blocks
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
			checkNextBlock = True
			for i in range(2):
				if checkNextBlock:
					result = self.blockAvailable((position[0] +i+1, position[1]))
					canOccupy = result[0]
					checkNextBlock = result[1]
					if canOccupy:
						maxMoves.append((position[0] +i+1, position[1]))
		elif self.blockAvailable((position[0] +1, position[1]))[0]:
				maxMoves.append((position[0] +1, position[1]))
		return maxMoves
	
	def whitePawnMove(self, position):
		maxMoves = []
		if self.block.isFirstTurn():
			checkNextBlock = True
			for i in range(2):
				if checkNextBlock:
					result = self.blockAvailable((position[0] -i-1, position[1]))
					canOccupy = result[0]
					checkNextBlock = result[1]
					if canOccupy:
						maxMoves.append((position[0] -i-1, position[1]))
		elif self.blockAvailable((position[0] -1, position[1]))[0]:
			maxMoves.append((position[0] -1, position[1]))
		return maxMoves

	def elephantMove(self, position):
		maxMoves = []
		i = 1
		checkNextBlock = True
		while position[1] +i < 8:
			if checkNextBlock:
				result = self.blockAvailable((position[0], position[1] + i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0], position[1] + i))
			i = i + 1
		i = 1
		checkNextBlock = True
		while position[0] +i < 8:
			if checkNextBlock:
				result = self.blockAvailable((position[0] + i, position[1]))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] + i, position[1]))
			i = i + 1
		i = 1
		checkNextBlock = True
		while position[1] -i >= 0:
			if checkNextBlock:
				result = self.blockAvailable((position[0], position[1] - i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0], position[1] - i))
			i = i + 1
		i = 1
		checkNextBlock = True
		while position[0] -i >= 0:
			if checkNextBlock:
				result = self.blockAvailable((position[0] - i, position[1]))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] - i, position[1]))
			i = i + 1		
		return maxMoves

	def horseMove(self, position):
		maxMoves = []
		if position[0] +2 >= 0 and position[1] +1 >= 0 and position[0] +2 < 8 and position[1] +1 < 8:
			if self.blockAvailable((position[0] +2,  position[1] +1))[0]:
				maxMoves.append((position[0] +2,  position[1] +1))
		if position[0] +2 >= 0 and position[1] -1 >= 0 and position[0] +2 < 8 and position[1] -1 < 8:
			if self.blockAvailable((position[0] +2,  position[1] -1))[0]:
				maxMoves.append((position[0] +2,  position[1] -1))
		if position[0] -2 >= 0 and position[1] +1 >= 0 and position[0] -2 < 8 and position[1] +1 < 8:
			if self.blockAvailable((position[0] -2,  position[1] +1))[0]:
				maxMoves.append((position[0] -2,  position[1] +1))
		if position[0] -2 >= 0 and position[1] -1 >= 0 and position[0] -2 < 8 and position[1] -1 < 8:
			if self.blockAvailable((position[0] -2,  position[1] -1))[0]:
				maxMoves.append((position[0] -2,  position[1] -1))
		if position[0] +1 >= 0 and position[1] +2 >= 0 and position[0] +1 < 8 and position[1] +2 < 8:
			if self.blockAvailable((position[0] +1,  position[1] +2))[0]:
				maxMoves.append((position[0] +1,  position[1] +2))
		if position[0] -1 >= 0 and position[1] +2 >= 0 and position[0] -1 < 8 and position[1] +2 < 8:
			if self.blockAvailable((position[0] -1,  position[1] +2))[0]:
				maxMoves.append((position[0] -1,  position[1] +2))
		if position[0] +1 >= 0 and position[1] -2 >= 0 and position[0] +1 < 8 and position[1] -2 < 8:
			if self.blockAvailable((position[0] +1,  position[1] -2))[0]:
				maxMoves.append((position[0] +1,  position[1] -2))
		if position[0] -1 >= 0 and position[1] -2 >= 0 and position[0] -1 < 8 and position[1] -2 < 8:
			if self.blockAvailable((position[0] -1,  position[1] -2))[0]:
				maxMoves.append((position[0] -1,  position[1] -2))
		return maxMoves

	def camelMoves(self, position):
		maxMoves = []
		i = 1
		checkNextBlock = True
		while position[0] +i < 8 and position[1] +i < 8:
			if checkNextBlock:
				result = self.blockAvailable((position[0] +i, position[1] +i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] +i, position[1] +i))
			i = i +1
		i = 1
		checkNextBlock = True
		while position[0] -i >= 0 and position[1] -i >= 0:
			if checkNextBlock:
				result = self.blockAvailable((position[0] -i, position[1] -i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] -i, position[1] -i))
			i = i +1
		i = 1
		checkNextBlock = True
		while position[0] +i < 8 and position[1] -i >= 0:
			if checkNextBlock:
				result = self.blockAvailable((position[0] +i, position[1] -i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] +i, position[1] -i))
			i = i +1
		i = 1
		checkNextBlock = True
		while position[0] -i >= 0 and position[1] +i < 8:
			if checkNextBlock:
				result = self.blockAvailable((position[0] -i, position[1] +i))
				canOccupy = result[0]
				checkNextBlock = result[1]
				if canOccupy:
					maxMoves.append((position[0] -i, position[1] +i))
			i = i +1
		return maxMoves

	def queenMove(self, position):
		maxMoves = []
		if position[0] +1 < 8:
			if self.blockAvailable((position[0] +1, position[1]))[0]:
				maxMoves.append((position[0] +1, position[1]))
		if position[0] -1 >= 0:
			if self.blockAvailable((position[0] -1, position[1]))[0]:
				maxMoves.append((position[0] -1, position[1]))
		if position[1] +1 < 8:
			if self.blockAvailable((position[0], position[1] +1))[0]:
				maxMoves.append((position[0], position[1] +1))
		if position[0] -1 >= 0:
			if self.blockAvailable((position[0], position[1] -1))[0]:
				maxMoves.append((position[0], position[1] -1))
		if position[0] +1 < 8 and position[1] +1 < 8:
			if self.blockAvailable((position[0] +1, position[1] +1))[0]:
				maxMoves.append((position[0] +1, position[1] +1))
		if position[0] -1 >= 0 and position[1] -1 >= 0:
			if self.blockAvailable((position[0] -1, position[1] -1))[0]:
				maxMoves.append((position[0] -1, position[1] -1))
		if position[0] +1 < 8 and position[1] -1 >= 0:
			if self.blockAvailable((position[0] +1, position[1] -1))[0]:
				maxMoves.append((position[0] +1, position[1] -1))
		if position[0] -1 >= 0 and position[1] +1 < 8:
			if self.blockAvailable((position[0] -1, position[1] +1))[0]:
				maxMoves.append((position[0] -1, position[1] +1))
		return maxMoves

	def kingMove(self, position):
		return self.elephantMove(position) + self.camelMoves(position)

	def blockAvailable(self, position):
		block = self.blocks[position]
		if block.haveOccupied():
			print("have occupied")
			if block.getColor() == self.block.getColor():
				print("with same color")
				return (False, False)
			else:
				print("with other color")
				return (True, False)
		else:
			print("not occupied")
			return (True, True)
