#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [HARISHANKER BRAHMA KANDE AND HKANDE]
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0][0] < n  and 0 <= pos[0][1] < m

# Find the possible moves from position (row, col)
def moves(map, fringe_visited, path, row, col):
        #Appending the directions in the tuple for the directions.
        moves=(((row+1,col),path+'D'), ((row-1,col),path+'U'), ((row,col-1),path+'L'), ((row,col+1),path+'R'))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".") and which are not visited.
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0][0]][move[0][1]] in ".@" ) and move[0] not in fringe_visited ]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe, fringe_visited = [(pichu_loc,0,'')],[pichu_loc]
        while fringe:
                (curr_move, curr_dist, curr_path)=fringe.pop()
                for move in moves(house_map, fringe_visited, curr_path, *curr_move):
                        if house_map[move[0][0]][move[0][1]]=="@":
                                return (curr_dist+1, curr_path+move[1][curr_dist])  # returning the distance and directions of the path. 
                        else:
                                fringe.append((move[0], curr_dist + 1,move[1]))
                                fringe_visited.append(move[0])      #Storing the visited nodes into the fringe.
        return -1        #Returning -1 when there is no path found.

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])

