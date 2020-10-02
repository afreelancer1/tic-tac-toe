#!/usr/bin/env python3

import random

board = []

for i in range(3):
	board.append([1,1,1])

def enter():
	'''Getting user's move'''
	try:
		inp = input("Enter Row and Column: ")
		r, c = int(inp[0])-1, int(inp[1])-1
		if board[r][c] == 1:
			board[r][c] = 0
		else:
			print("Move not allowed")
			enter()
	except:
		print("Invalid Input")
		enter()
	move()
	draw()

def move():
	'''Getting AI move'''
	try:
		r, c = random.randint(0,2), random.randint(0,2)
		if board[r][c] == 1:
			board[r][c] = 2
		else:
			move()
	except:
		print("Game Over!")

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
	for i in range(3):
		if (sum(board[i]) == 6) or (board[0][i]+board[1][i]+board[2][i] == 6) or (board[0][0]+board[1][1]+board[2][2] == 6) or (board[0][2]+board[1][1]+board[2][0] == 6):
			print("You lose!")
			return 1
			break
		if (sum(board[i]) == 0) or (board[0][i]+board[1][i]+board[2][i] == 0) or (board[0][0]+board[1][1]+board[2][2] == 0) or (board[0][2]+board[1][1]+board[2][0] == 0):
			print("You win!")
			return 1
			break

draw()
