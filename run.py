#!/usr/bin/env python3
import random
import copy

def get_seed_spaces():
    yellow = {"required": "yellow", "contents": "yellow", "links": ["purple", "green"]}
    green = {"required": "green", "contents": "purple", "links": ["yellow", "empty", "blue"]}
    blue = {"required": "blue", "contents": "red", "links": ["green", "red"]}
    purple = {"required": "purple", "contents": "empty", "links": ["empty", "yellow"]}
    empty = {"required": "empty", "contents": "green", "links": ["purple", "green", "red"]}
    red = {"required": "red", "contents": "blue", "links": ["empty", "blue"]}
    spaces_idx = {
        "yellow": yellow,
        "green": green,
        "blue": blue,
        "purple": purple,
        "empty": empty,
        "red": red
    }
    return spaces_idx

def get_spaces(spaces_idx):
    spaces = []
    for key, value in spaces_idx.items():
        spaces.append(value)
    return spaces

def find_empty(spaces):
    for space in spaces:
        if (space["contents"] == "empty"):
            return space
    return None

def swap(space1, space2):
    space1Contents = space1["contents"]
    space1["contents"] = space2["contents"]
    space2["contents"] = space1Contents

def solved(spaces):
    for space in spaces:
        if (space["required"] != space["contents"]):
            return False
    return True

max_solutions = 1000
solutions = []
while True:
    spaces_idx = get_seed_spaces()
    spaces = get_spaces(spaces_idx)
    last_swapped_with = None
    i = 0
    moves = []
    while True:
        empty_space = find_empty(spaces)
        links = empty_space["links"]
        link = random.choice(links)
        space = spaces_idx[link]
        if (space["contents"] == last_swapped_with):
            continue
        last_swapped_with = space["contents"]
        move = "Swapping " + str(empty_space["contents"]) + " with " + str(space["contents"])
        #print(move)
        moves.append(move)
        swap(empty_space, space)
        i += 1
        if (solved(spaces)):
            #print("Solved in " + str(i) + " moves :D")
            break
    solutions.append(moves)
    if (len(solutions) >= max_solutions):
        break

solution = min(solutions, key=len)
print("Smallest solution has " + str(len(solution)) + " moves:")
for move in solution:
    print(move)
