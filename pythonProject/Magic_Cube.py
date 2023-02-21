import Board
import random
from Shape import Shape

score = 0
board = Board.create_board()
game_over = False
while not game_over:
    shape_number = random.randint(0, 10)  # generate a random number to get a random shape
    curr = Shape(shape_number)
    print(curr.get_shape_type())
    col = int(input("Choose the column to drop the shape"))
    row = int(input("Choose the row to drop the shape"))
    if Board.is_valid_location(board, col, row):
        game_over = Board.shape_drop_piece(board, curr.get_shape_type(), row, col)
        for r in range(Board.BOARD_WIDTH):
            score += Board.delete_col_if_filled(board, col)
        for r in range(Board.BOARD_HEIGHT):
            score += Board.delete_row_if_filled(board, r)
    else:
        game_over = True

    if game_over:
        print("Can't Put There! Game Over!")
        print("Final Score:" + str(score))
    else:
        Board.print_board(board)
        print("Current Score:" + str(score))
