# A simple text-based soduko solver 
#
# Author: Nicholas O'Kelley
# Date: June 20, 2020

def locate(board):
    #print("Locating valid entry...")
    # For each row, col 
    # Find each cell that contains a zero and
    # then return that (row, col) pair
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                #print("Valid entry located.")
                return (i,j)
    # Return none if there is no more 
    # cells left to fill
    return None


def solved_board(board):
    #print("Beginning to find a solution...")
    # To begin to solve, we find the next available cell
    located = locate(board)

    
    if not located:
        # return true if the board is filled
        return True
    else:
        # Separate the tuple into 
        # the respective variables
        row, col = located


    # Now that we have our grid point, we need 
    # to fill in the 9 digits for each of the sub
    # divisions
    for i in range(1, 10):
        if check_validity(board, i, (row,col)):
            # Set the current cell to i if it passes the validity check
            board[row][col] = i
            
            if solved_board(board):
                # Check for none and return true 
                # meaning the board is filled
                return True

            # this allows us to reset the board
            # if the previous iteration failed
            board[row][col] = 0
    # return false for an 
    # unsolvable solution or board
    return False


def check_validity(board, num, position):

    # Check the row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check the column 
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False
    
    # Get the cords in the matrix
    x = position[1] // 3
    y = position[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False
        
    return True


def display_board(board):
    message = ""
    # For the length of our array
    for i in range(len(board)):
        # we want to have this line after 3 rows, but
        # not at the start
        if i % 3 == 0 and i != 0:
            print("-------------------------")
            message = message + "-------------------------\n"

        # Then for each column
        for j in range(len(board)):
            #print the pipe character to
            # breakup the 3 x 3 grids
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                message = message + " | "
            # If on the last iteration just the number
            # otherwise include the proper spacing
            if j == 8:
                print(board[i][j])
                message = message + str(board[i][j]) + "\n"
            else:
                print(str(board[i][j]) + " ", end="")
                message = message + str(board[i][j]) + " "
    return message


def process_output(board, isBoardSolved):

    write_to_file = ""
    if isBoardSolved:
        print("\nSolution found!\n")
        write_to_file = write_to_file + "\nSolution found!\n"
    else:
        print("\nNo solution found!")
        write_to_file = write_to_file + "\nNo Solution Found\n"
    write_to_file = write_to_file + display_board(board)
    print("\n\n")
    write_to_file = write_to_file + "\n\n"

    return write_to_file

def read_file(file):
    try:
        write_to_file = ""
        board = [[0 for x in range(9)] for y in range(9)]

        with open(file) as input_board:
            write_to_file = write_to_file + input_board.readline()
            i = 0
            j = 0
            for line in input_board:
                line.rstrip()
                j = 0
                for c in line:
                    board[i][j] = int(c)
                    j = j + 1
                    if j == 9:
                        i = i + 1
                        break
                if i == 9:
                    break
        return write_to_file,board
    except FileNotFoundError:
        raise FileNotFoundError("ERROR: Could not find that board. Try again.")

def write_file(message):
    output = "./solved_boards/" + input("Enter output file name: ").strip() + ".txt"
    with open(output, "w+") as f:
        for line in message:
            f.write(line)


def main():
    text_file = ("./unsolved_boards/" + input("Enter file: "))
    message, board = read_file(text_file)
    message = message + display_board(board)
    result = solved_board(board)
    message = message + process_output(board, result)
    write_file(message)

    # This sample board was pulled from 
    # the book: The Algorithm Design Manual
    sample_board1 = [
            [0, 0, 0, 0, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 3, 5, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 7, 0],
            [7, 0, 0, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 4, 0, 0, 8, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 4, 0],
            [0, 5, 0, 0, 0, 0, 6, 0, 0]
    ]


if __name__ == '__main__':
    main()
