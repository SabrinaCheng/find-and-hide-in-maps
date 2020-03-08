#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Pei-Yi Cheng, peicheng]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json
import queue

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves={'S':(row+1,col), 'N':(row-1,col), 'W':(row,col-1), 'E':(row,col+1)}
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves.items() if valid_index(move[1], len(map), len(map[0])) and (map[move[1][0]][move[1][1]] in ".@" ) ]

# get origin-destination pair
def find_od_pair(board):
    for row_i in range(len(board)):
        for col_i in range(len(board[0])):
            if board[row_i][col_i] == '#':
                o = (row_i, col_i)
            if board[row_i][col_i] == '@':
                d = (row_i, col_i)
    return o, d

# calculate squared euclidean distance
def sq_euclidean_dist(pt1, pt2):
    return ((pt1[0] - pt2[0]) ** 2) + ((pt1[1] - pt2[1]) ** 2)

# Perform search on the map
def search1(board):
    # Find my start position
    N, M = len(board), len(board[0])
    you_loc, lud_loc = find_od_pair(board)

    fringe = queue.PriorityQueue()
    # val, path, curr_loc, path length
    fringe.put((sq_euclidean_dist(you_loc, lud_loc), '', you_loc, 0))
    
    coordinate = [(n, m) for n in range(N) for m in range(M)]
    visited = dict(zip(coordinate, [False] * N * M))
    visited[you_loc] = True
    
    shortest_dist = dict(zip(coordinate, [float('inf')] * N * M))
    shortest_dist[you_loc] = 0
    
    while fringe.qsize() > 0:
        (val, path, curr_move, curr_dist) = fringe.get()
        for direction, pos in moves(board, *curr_move):
            if visited[pos] == False:
                if board[pos[0]][pos[1]] == "@":
                    return str(curr_dist + 1) + ' ' + str(path + direction)
                else:
                    alt = shortest_dist[curr_move] + 1
                    if alt < shortest_dist[pos]:
                        shortest_dist[pos] = alt
                    new_val = sq_euclidean_dist(pos, lud_loc) + shortest_dist[pos]
                    new_path = path + direction
                    fringe.put((new_val, new_path, pos, curr_dist + 1))
                visited[pos] = True
    return 'Inf'

# Main Function
if __name__ == "__main__":
	IUB_map=parse_map(sys.argv[1])
	print("Shhhh... quiet while I navigate!")
	solution = search1(IUB_map)
	print("Here's the solution I found:")
	print(solution)

