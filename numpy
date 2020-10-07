import random
import numpy as np 

board = np.ones((3,3), int)

def get_player():
	board = np.ones((3,3), int)
	choice = input("Choose Player One or Two?")
	if not choice == "1":
		player = "bot"
	else:
		player = "human"
	return player

player = get_player()

def move():
	global board, player
	draw()
	if (np.sum(np.where((board-2)<0, 0, board))) > 8:
		print("Draw!")
	elif player == "human":
		inp = input("Enter Row and Column: ")
		r, c = int(inp[0])-1, int(inp[1])-1
		if board[r][c] == 1:
			board[r][c] = 0
			player = "bot"
			check()
		else:
			print("Invalid input")
			move()
	elif player == "bot":
		r, c = random.randint(0,2), random.randint(0,2)
		if board[r][c] == 1:
			board[r][c] = 2
			player = "human"
			check()
		else:
			move()

def check():
	global board, player
	board_checker = board.T
	for i in range(3):
		if (np.sum(board[i]) == 6) or (np.sum(board_checker[i]) == 6) or (board[0][0]+board[1][1]+board[2][2] == 6) or (board[0][2]+board[1][1]+board[2][0] == 6):
			print("You lose!")
			draw()
			break
		if (np.sum(board[i]) == 0) or (np.sum(board_checker[i]) == 0) or (board[0][0]+board[1][1]+board[2][2] == 0) or (board[0][2]+board[1][1]+board[2][0] == 0):
			print("You Win!")
			draw()
			break
		elif i == 2:
			move()

def draw():
	'''Drawing the board'''
	mp = ["O", "_", "X"]
	for i in range(3):
		line = mp[board[i][0]] + "|" + mp[board[i][1]] + "|" + mp[board[i][2]]
		print(line)

move()
