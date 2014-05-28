from bunkerBoard import bunkerBoard
file = open('map.txt','r')
board = file.read()

bb = bunkerBoard(board)
bb.printBoard()
bb.findNest()