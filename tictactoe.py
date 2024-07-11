"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in board:
        for element in row:
            if element == 'X':
                xCount += 1
            if element == 'O':
                oCount += 1
    if (xCount+oCount)%2 == 0:
        return 'X'
    else:
        return 'O'
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                actions.add((i, j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("The cell is not empty")
    
    #making a deep copy of board
    board_after_action = [row.copy() for row in board] 
    board_after_action[action[0]][action[1]] = player(board)
    return board_after_action


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winX = set()
    winO = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == 'X':
                winX.add((i, j))
            elif element == 'O':
                winO.add((i, j))

    winning_combinations = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)}
    ]

    for combination in winning_combinations:
        if combination <= winX:
            return 'X'
        if combination <= winO:
            return 'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCount = 0
    for row in board:
        for element in row:
            if element == EMPTY:
                emptyCount += 1
    if emptyCount == 0 or winner(board) == 'X' or winner(board) == 'O':
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]