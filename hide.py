#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : [Pei-Yi Cheng, peicheng]
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys
import copy
import queue

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip().split("\n")]

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# successors of given board state (initial step)
# Get initial state including available locations and number of surrounding available locations
def get_init_state(board, nr, nc):
    # available locations, number of surrounding available locations
    avail_locs = dict(zip([(ri, ci) for ri in range(nr) for ci in range(nc)], [0] * nc * nr))
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '.':
                for s in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= r + s[0] < nr and 0 <= c + s[1] < nc and board[r + s[0]][c + s[1]] == '.': 
                        avail_locs[(r + s[0], c + s[1])] += 1
            elif board[r][c] == '&' or board[r][c] == '@':
                del avail_locs[(r, c)]
            elif board[r][c] == '#':
                del avail_locs[(r, c)]
    return avail_locs

# successors
# find locations that can be seen, current location is included
def can_see(nr, nc, avail_loc, occ):
    res = [occ]
    see = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for s in see:
        tmp = [occ]
        while tmp:
            row_i, col_i = tmp.pop()
            if 0 <= row_i + s[0] < nr and 0 <= col_i + s[1] < nc and (row_i + s[0], col_i + s[1]) in avail_loc:
                tmp += [(row_i + s[0], col_i + s[1])]
                res.append((row_i + s[0], col_i + s[1]))
    return res

# Solve n-rooks!
def solve(board):    
    nr, nc = len(board), len(board[0])
    init_avail_locs = get_init_state(board, nr, nc)
    fringe = queue.PriorityQueue()
    for pos, cnt in init_avail_locs.items():
        fringe.put((cnt + K, pos, init_avail_locs, []))
    
    while fringe.qsize() > 0:
        val, curr_loc, pre_avail_locs, pre_occ_locs = fringe.get()
        new_occ_locs = pre_occ_locs + [curr_loc]
        if len(new_occ_locs) == K:
            new_board = copy.deepcopy(board)
            for r, c in new_occ_locs:
                new_board = add_friend(new_board, r, c)
            return new_board
        invalid_pos = can_see(nr, nc, init_avail_locs, curr_loc)
        new_avail_locs = {k:v for (k, v) in pre_avail_locs.items() if k not in invalid_pos}
        if not new_avail_locs: return None
        
        for p, c in new_avail_locs.items():
            fringe.put((c + (K - len(new_occ_locs)), p, new_avail_locs, new_occ_locs))

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print(IUB_map)
    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")


