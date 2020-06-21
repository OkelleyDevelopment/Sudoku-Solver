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
    # For the length of our array
    for i in range(len(board)):
        # we want to have this line after 3 rows, but
        # not at the start
        if i % 3 == 0 and i != 0:
            print("-------------------------")

        # Then for each column
        for j in range(len(board)):
            #print the pipe character to
            # breakup the 3 x 3 grids
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # If on the last iteration just the number
            # otherwise include the proper spacing
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def main():
    # this sample board was pulled from 
    # Arizona Daily Wildcat: Tuesday, Jan 17th 2006
    sample_board = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ]

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

    print("Arizona Daily Wildcat Board\n")
    display_board(sample_board)
    result = solved_board(sample_board)
    if result:
        print("\nSolution found!")
    else:
        print("\nNo solution found!")
    display_board(sample_board)
    print("\n\n")

    print("Hardest Board from Design Manual")
    display_board(sample_board1)
    result = solved_board(sample_board1)
    if result:
        print("\nSolution found!")
    else:
        print("\nNo solution found")
    display_board(sample_board1)


if __name__ == '__main__':
    main()
