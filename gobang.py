from collections import defaultdict
n = 50
board = [[0]*n for i in range(n)]

O = []
X = []

vis = [[False]*n for i in range(n)]


def value_state(board):
    score = 0
    for i,j in O:
        pass






def nxt_states(board,MAX_TRUE):
    states = []
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                states.append([i,j])
    return states
         



def minmax(board,d,alpha,beta,MAX_TRUN):
    if d == 0:return value_state(board)
    if MAX_TRUN:
        v = float('-inf')
        states = nxt_states()
        for state in states:
            i,j = state
            board[i][j] = 'X'
            vis[i][j] = True
            X.append((i,j))
            tmp_v = minmax(board,d-1,v,beta)
            board[i][j] = 0
            vis[i][j] = False
            X.pop()
            if tmp_v > v: v = tmp_v
            if tmp_v > beta:return beta
        return v
    else:
        v = float('inf')
        states = nxt_states()
        for  state in states:
            i,j = state
            board[i][j] = 'O'
            vis[i][j] = True
            O.append((i,j))
            tmp_v = minmax(board,d-1,alpha,v)
            board[i][j] = 0
            vis[i][j] = False
            O.pop()
            if tmp_v < v:v = tmp_v
            if tmp_v > alpha:return alpha
        return v