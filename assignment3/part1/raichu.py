#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy
from copy import deepcopy

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))

def raichu_backward(b,i,j,valid_coins):
    successors = []
    number = -1
    for row in range(i-1,-1,-1):
        if b[row][j] =='.':
            c = deepcopy(b)
            c[row][j] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][j] in valid_coins:
            number = row
            break
        else:
            break
    for row in range(number-1,-1,-1):
        if b[row][j] =='.':
            c = deepcopy(b)
            c[row][j] , c[i][j],c[number][j] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors
            
def raichu_forward(b,i,j,valid_coins):
    successors = []
    number = len(b)
    for row in range(i+1,len(b)):
        if b[row][j] =='.':
            c = deepcopy(b)
            c[row][j] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][j] in valid_coins:
            number = row
            break
        else:
            break
    for row in range(number+1,len(b)):
        if b[row][j] =='.':
            c = deepcopy(b)
            c[row][j] , c[i][j],c[number][j] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors

def raichu_right(b,i,j,valid_coins):
    successors = []
    number = len(b[i])
    for col in range(j+1,len(b[i])):
        if b[i][col] =='.':
            c = deepcopy(b)
            c[i][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[i][col] in valid_coins:
            number = col
            break
        else:
            break
    for col in range(number+1,len(b[i])):
        if b[i][col] =='.':
            c = deepcopy(b)
            c[i][col] , c[i][j],c[i][number] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors

def raichu_left(b,i,j,valid_coins):
    successors = []
    number = -1
    for col in range(j-1,-1,-1):
        if b[i][col] =='.':
            c = deepcopy(b)
            c[i][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[i][col] in valid_coins:
            number = col
            break
        else:
            break
    for col in range(number-1,-1,-1):
        if b[i][col] =='.':
            c = deepcopy(b)
            c[i][col] , c[i][j],c[i][number] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors
            
def raichu_right_upper_diagonal(b,i,j,valid_coins):
    successors = []
    number1 = -1
    number2 = len(b[i])
    for row,col in zip(range(i-1,-1,-1),range(j+1,len(b[i]))):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][col] in valid_coins:
            number1 = row
            number2 = col
            break
        else:
            break
    for row,col in zip(range(number1-1,-1,-1),range(number2+1,len(b[i]))):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j],c[number1][number2] = c[i][j] , '.', '.'
            successors.append(c)
        else:
            break
    return successors
            
def raichu_left_upper_diagonal(b,i,j,valid_coins):
    successors = []
    number1 = -1
    number2 = -1
    for row,col in zip(range(i-1,-1,-1),range(j-1,-1,-1)):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][col] in valid_coins:
            number1 = row
            number2 = col
            break
        else:
            break
    for row,col in zip(range(number1-1,-1,-1),range(number2-1,-1,-1)):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j],c[number1][number2] = c[i][j] , '.', '.'
            successors.append(c)
        else:
            break
    return successors
            
def raichu_right_lower_diagonal(b,i,j,valid_coins):
    successors = []
    number1 = len(b)
    number2 = len(b[i])
    for row,col in zip(range(i+1,len(b)),range(j+1,len(b[i]))):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][col] in valid_coins:
            number1 = row
            number2 = col
            break
        else:
            break
    for row,col in zip(range(number1+1,len(b)),range(number2+1,len(b[i]))):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j],c[number1][number2] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors
            
def raichu_left_lower_diagonal(b,i,j,valid_coins):
    successors = []
    number1 = len(b)
    number2 = -1
    for row,col in zip(range(i+1,len(b)),range(j-1,-1,-1)):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j] = c[i][j] , '.'
            successors.append(c)
        elif b[row][col] in valid_coins:
            number1 = row
            number2 = col
            break
        else:
            break
    for row,col in zip(range(number1+1,len(b)),range(number2-1,-1,-1)):
        if b[row][col] =='.':
            c = deepcopy(b)
            c[row][col] , c[i][j],c[number1][number2] = c[i][j] , '.','.'
            successors.append(c)
        else:
            break
    return successors

def successors_white(board):
    b =   deepcopy(board)
    size =len(board)
    successors = []
    for i in range(0,size):
        for j in range(0,size):
            if b[i][j] == '.':
                continue
            #White Raichu's
            elif b[i][j] == '@':
                valid_coins = ('b','B','$')
                result = raichu_forward(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_backward(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right_upper_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left_upper_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right_lower_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left_lower_diagonal(b,i,j,valid_coins)
                successors.extend(result)
            #white Pichu's
            elif b[i][j]=='w':
                if j-1>=0 and b[i+1][j-1]=='.':
                    if i+1 == size-1:
                        coin = '@'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i+1][j-1] , c[i][j] = coin , '.'
                    successors.append(c)
                elif j-2>=0 and i+2<size and b[i+1][j-1] == 'b' and b[i+2][j-2] == '.':
                    if i+2 == size-1:
                        coin = '@'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i+2][j-2] ,c[i][j] , c[i+1][j-1] = coin , '.', '.'  #Jumping over black Pichu left side
                    successors.append(c)
                if j+1<size and b[i+1][j+1]=='.':
                    if i+1 == size-1:
                        coin = '@'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i+1][j+1],c[i][j] = coin,'.'
                    successors.append(c)
                elif j+2<size and i+2<size and b[i+1][j+1] == 'b' and b[i+2][j+2] == '.':
                    if i+2 == size-1:
                        coin = '@'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i+2][j+2] , c[i][j], c[i+1][j+1] = coin,'.','.'    #Jumping over black pichu right side
                    successors.append(c)
            #White Pikachu's
            elif b[i][j] == 'W':
                if i+1<size and b[i+1][j] == '.':
                    if i+1 == size-1:
                        c =   deepcopy(b)
                        c[i+1][j], c[i][j] = '@','.'    
                        successors.append(c)
                    else:
                        c =   deepcopy(b)
                        c[i+1][j],c[i][j] = c[i][j],'.'     #One step Forward
                        successors.append(c)
                elif i+2<size and (b[i+1][j] in ('B','b')) and b[i+2][j] == '.':
                    if i+2 == size-1:
                        c =  deepcopy(b)
                        c[i+2][j], c[i][j] = '@','.'
                        c[i+1][j] = '.'
                        successors.append(c)
                    else:
                        c =  deepcopy(b)
                        c[i+2][j] , c[i][j] = c[i][j] , '.'
                        c[i+1][j] = '.'     #Jumping over black pichu or black pikachu in one step forward.
                        successors.append(c)
                if j-1>=0 and b[i][j-1]=='.':
                    c =   deepcopy(b)
                    c[i][j-1],c[i][j] = c[i][j],'.'
                    successors.append(c)
                elif j-2>=0 and j-1>=0 and (b[i][j-1] in ('B','b')) and b[i][j-2] == '.':
                    c =   deepcopy(b)
                    c[i][j-2] , c[i][j] = c[i][j],'.'
                    c[i][j-1] = '.'     #Jumping over black pichu or black pikachu in one step left side.
                    successors.append(c)
                if j+1<size and b[i][j+1] == '.':
                    c =   deepcopy(b)
                    c[i][j+1],c[i][j] = c[i][j],'.'
                    successors.append(c)
                elif j+2<size and j+1<size and (b[i][j+1] in ('B','b')) and b[i][j+2] == '.':
                    c =   deepcopy(b)
                    c[i][j+2] , c[i][j] = c[i][j],'.'
                    c[i][j+1] = '.'     #Jumping over black pichu or black pikachu in one step right side.
                    successors.append(b)
                #Two steps 
                if i+2<size and b[i+2][j] == '.':
                    if i+2 == size-1:
                        c =   deepcopy(b)
                        if b[i+1][j] in ('b','B','.'):
                            c[i+2][j], c[i][j] = '@','.'
                            if b[i+1][j] in ('b','B'):
                                c[i+1][j] = '.'
                            successors.append(c)
                    else:
                        c =   deepcopy(b)
                        if b[i+1][j] in ('b','B','.'):
                            c[i+2][j],c[i][j] = c[i][j],'.'
                            if b[i+1][j] in ('b','B'):
                                c[i+1][j] = '.'
                            successors.append(c)
                if i+3<size and (b[i+2][j] in ('b','B')) and b[i+3][j] == '.':
                    if i+3 == size-1:
                        c =   deepcopy(b)
                        if b[i+1][j]  == '.':
                            c[i+3][j], c[i][j] = '@','.'
                            c[i+2][j] = '.'
                            successors.append(c)
                    else:
                        c =   deepcopy(b)
                        if b[i+1][j]  == '.':
                            c[i+3][j] , c[i][j] = c[i][j] , '.'
                            c[i+2][j] = '.'     #Jumping over black pichu or black pikachu in two step forward.
                            successors.append(c)
                if j-2>=0 and b[i][j-2]=='.':
                    c =   deepcopy(b)
                    if b[i][j-1] in ('b','B','.'):
                        c[i][j-2],c[i][j] = c[i][j],'.'
                        if b[i][j-1] in ('b','B'):
                                c[i][j-1] = '.'
                        successors.append(c)
                if j-2>=0 and j-3>=0 and (b[i][j-2] in ('B','b')) and b[i][j-3] == '.' and b[i][j-1] == '.':
                    c =   deepcopy(b)
                    c[i][j-3] , c[i][j] = c[i][j],'.'
                    c[i][j-2] = '.'     #Jumping over black pichu or black pikachu in two step left side.
                    successors.append(c)
                if j+2<size and b[i][j+2] == '.' and b[i][j+1] in ('b','B','.'):
                    c =   deepcopy(b)
                    c[i][j+2],c[i][j] = c[i][j],'.'
                    if b[i][j+1] in ('b','B'):
                            c[i][j+1] = '.'
                    successors.append(c)
                if j+2<size and j+3<size and (b[i][j+2] in ('B','b')) and b[i][j+3] == '.' and b[i][j+1] == '.':
                    c =   deepcopy(b)
                    c[i][j+3] , c[i][j] = c[i][j],'.'
                    c[i][j+2] = '.'     #Jumping over black pichu or black pikachu in two step right side.
                    successors.append(b)
    return successors

def successors_black(board):
    #x =   deepcopy(board)
    b =   deepcopy(board)
    #b = list()
    #for i in range(0,len(x),N):
    #    b.append(list(x[i:i+N]))
    
    size =len(b)
    successors = []
    for i in range(0,size):
        for j in range(0,size):
            if b[i][j] == '.':
                continue
            #White Raichu's
            elif b[i][j] == '$':
                valid_coins = ('w','W','@')
                result = raichu_forward(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_backward(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right_upper_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left_upper_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_right_lower_diagonal(b,i,j,valid_coins)
                successors.extend(result)
                result = raichu_left_lower_diagonal(b,i,j,valid_coins)
                successors.extend(result)
            #Black Pichu's
            elif b[i][j]=='b':
                if i-1>=0 and j+1<size and b[i-1][j+1]=='.':        #one step right diagonal
                    if i-1 == 0:
                        coin = '$'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i-1][j+1],c[i][j] = coin,'.'
                    successors.append(c)
                elif i-2>=0 and j+2<size and b[i-1][j+1] == 'w' and b[i-2][j+2] == '.':
                    if i-2 == 0:
                        coin = '$'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i-2][j+2] ,c[i][j] , c[i-1][j+1] = coin, '.', '.'  #Jumping over white Pichu right diagonal
                    successors.append(c)
                if i-1>=0 and j-1>=0 and b[i-1][j-1]=='.':          #one step left diagonal
                    if i-1 == 0:
                        coin = '$'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i-1][j-1],c[i][j] = coin,'.'
                    successors.append(c)
                elif i-2>=0 and j-2>=0 and b[i-1][j-1] == 'w' and b[i-2][j-2] == '.':
                    if i-2 == 0:
                        coin = '$'
                    else:
                        coin = b[i][j]
                    c = deepcopy(b)
                    c[i-2][j-2] , c[i][j] , c[i-1][j-1] = coin,'.','.'  #Jumping over white pichu left diagonal
                    successors.append(c)
            #Black Pikachu's
            elif b[i][j] == 'B':
                if i-1>=0 and b[i-1][j] == '.':     #One step forward
                    if i-1 == 0:
                        c = deepcopy(b)
                        c[i-1][j],c[i][j] = '$','.'
                        successors.append(c)
                    else:
                        c = deepcopy(b)
                        c[i-1][j],c[i][j] = c[i][j],'.'
                        successors.append(c)
                elif i-2>=0 and (b[i-1][j] in ('w','W')) and b[i-2][j] == '.':
                    if i-2 == 0:
                        c = deepcopy(b)
                        c[i-2][j] , c[i][j] = '$' , '.'
                        c[i-1][j] = '.'     
                        successors.append(c)
                    else:
                        c = deepcopy(b)
                        c[i-2][j] , c[i][j] = c[i][j] , '.'
                        c[i-1][j] = '.'     #Jumping over white pichu or white pikachu in one step forward.
                        successors.append(c)
                if j-1>=0 and b[i][j-1]=='.':       #One step left
                    c = deepcopy(b)
                    c[i][j-1],c[i][j] = c[i][j],'.'
                    successors.append(c)
                elif j-2>=0 and (b[i][j-1] in ('w','W')) and b[i][j-2] == '.':
                    c = deepcopy(b)
                    c[i][j-2] , c[i][j] = c[i][j],'.'
                    c[i][j-1] = '.'     #Jumping over white pichu or white pikachu in one step left side.
                    successors.append(c)
                if j+1<size and b[i][j+1] == '.':       #One Step right
                    c = deepcopy(b)
                    c[i][j+1],c[i][j] = c[i][j],'.'
                    successors.append(c)
                elif j+2<size and (b[i][j+1] in ('w','W')) and b[i][j+2] == '.':
                    c = deepcopy(b)
                    c[i][j+2] , c[i][j] = c[i][j],'.'
                    c[i][j+1] = '.'     #Jumping over white pichu or white pikachu in one step right side.
                    successors.append(b)

                if i-2>=0 and b[i-2][j] == '.' and b[i-1][j] in ('w','W','.'):     #Two step forward
                    if i-2 == 0:
                        c = deepcopy(b)
                        c[i-2][j],c[i][j] = '$','.'
                        if b[i-1][j] in ('w','W'):
                            c[i-1][j] = '.'
                        successors.append(c)
                    else:
                        c = deepcopy(b)
                        c[i-2][j],c[i][j] = c[i][j],'.'
                        if b[i-1][j] in ('w','W'):
                            c[i-1][j] = '.'
                        successors.append(c)
                if i-3>=0 and (b[i-2][j] in ('w','W') ) and b[i-3][j] == '.' and b[i-1][j] == '.':
                    if i-3 == 0:
                        c = deepcopy(b)
                        c[i-3][j] , c[i][j] = '$' , '.'
                        c[i-2][j] = '.'     
                        if b[i-1][j] in ('w','W'):
                            c[i-1][j] = '.'
                        successors.append(c)
                    else:
                        c = deepcopy(b)
                        c[i-3][j] , c[i][j] = c[i][j] , '.'
                        c[i-2][j] = '.'     #Jumping over white pichu or white pikachu in two step forward.
                        if b[i-1][j] in ('w','W'):
                            c[i-1][j] = '.'
                        successors.append(c)
                if j-2>=0 and b[i][j-2]=='.' and b[i][j-2] in ('w','W','.'):       #Two step Left
                    c = deepcopy(b)
                    c[i][j-2],c[i][j] = c[i][j],'.'
                    if b[i][j-1] in ('w','W'):
                            c[i][j-1] = '.'
                    successors.append(c)
                if j-3>=0 and (b[i][j-2] in ('w','W')) and b[i][j-3] == '.' and b[i][j-1] == '.':
                    c = deepcopy(b)
                    c[i][j-3] , c[i][j] = c[i][j],'.'
                    c[i][j-2] = '.'     #Jumping over white pichu or white pikachu in two step left side.
                    if b[i][j-1] in ('w','W'):
                            c[i][j-1] = '.'
                    successors.append(c)
                if j+2<size and b[i][j+2] == '.' and b[i][j+2] in ('w','W','.'):       #Two step right
                    c = deepcopy(b)
                    c[i][j+2],c[i][j] = c[i][j],'.'
                    successors.append(c)
                if j+3<size and (b[i][j+2] in ('w','W')) and b[i][j+3] == '.' and b[i][j+1] == '.':
                    c = deepcopy(b)
                    c[i][j+3] , c[i][j] = c[i][j],'.'
                    c[i][j+2] = '.'     #Jumping over white pichu or white pikachu in two step right side.
                    if b[i][j+1] in ('w','W'):
                            c[i][j+1] = '.'
                    successors.append(b)
    return successors

def evaluate(board,player):
    white_left =0
    black_left = 0
    weighted_white = 0
    weighted_black = 0
    for row in board:
        for ele in range(len(row)):
            if row[ele] == 'w':
                weighted_white += 1
                white_left+=1
            elif row[ele] == 'W':
                weighted_white += 10
                white_left +=1
            elif row[ele] == '@':
                weighted_white += 50
                white_left+=1
            elif row[ele] == 'b':
                weighted_black += 1
                black_left +=1
            elif row[ele] == 'B':
                weighted_black += 10
                black_left += 1
            elif row[ele] == '$':
                weighted_black += 50
                black_left += 1
    if player == 'w':
        return (white_left - black_left) + (weighted_white - weighted_black)
    elif player == 'b':
        return (black_left - white_left) + (weighted_black - weighted_white)
            
                    
def minimax_white(board,depth,maxplayer,alpha,beta):
    if depth == 0:
        #print('depth is {}'.format(depth))
        return evaluate(board,'w') , board
    if maxplayer:
        #print('depth is {}'.format(depth))
        maxEval = float('-inf')
        best_move = None
        for child in successors_white(board):
            eval = minimax_white(child,depth-1,False,alpha,beta)[0]
            maxEval = max(maxEval,eval)
            if maxEval >= beta:
                break
            alpha = max(alpha,eval)
            if maxEval == eval:
                best_move = child
        return maxEval,best_move
    else:
        #print('depth is {}'.format(depth))
        minEval = float('inf')
        best_move = None
        for child in successors_black(board):
            eval = minimax_white(child,depth-1,True,alpha,beta)[0]
            minEval = min(minEval,eval)
            if minEval <= alpha:
                break
            beta = min(beta,eval)
            if minEval == eval:
                best_move = child
        return minEval,best_move
    
def minimax_black(board,depth,maxplayer,alpha,beta):
    if depth == 0:
        #print('depth is {}'.format(depth))
        return evaluate(board,'b') , board
    if maxplayer:
        #print('depth is {}'.format(depth))
        maxEval = float('-inf')
        best_move = None
        for child in successors_black(board):
            eval = minimax_black(child,depth-1,False,alpha,beta)[0]
            maxEval = max(maxEval,eval)
            if maxEval >= beta:
                break
            alpha = max(alpha,eval)
            if maxEval == eval:
                best_move = child
        return maxEval,best_move
    else:
        #print('depth is {}'.format(depth))
        minEval = float('inf')
        best_move = None
        for child in successors_white(board):
            eval = minimax_black(child,depth-1,True,alpha,beta)[0]
            minEval = min(minEval,eval)
            if minEval <= alpha:
                break
            beta = min(beta,eval)
            if minEval == eval:
                best_move = child
        return minEval,best_move

def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    alpha = float('-inf')
    beta = float('inf')
    x =   deepcopy(board)
    board_to_list = list()
    for i in range(0,len(x),N):
        board_to_list.append(list(x[i:i+N]))
    
    #print(time.time()-start_time)
    
    #for move in successors_black(board):
    #    for ele in move:
    #        print(ele)
    #    print('\n')
    depth = 1
    while True:
        if player == 'w':
            new_board = minimax_white(board_to_list,depth,True,alpha,beta)[1]
        else:
            new_board = minimax_black(board_to_list,depth,True,alpha,beta)[1]
        
        if new_board is not None:
            best_move_board =''
            for b in new_board:
                for i in range(len(b)):
                    best_move_board += str(b[i])
            print(best_move_board)
            #time.sleep(1)
            yield best_move_board
        depth += 1
    #return [best_move_board]


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
        
