import json


def check_draw(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def get_pozition(turn):

    if turn == [0, 0]:
        return 0
    if turn == [1, 0]:
        return 1
    if turn == [2, 0]:
        return 2
    if turn == [0, 1]:
        return 3
    if turn == [1, 1]:
        return 4
    if turn == [2, 1]:
        return 5
    if turn == [0, 2]:
        return 6
    if turn == [1, 2]:
        return 7
    if turn == [2, 2]:
        return 8
    raise ValueError('Undefined unit: {}'.format(unit))


with open('data/oxotestdata.json') as json_data:
    data = json.load(json_data)
json_data.closed

tmp = 0
for one_game in data:
    board = list(range(1, 10))
    for one_turn in one_game:
        board[get_pozition(one_turn[:2])] = one_turn[2]
    if not check_draw(board):
        tmp += 1
print(tmp)
