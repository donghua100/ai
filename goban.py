from enum import Enum


N = 15

class ChessboardState(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

class GoBang(object):
    def __init__(self):
        self.__chessMap = [[ChessboardState.EMPTY for j in range(N)] for i in range(N)]
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = ChessboardState.EMPTY

    def get_chessMap(self):
        return self.__chessMap

    def get_chessboard_state(self, i, j):
        return self.__chessMap[i][j]

    def set_chessboard_state(self, i, j, state):
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state

    def get_chess_result(self):
        if self.have_five(self.__currentI, self.__currentJ, self.__currentState):
            return self.__currentState
        else:
            return ChessboardState.EMPT
            return True


    def have_five(self, current_i, current_j):
        #四个方向计数 横 竖 左斜 右斜
        hcount = 1
        vcount = 1
        lbhcount = 1
        rbhcount = 1

        temp = ChessboardState.EMPTY

        #H-左
        for j in range(current_j - 1, -1, -1):  #横向往左 from (current_j - 1) to 0
            temp = self.__chessMap[current_i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            hcount = hcount + 1
        #H-右
        for j in range(current_j + 1, N):  #横向往右 from (current_j + 1) to N
            temp = self.__chessMap[current_i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            hcount = hcount + 1
        #H-结果
        if hcount >= 5:
            return True
        #V-上
        for i in range(current_i - 1, -1, -1):  # from (current_i - 1) to 0
            temp = self.__chessMap[i][current_j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            vcount = vcount + 1
        #V-下
        for i in range(current_i + 1, N):  # from (current_i + 1) to N
            temp = self.__chessMap[i][current_j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            vcount = vcount + 1
        #V-结果
        if vcount >= 5:
            return True
        #LB-上
        for i, j in zip(range(current_i - 1, -1, -1), range(current_j - 1, -1, -1)):  
            temp = self.__chessMap[i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            lbhcount = lbhcount + 1
        #LB-下
        for i, j in zip(range(current_i + 1, N), range(current_j + 1, N)):  
            temp = self.__chessMap[i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            lbhcount = lbhcount + 1
        #LB-结果
        if lbhcount >= 5:
            return True
        #RB-上
        for i, j in zip(range(current_i - 1, -1, -1), range(current_j + 1, N)):  
            temp = self.__chessMap[i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            rbhcount = rbhcount + 1
        #RB-下
        for i, j in zip(range(current_i + 1, N), range(current_j - 1, -1, -1)):  
            temp = self.__chessMap[i][j]
            if temp == ChessboardState.EMPTY or temp != self.__currentState:
                break
            rbhcount = rbhcount + 1
        #LB-结果
        if rbhcount >= 5:
            return True