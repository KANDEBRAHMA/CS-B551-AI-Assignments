#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: name IU ID
#
# Based on skeleton code by D. Crandall & B551 Staff, September 2021
#

import sys
import copy
import numpy as np
import heapq as hq
import math


ROWS=5
COLS=5
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
#depth=0

def move_right(board, row):
  """Move the given row to one position right"""
  operational_board = copy.deepcopy(board)
  operational_board[row] = operational_board[row][-1:] + operational_board[row][:-1]
  return operational_board

def move_left(board, row):
  """Move the given row to one position left"""
  operational_board = copy.deepcopy(board)
  operational_board[row] = operational_board[row][1:] + operational_board[row][:1]
  return operational_board

def rotate_right_Ic(board,row,residual):
    board[row] = board[row][:2] + [residual] + board[row][2:]
    residual=board[row].pop(-2)
    return residual

def rotate_left_Ic(board,row,residual):
    board[row] = board[row][:3] + [residual] + board[row][3:]
    residual=board[row].pop(1)
    return residual

def move_Ic_clockwise(board):
    operational_board=copy.deepcopy(board)
    operational_board[1]=[operational_board[1][0]]+[operational_board[2][1]]+operational_board[1][1:]
    residual=operational_board[1].pop(4)
    operational_board=transpose_board(operational_board)
    residual=rotate_right_Ic(operational_board,-2,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left_Ic(operational_board,-2,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left_Ic(operational_board,1,residual)
    operational_board=transpose_board(operational_board)
    return operational_board

def move_Ic_cclockwise(board):
    operational_board=copy.deepcopy(board)
    operational_board[1]=operational_board[1][0:-1]+[operational_board[2][-2]]+[operational_board[1][-1]]
    residual=operational_board[1].pop(1)
    operational_board=transpose_board(operational_board)
    residual=rotate_right_Ic(operational_board,1,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_right_Ic(operational_board,-2,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left_Ic(operational_board,-2,residual)
    operational_board=transpose_board(operational_board)
    return operational_board

def rotate_right(board,row,residual):
    board[row] = [board[row][0]] +[residual] + board[row][1:]
    residual=board[row].pop()
    return residual

def rotate_left(board,row,residual):
    board[row] = board[row][:-1] + [residual] + [board[row][-1]]
    residual=board[row].pop(0)
    return residual

def move_Oc_cclockwise(board):
    operational_board=copy.deepcopy(board)
    operational_board[0]=operational_board[0]+[operational_board[1][-1]]
    residual=operational_board[0].pop(0)
    operational_board=transpose_board(operational_board)
    residual=rotate_right(operational_board,0,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_right(operational_board,-1,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left(operational_board,-1,residual)
    operational_board=transpose_board(operational_board)
    return operational_board
def move_Oc_clockwise(board):
    operational_board=copy.deepcopy(board)
    operational_board[0]=[operational_board[1][0]]+operational_board[0]
    residual=operational_board[0].pop()
    operational_board=transpose_board(operational_board)
    residual=rotate_right(operational_board,-1,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left(operational_board,-1,residual)
    operational_board=transpose_board(operational_board)
    residual=rotate_left(operational_board,0,residual)
    operational_board=transpose_board(operational_board)
    return operational_board

def transpose_board(board):
  """Transpose the board --> change row to column"""
  operational_board = copy.deepcopy(board)
  return [list(col) for col in zip(*operational_board)]

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

def heuristic_function(state):
    manhattan_dist=0
    #return mis_placed_count += 1 for i in range(ROWS) for j in range(COLS) if not board[i][j]==goal_state[i][j]         
    #for i in range(ROWS*COLS):
    #        if not state[i] == goal_state[i]:
    #            mis_placed_count += 1   

    goal_location =[(0,0),(0,1),(0,2),(0,3),(0,4),
                    (1,0),(1,1),(1,2),(1,3),(1,4),
                    (2,0),(2,1),(2,2),(2,3),(2,4),
                    (3,0),(3,1),(3,2),(3,3),(3,4),
                    (4,0),(4,1),(4,2),(4,3),(4,4)]
    
    for row in range(ROWS):
        for col in range(COLS):
            i,j = goal_location[state[row][col]-1]
            manhattan_dist += (abs(col-j)+abs(row-i))
            
    return manhattan_dist


# return a list of possible successor states
def successors(state):
    child_nodes,sample_board=[],[]
    for i in range(0,(ROWS*COLS),ROWS):
        sample_board.append(list(state[i:i+ROWS]))
    current_board = copy.deepcopy(sample_board)
    #print(current_board)
    #print(current_board)
    valid_moves_set={'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}
    for direction in valid_moves_set:
        move = copy.deepcopy(direction)
        if set(direction).intersection(set(['R','L','U','D'])):
            direction,index=direction
            index=int(index)-1
        if direction == "R":
            successor_board = move_right(current_board, index)
            #print(successor_board)
        elif direction == "L":
            successor_board = move_left(current_board, index)
        elif direction == "U":
            successor_board = transpose_board(move_left(transpose_board(current_board), index))
        elif direction == "D":
            successor_board = transpose_board(move_right(transpose_board(current_board), index))
        elif direction == 'Oc':
            successor_board = move_Oc_clockwise(current_board)
        elif direction == 'Occ':
            successor_board = move_Oc_cclockwise(current_board)
        elif direction == 'Ic':
            successor_board = move_Ic_clockwise(current_board)
        elif direction == 'Icc':
            successor_board = move_Ic_cclockwise(current_board)
        manhattan_distance = heuristic_function(successor_board)
        succ_board = [ele for row in successor_board for ele in row]
        child_nodes.append([manhattan_distance,succ_board,move])
    return child_nodes

# check if we've reached the goal
def is_goal(state):
    if not state == goal_state:
        return False
    return True

def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    explored_states=[]
    current_initial_board = list(initial_board)
    frontier=[[0,current_initial_board,[]]]
    hq.heapify(frontier)
    while frontier:
        node = hq.heappop(frontier)
        if is_goal(node[1]):
            break
        explored_states.append(node[1])
        for action in successors(node[1]):
            node_in_frontier = False
            child_f_score = len(node[2])+action[0]+1
            for item in frontier:
                    if action[0] == item[1]:
                        node_in_frontier = True
                        break
            if action[1] not in explored_states and not node_in_frontier:
                    hq.heappush(frontier,(child_f_score,action[1],node[2][0:]+[action[2]]))
            for child in frontier:
                if action[1] == child[1] and child_f_score < child[0]:
                    #hq.heappush(frontier,(child_f_score,action[1],node[2][0:]+[action[2]]))
                    child = action
                    break
    return node[2]

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
