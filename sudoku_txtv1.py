# board = [
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# ]
#Navigate Sudoku board by board[row][column]
#Vertical lines to separate after board[row][2]; and horizontal lines to separate after board[2]
#Vertical and horizontal lines to define the 9units x 9units Sudoku grid (81 squares total)
sudoku_board = [
    [5, 0, 0, 1, 8, 0, 0, 7, 0],
    [0, 0, 7, 2, 9, 0, 5, 4, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 5, 0, 6, 0, 0, 9, 8, 0],
    [7, 0, 0, 9, 0, 0, 3, 0, 4],
    [0, 9, 6, 3, 0, 8, 2, 1, 5],
    [0, 0, 5, 8, 0, 0, 0, 0, 6],
    [1, 4, 0, 0, 6, 0, 0, 0, 2],
    [0, 3, 0, 0, 2, 7, 1, 0, 0]]     #sample sudoku board, 0 means empty

#define function that takes a board as an argument and returns a printed
#9x9 board fashioned as a Sudoku board.
def make_board(board):
    for row in range(len(board)):
        if row % 3 == 0:      
            print ("-------------------------")             #prints a horizontal line before row % 3 == 0, which includes topmost border.
        for column in range(len(board[row])):
            if column % 3 == 0:
                print ("|", board[row][column], end = " ")  #prints vertical line before column % 3 == 0; end parameter replaces '\n' with " " so that after board[row][column],...        
            elif column == 8:                               #...the print statement ends on " ", and this allows other iteration variables to append to the print statement.
                print (board[row][column], "|")             #prints board[row][8] and the rightmost border of the sudoku board.
            else:
                print (board[row][column], end = " ")       #for column % 3 != 0, iteration variable will continue to append to the same print statement since '\n' is replaced
        if row == 8:                                        #...with " ". Print statement will not have any '\n' , so more iteration variables can still append to the same statement.
            print ("-------------------------")             #prints lowest border of sudoku board, comes last so row[8] can be populated first.
        else:
            continue

make_board(sudoku_board)

