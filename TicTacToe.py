from random import randint
board = []
for x in range (3):
    board.append(['#'] * 3)
def print_board(board):
    for row in board:
        print " ".join(row)


    
print "lets play!!"
print_board(board)
for x in range(9):
    row = int(raw_input("row:"))
    col = int(raw_input("col:"))
    board[row][col] = 'X'
    print_board(board)
    if ( board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' ) or \
       ( board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' ) or \
       ( board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' ) or \
       ( board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' ) or \
       ( board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' ) or \
       ( board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' ):
           print 'You Win!!'
           break
    
    print "comp's turn:"
    random_row = randint(0,2)
    random_col = randint(0,2)
    while board[row][col] == board[random_row][random_col] or \
          board[random_row][random_col] == "0":
          random_row = randint(0,2)
          random_col = randint(0,2)
        
    board[random_row][random_col] = "0"
    print_board(board)
     
raw_input()        
