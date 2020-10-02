#!/usr/bin/env python3

import random


ai = {}
steps = ""
board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

def enter():
	'''Getting user's move'''
	global steps
	try:
		inp = input("Enter Row and Column: ")
		r, c = int(inp[0])-1, int(inp[1])-1
		if board[r][c] == 1:
			board[r][c] = 0
			steps = steps + str(r) + str(c)
			move()
		else:
			print("Move not allowed")
			enter()
	except:
		print("Invalid Input")
		enter()
	draw()

def move():
	'''Getting AI move'''
	global steps
	r, c = random.randint(0,2), random.randint(0,2)
	if board[r][c] == 1:
		step = steps + str(r) + str(c)
		if step in ai and not (ai[step] is None):
			if ai[step] >= 0:
				board[r][c] = 2
			else:
				move()
		else:
			ai[step] = 0
			board[r][c] = 2
		steps = step
	elif len(steps)==18:
		check()
	else:
		move()

def draw():
	'''Drawing the board'''
	mp = ["O", "_", "X"]
	for i in range(3):
		line = mp[board[i][0]] + "|" + mp[board[i][1]] + "|" + mp[board[i][2]]
		print(line)
	result = check()
	if not result == 1:
		enter()


def check():
	'''Checking for Victory'''
	global steps, board
	for i in range(3):
		if (sum(board[i]) == 6) or (board[0][i]+board[1][i]+board[2][i] == 6) or (board[0][0]+board[1][1]+board[2][2] == 6) or (board[0][2]+board[1][1]+board[2][0] == 6):
			print("You lose!")
			while len(steps)>0:
				ai[steps] += 0.5
				steps = steps[:-4]
			next_game()
			return 1
			break
		if (sum(board[i]) == 0) or (board[0][i]+board[1][i]+board[2][i] == 0) or (board[0][0]+board[1][1]+board[2][2] == 0) or (board[0][2]+board[1][1]+board[2][0] == 0):
			print("You win!")
			while len(steps)>0:
				ai[steps] += -0.3
				steps = steps[:-4]
			next_game()
			return 1
			break
	if len(steps)==18:
		print("Draw!")
		while len(steps)>0:
			ai[steps] += 0.1
			steps = steps[:-4]
		next_game()
		return 1

def next_game():
	global board
	board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	again = input("Play again?")
	yes = ["yes","Yes","Y","y"]
	for i in yes:
		if again == i:
			draw()
			break
	else:
		print("Thanks for playing!")
		exit()

draw()
