import random
import math

# Global constant
SPACE = " "
DIRECTION_LIST = ["left", "right", "up", "down"]

# Global variable
g_puzzle = []
g_solved = []
g_size = 0
g_side_len = 0
step = 0

def create_puzzle(p_size):
    global g_puzzle
    global g_size
    g_size = p_size
    global g_side_len
    global g_solved
    g_side_len = int(math.sqrt(g_size))
    g_puzzle = [x for x in range(1, g_size)]
    g_puzzle.append(SPACE)
    g_solved = g_puzzle[:]

def randomize_puzzle():
    global g_puzzle   
    for i in range(g_size**2):
        valid_dirct = [x for x in DIRECTION_LIST if is_valid(x)]
        direction = random.choice(valid_dirct)
        slid(direction)

def print_puzzle():
    index = 0
    for num in g_puzzle:
        index += 1
        print("{:>2}".format(num), end=" ")
        if index % g_side_len == 0: print("")

def is_valid(p_direction):
    pos = g_puzzle.index(SPACE)
    if p_direction == "left":
        if (pos+1) % g_side_len == 0:
            return False
    elif p_direction == "right":
        if pos % g_side_len == 0:
            return False
    elif p_direction == "up":
        if pos >= (g_size - g_side_len):
            return False
    elif p_direction == "down":
        if pos < g_side_len:
            return False
    return True

# Make a sliding move.
def slid(p_direction):
    pos = g_puzzle.index(SPACE)
    if p_direction == "left":
        g_puzzle[pos], g_puzzle[pos+1] = g_puzzle[pos+1], g_puzzle[pos]
    elif p_direction == "right":
        g_puzzle[pos], g_puzzle[pos-1] = g_puzzle[pos-1], g_puzzle[pos]
    elif p_direction == "up":
        g_puzzle[pos], g_puzzle[pos+g_side_len] = g_puzzle[pos+g_side_len], g_puzzle[pos]
    elif p_direction == "down":
        g_puzzle[pos], g_puzzle[pos-g_side_len] = g_puzzle[pos-g_side_len], g_puzzle[pos]
    
def is_alpha_list(p_list):
    for element in p_list:
        if not element.isalpha():
            return False
    return True

def determine_letters_for_directions():
    while True:
        letters = input("Enter four different letters for left, right, up, and down directions (seperate them by space): ").lower().split()
        if not is_alpha_list(letters):
            print("Please enter letters only!")
            continue
        elif len(set(letters)) != 4:
            print("Please enter four different letters and seperate then by space!")
            continue
        else:
            directions = dict(zip(letters,DIRECTION_LIST))
            break
    return directions

def win():
    if g_puzzle.index(SPACE) == g_size-1:
        if g_puzzle == g_solved:
            return True
    return False

def introduction():
    print("Welcome to puzzle game!")
    print("In this game, there is a square-framed board consisting of 8 or 15 square tiles,")
    print("which are numbered 1 to 8\\15, initially placed in random order.")
    print("The board has an empty space where an adjacent tile can be slid to.")
    print("The objective of the game is to re-arrange the tiles into a sequential order by their numbers.")
    print("Start the game now!")

def main():
    introduction()
    directions = determine_letters_for_directions()

    # Game loop
    while True:

        while True:
            size = input('Enter "1" for 8-puzzle, "2" for 15-puzzle, or "q" to end the game: ')
            if size == "1" or size == "2" or size == "q":
                break
            else:
                print("Wrong input!")

        if size == "q":
            break

        size = int(size)
        if size == 1:
            size = 9
        else:
            size = 16
        create_puzzle(size)
        randomize_puzzle()

        step = 0
        while True:
            print_puzzle()
            valid_move_letters = []

            while True:
                print("Enter your move (", end="")
                for letter, move in directions.items():
                    if is_valid(move):
                        print("%s-%s"%(letter, move), end=" ")
                        valid_move_letters.append(letter)
                print(")", end="")
                letter = input()
                if letter in valid_move_letters:
                    break
                else:
                    print("The direction is not valid.")

            move = directions[letter]
            slid(move)
            step += 1
            if win():
                break

        print_puzzle()
        print("Congratulations! You solved the puzzle in %d moves!"%step)

if __name__ == '__main__':
    main()