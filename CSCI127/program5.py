import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Pegathon                   |
# Your Name(, Your Partner's Name)      |
# Last Modified: Month __, 20__         |
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
