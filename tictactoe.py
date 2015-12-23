'''
Tic Tac Toe game

Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal. The program should let the players take turns to input their moves. The program should report the outcome of the game.

During your interview, you will pair on adding support for a computer player to your game.
'''

from copy import copy
from itertools import permutations

# board = [['00', '01', '02'],
#          ['10', '11', '12'],
#          ['20', '21', '22']]


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def play(m, player=None):
    while True:
        a = raw_input('Player %s: Enter x (0, 1, or 2) and y (0, 1, or 2): \n' % player)
        a = tuple([int(c) for c in a if c.isalnum()])

        if a not in [(x, y) for x in range(3) for y in range(3)]:
           print 'Invalid coordinates. Try again.'
           print 'Choose from: ', list(permutations([0, 1, 2], 2))
           continue
        elif m[a[0]][a[1]] == 'X' or m[a[0]][a[1]] == 'Y':
    	    print "Sorry, that's already been played."
            continue
        else:
            m[a[0]][a[1]] = player # Update board
            return m      


def check_board(board, last):
    message = ''.join(['Game over. ', last, ' wins. Congratulations ', last, '!'])
    
    last = [last]*3 # EG, ['X', 'X', 'X']

    print '\n'
    for i, e in enumerate(('  |  '.join(c for c in r) for r in m)):
    	print '  ', e
    	if i < 2:
    		print '  ', '_____________\n'
    print '\n'

    # Horizontal
    for y in range(3):
    	if [board[y][x] for x in range(3)] == last:
        	print message
        	return False

    # Vertical
    for x in range(3):
    	if [board[y][x] for y in range(3)] == last:
        	print message
        	return False
    
    # Diagonal
    if [board[0][0], board[1][1], board[2][2]] == last:
        print message
        return False    	

    # Diagonal up
    if [board[2][0], board[1][1], board[0][2]] == last:
        print message
        return False


def check(state, m):
    if state == False:
    	a = raw_input('Play again? (y or n) \n')
        if a == 'y' or a == 'Y':
        	m = copy(board)
        	return m
        else:
            print 'Thanks for playing!'
            return False     	




m = copy(board)
playon = True
while playon == True: 
    
    m = play(m, player='X')
    state = check_board(m, 'X')
    if state == False:
        playon = check(state, m)
        if playon == False:
            break             

    m = play(m, player='O')
    state = check_board(m, 'O')
    if state == False:
        playon = check(state, m)
        if playon == False:
            break
        else:
            m = copy(board)
            print '\n', '\n'.join(str(r) for r in m), '\n'
