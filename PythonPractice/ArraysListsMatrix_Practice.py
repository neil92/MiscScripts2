
ROWS=2
COLS=2
board = []

for row in range(0, ROWS):
	board.append([])
	for col in range(0, COLS):
		board[row].append(None)
	

print board

for row in range (0, ROWS):
	for col in range (0, COLS):
		if not (board[row][col]):
			board[row][col] = (row+col)
			
print board