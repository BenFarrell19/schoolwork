import numpy as np
import string


# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Pegathon                   |
# Ben Farrell                           |
# Last Modified: Month 12, 2021         |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# ---------------------------------------
# Start of Pegathon Class               |
# ---------------------------------------

class Pegathon:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1

    # ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer

    # ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

    # ---------------------------------------
    # The four missing methods go here.  Do |
    # not modify anything else.             |
    # --------------------------------------|

    def game_over(self):
        pass


    def legal_move(self, row_start, col_start, row_end, col_end):
        # for checking if jumping over peg
        moves_dic = {'diag_upr': [row_start - 1, col_start + 1], 'diag_downr': [row_start + 1, col_start + 1],
                     'diag_upl': [row_start - 1, col_start - 1], 'diag_downl': [row_start + 1, col_start - 1],
                     'up': [row_start - 1, col_start + 0], 'down': [row_start + 1, col_start + 0],
                     'left': [row_start + 0, col_start - 1], 'right': [row_start + 0, col_start + 1]}
        # for checking final peg position empty
        moves_dic_f = {'diag_upr': [row_start - 2, col_start + 2], 'diag_downr': [row_start + 2, col_start + 2],
                       'diag_upl': [row_start - 2, col_start - 2], 'diag_downl': [row_start + 2, col_start - 2],
                       'up': [row_start - 2, col_start + 0], 'down': [row_start + 2, col_start + 0],
                       'left': [row_start + 0, col_start - 2], 'right': [row_start + 0, col_start + 2]}
        for k, v in moves_dic_f.items():
            if v[0] == row_end and v[1] == col_end:
                move = k
        try:
            if int(self.board[moves_dic[move][0], moves_dic[move][1]]) == 1:
                if int(self.board[moves_dic_f[move][0], moves_dic_f[move][1]]) == 0:
                    return True
            else:
                return False
        except ValueError:
            return False

    def make_move(self, row_start, col_start, row_end, col_end):
        moves_dic = {'diag_upr': [row_start - 1, col_start + 1], 'diag_downr': [row_start + 1, col_start + 1],
                     'diag_upl': [row_start - 1, col_start - 1], 'diag_downl': [row_start + 1, col_start - 1],
                     'up': [row_start - 1, col_start + 0], 'down': [row_start + 1, col_start + 0],
                     'left': [row_start + 0, col_start - 1], 'right': [row_start + 0, col_start + 1]}
        moves_dic_f = {'diag_upr': [row_start - 2, col_start + 2], 'diag_downr': [row_start + 2, col_start + 2],
                       'diag_upl': [row_start - 2, col_start - 2], 'diag_downl': [row_start + 2, col_start - 2],
                       'up': [row_start - 2, col_start + 0], 'down': [row_start + 2, col_start + 0],
                       'left': [row_start + 0, col_start - 2], 'right': [row_start + 0, col_start + 2]}
        for k, v in moves_dic_f.items():
            if v[0] == row_end and v[1] == col_end:
                move = k
        self.board[moves_dic[move][0], moves_dic[move][1]] = False
        self.board[row_start, col_start] = False
        self.board[row_end, col_end] = True




# ---------------------------------------
# End of Pegathon Class                 |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer


# ---------------------------------------

def main():
    print("Welcome to Pegathon!")
    print("-----------------------------------\n")

    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1
    game = Pegathon(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()


# ---------------------------------------

main()
