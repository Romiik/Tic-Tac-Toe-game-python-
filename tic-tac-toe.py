from IPython.display import clear_output
import random


def displayBoard(board):
    clear_output()
    print(board[7], '|', board[8], '|', board[9])
    print('--|---|--')
    print(board[4], '|', board[5], '|', board[6])
    print('--|---|--')
    print(board[1], '|', board[2], '|', board[3])


myList = ['#', ' ', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'X']
# displayBoard(myList)


def askPlayer(board, mark, no):
    print("#Player {}".format(no))
    print('Please Enter your choice (1-9):')
    position = int(input())
    while not position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Please Enter correct option:')
        position = int(input())
    while isOccupied(position, board):
        while not fullBoard(board):
            print('Please enter another board ')
            position = int(input())
        break
    store(board, position, mark)


def winCheck(board, mark):
    return ((board[7] == board[8] == board[9] == mark)or
            (board[4] == board[5] == board[6] == mark)or
            (board[1] == board[2] == board[3] == mark)or
            (board[7] == board[4] == board[1] == mark)or
            (board[5] == board[8] == board[2] == mark)or
            (board[6] == board[3] == board[9] == mark)or
            (board[7] == board[5] == board[3] == mark)or
            (board[9] == board[5] == board[1] == mark))


#isAns = winCheck(myList, 'X')
# print(isAns)
def fullBoard(board):
    for x in board:
        if x == ' ' or x == '':
            return False
    return True


#isFull = fullBoard(myList)
# print(isFull)
def isOccupied(position, board):
    return (board[position] == 'X' or board[position] == 'X')


def store(board, postion, mark):
    board[postion] = mark


def playgame():
    win = 0
    board = [' ']*10
    board[0] = '#'
    toss = random.randint(0, 1)
    if toss == 0:
        no1 = 1
        no2 = 2
    else:
        no1 = 2
        no2 = 1
    print('Player {} : Please select your mark --> X or O'.format(no1))
    mark1 = input()
    while mark1 != 'O' and mark1 != 'X':
        mark1 = input()
    if mark1 == 'X':
        mark2 = 'O'
    else:
        mark2 = 'X'
    while not fullBoard(board):
        askPlayer(board, mark1, no1)
        if winCheck(board, mark1):
            print('Congratulations player {}'.format(no1))
            win = 1
            displayBoard(board)
            break
        displayBoard(board)
        askPlayer(board, mark2, no2)
        if winCheck(board, mark2):
            print('Congratulations player {}'.format(no2))
            win = 1
            displayBoard(board)
            break
        displayBoard(board)
    if win == 0:
        print("DDDDDRRRRRAAAWWWWWW !!!!!!!")
    print('Would you like to play again? y or n ')
    choice = input()
    if choice == 'y':
        playgame()
    else:
        print('Have  a  nice  day !!!')


playgame()
