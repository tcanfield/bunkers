class bunkerBoard(object):	
	def __init__(self, bo):
		self.board = bo.replace(" ", "").split('\n')
		self.boardInput = bo
		
		##Find the boards size##
		self.boardHeight = int(self.board[0][0])
		self.boardWidth = int(self.board[0][1])
		
		##Remove size and leave only the board##
		del self.board[0]
		
		##Start all visited values false##
		self.boardVisited = [[False for i in range(0,self.boardHeight)] for j in range(0,self.boardWidth)]
		
	def printBoard(self):
		print("Height: ", self.boardHeight)
		print("Width: ", self.boardWidth)
		print("Board: ")
		for x in range(0,self.boardHeight):
			print(self.board[x])
			
		print(self.boardVisited)
	
	def findNest(self):
		self.nestRow = None
		self.nestCol = None
		for row in range(0, self.boardHeight):
			for col in range(0, self.boardWidth):
				if self.board[row][col] == "*":
					self.nestRow = row
					self.nestCol = col
					
		print("Nest Row: ", self.nestRow)
		print("Nest Col: ", self.nestCol)