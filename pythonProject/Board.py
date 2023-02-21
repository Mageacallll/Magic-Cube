import numpy as np

BOARD_WIDTH = 9  # the width of the board
BOARD_HEIGHT = 9  # the height of the board


# note that board[y-cor][x-cor]
def create_board():
    board = np.zeros((BOARD_WIDTH, BOARD_HEIGHT))
    return board


# drop the piece of cube
# input Board, int row, int col, row in range(BOARD_WIDTH), col in range(BOARD_HEIGHT)
# change the board and return none
def drop_piece(board, row, col):
    board[row][col] = 1


# determine if it is a valid row to drop in the cube
# input Board, int col in range(BOARD_WIDTH)
# return boolean
def is_valid_location(board, col, row):
    return board[row][col] == 0


# determine if it is a valid cor to drop in a piece
def is_valid_drop(board, row, col):
    return row <= BOARD_WIDTH - 1 and col <= BOARD_HEIGHT - 1 and board[row][col] == 0 and row >= 0 and col >= 0


# get the next plot that is valid for drop in
# def get_next_open_row(board, col, shape_type):
#     if shape_type == "o" or shape_type == "i" or shape_type == "I":
#         for r in range(BOARD_HEIGHT):
#             if board[r][col] == 0:
#                 return r
#     else:
#         if shape_type == "l" or shape_type == "S" or shape_type == "O":
#             for r in range(BOARD_HEIGHT):
#                 if board[r][col] == 0 and board[r][col+1] == 0:
#                     return r
#         else:
#             for r in range(BOARD_HEIGHT):
#                 if board[r][col] == 0 and board[r][col+1] == 0 and board[r][col+2] == 0:
#                     return r


# print the board in the way that flips across the x-axis
def print_board(board):
    print(np.flip(board, 0))


# return if the column has been filled or nor
def col_filled(board, col):
    result = True
    for r in range(BOARD_HEIGHT):
        result = result and board[r][col] == 1
    return result


# return if the row has been filled or not
def row_filled(board, row):
    result = True
    for r in range(BOARD_WIDTH):
        result = result and board[row][r] == 1
    return result


# delete the col if that col is already filled, otherwise do nothing
# Board, int col
# change the board, return 10 points if deleted
def delete_col_if_filled(board, col):
    if col_filled(board, col):
        for r in range(BOARD_HEIGHT):
            board[r][col] = 0
        return 10
    else:
        return 0


# delete the col if that col is already filled, otherwise do nothing
# Board, int col
# change the board, return 10 points if deleted
def delete_row_if_filled(board, row):
    if row_filled(board, row):
        for r in range(BOARD_WIDTH):
            board[row][r] = 0
        return 10
    else:
        return 0


# drop piece according to the shape
# input board, str shape_type, int row, int col
# change the board, return none
def shape_drop_piece(board, shape_type, row, col):
    result = False
    if shape_type == "o":
        drop_piece(board, row, col)
    elif shape_type == "O":
        if is_valid_drop(board, row + 1, col) and is_valid_drop(board, row, col + 1) and is_valid_drop(board, row + 1,
                                                                                                       col + 1):
            drop_piece(board, row, col)
            drop_piece(board, row + 1, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row + 1, col + 1)
        else:
            result = True
    elif shape_type == "i":
        if is_valid_drop(board, row + 1, col):
            drop_piece(board, row, col)
            drop_piece(board, row + 1, col)
        else:
            result = True
    elif shape_type == "l":
        if is_valid_drop(board, row, col + 1) and is_valid_drop(board, row + 1, col) and is_valid_drop(board, row + 2,
                                                                                                       col):
            drop_piece(board, row, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row + 1, col)
            drop_piece(board, row + 2, col)
        else:
            result = True
    elif shape_type == "S":
        if is_valid_drop(board, row, col + 1) and is_valid_drop(board, row + 1, col + 1) and is_valid_drop(board,
                                                                                                           row + 1,
                                                                                                           col + 2):
            drop_piece(board, row, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row + 1, col + 1)
            drop_piece(board, row + 1, col + 2)
        else:
            result = True
    elif shape_type == "L":
        if is_valid_drop(board, row, col + 1) and is_valid_drop(board, row, col + 2) and is_valid_drop(board, row + 1,
                                                                                                       col) and \
                is_valid_drop(
                    board, row + 2, col):
            drop_piece(board, row, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row, col + 2)
            drop_piece(board, row + 1, col)
            drop_piece(board, row + 2, col)
        else:
            result = True
    elif shape_type == "I":
        if is_valid_drop(board, row + 1, col) and is_valid_drop(board, row + 2, col) and is_valid_drop(board, row + 3,
                                                                                                       col):
            drop_piece(board, row, col)
            drop_piece(board, row + 1, col)
            drop_piece(board, row + 2, col)
            drop_piece(board, row + 3, col)
        else:
            result = True
    elif shape_type == "T":
        if is_valid_drop(board, row, col+1) and is_valid_drop(board, row, col+2) and is_valid_drop(board, row-1, col+1):
            drop_piece(board, row, col)
            drop_piece(board, row, col+1)
            drop_piece(board, row, col+2)
            drop_piece(board, row-1, col+1)
        else:
            result = True
    elif shape_type == "J":
        if is_valid_drop(board, row, col+1) and is_valid_drop(board, row+1, col+1) and \
                is_valid_drop(board, row+2, col+1):
            drop_piece(board, row, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row + 1, col + 1)
            drop_piece(board, row + 2, col + 1)
        else:
            result = True
    elif shape_type == "Z":
        if is_valid_drop(board, row, col+1) and is_valid_drop(board, row-1, col+1) and \
                is_valid_drop(board, row-1, col+2):
            drop_piece(board, row, col)
            drop_piece(board, row, col + 1)
            drop_piece(board, row - 1, col + 1)
            drop_piece(board, row - 1, col + 2)
        else:
            result = True
    elif shape_type == "-":
        if is_valid_drop(board, row, col+1):
            drop_piece(board, row, col)
            drop_piece(board, row, col+1)
        else:
            result = True

    return result
