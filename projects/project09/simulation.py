# Author: FILL IN
# Class: COMP 141
# Program 9: Predator-Prey Simulation
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: FILL IN
from cs1.graphics import *
import random

# GLOBALS:
ROWS = 4 # num rows
COLS = 4 # num cols
ITERATIONS = 3 # num generations
INITIAL_PREY = 5 # num prey
INITIAL_PREDATORS = 1 # num predators
CELL_LENGTH_PIXELS = 16 # side length of a cell when you draw it


def random_state(height, width, prey, predators):
    # make an empty world state, and then populate it with prey and predators
    new_state = []
    for h in range(height):
        new_state.append([0]*width)
    for p in range(prey):
        r, c = get_empty_cell(new_state)
        new_state[r][c] = 1
    for p in range(predators):
        r, c = get_empty_cell(new_state)
        new_state[r][c] = 2
    return new_state


# find a random empty cell (cell_value=0) in the state
def get_empty_cell(state):
    # use random.randint to pick a random row/col until you find an empty one
    height = len(state)
    width = len(state[0])
    r = random.randint(0, height-1)
    c = random.randint(0, width-1)
    while state[r][c] != 0:
        r = random.randint(0, height-1)
        c = random.randint(0, width-1)
    return r, c


# print the state as text
def print_state(state):
    for r in state:
        print(r)
    print()
    
    
# use the DOUBLE BUFFER pattern to create the next state:
# - create an empty state called new_state
# - for each cell in state, call next_cell_value to determine
#   what value should be in new_state for that cell
# - return new_state
def next_state(state):
    new_state = []
    # make an empty 2D list for the next state

    # use the next_value function (already written)
    # to populate the new state
    
    return new_state


# given state, a row r, and a col c, determine what the cell value
# at (r, c) will be in the next iteration
def next_value(state, r, c):
    if state[r][c] == 0 and prey_in_neighborhood(state, r, c) > 0:
        return 1
    if state[r][c] == 1 and predators_in_neighborhood(state, r, c) > 0:
        return 2
    if state[r][c] == 2:
        return random.choice([0, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    if state[r][c] == 1:
        return random.choice([0, 1])
    if state[r][c] == 0:
        return 0


# given state, row r, and col c, determine how many
# prey are in the neighborhood of (r, c)
def prey_in_neighborhood(state, r, c):
    # use neighbors and count the number of prey (ie, 1s)
    neighbors = neighborhood(state, r, c)
    num_prey = 0
    for n in neighbors:
        if n == 1:
            num_prey += 1
    return num_prey


# as above, except for predators
def predators_in_neighborhood(state, r, c):
    # use neighbors and count the number of preadtors (ie, 2s)
    neighbors = neighborhood(state, r, c)
    num_pred = 0
    for n in neighbors:
        if n == 2:
            num_pred += 1
    return num_pred


# given state, r, c, return the values of the neighbors of (r, c)
# as a list, eg [1, 2, 0, 1, 1, 0, 0, 2]
def neighborhood(state, r, c):
    neighbors = []
    min_r = max(0, r - 1)
    max_r = min(len(state), r + 2)
    min_c = max(0, c - 1)
    max_c = min(len(state[r]), c + 2)
    for x in range(min_c, max_c):
        for y in range(min_r, max_r):
            if not (x == c and y == r):
                neighbors.append(state[y][x])
    return neighbors


# write a function which takes a state, clears the previous canvas,
# and draws each cell
def draw_state(state):
    colors = {} # Keys = 0, 1, 2; values = colors for the keys


# write a function which takes an (x, y) coordinate in PIXEL SPACE
# and draws a creature as a square with a specific color (eg, "red")
def draw_cell(x, y, color):
    pass


# main needs to open a canvas, create an initial state,
# and loop over the iterations, producing and drawing the
# next state in each iteration
def main():
    # open canvas, produce random starting state, iteratively produce next states, draw the new states
    state = random_state(ROWS, COLS, INITIAL_PREY, INITIAL_PREDATORS)
    print_state(state)
    for i in range(ITERATIONS):
        state = next_state(state)
        print_state(state)
        input() # comment/uncomment if you want more control over the simulation "time"

#main() #uncomment this when you're ready to test your full program
