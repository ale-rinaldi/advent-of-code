import sys
import copy

with open('d4-input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

winning_board = None
winning_extracted = None

def parse_input(lines):
    numbers = [int(x) for x in lines.pop(0).split(',')]
    lines.pop(0)
    boards = []
    board = []
    for line in lines:
        if line == "":
            if len(board) != 5:
                raise ValueError(f"invalid board: {board}")
            boards.append({"nums": board, "won": False})
            board = []
            continue
        row_numbers = [{"number": int(n), "extracted": False} for n in line.split(' ') if n]
        if len(row_numbers) != 5:
            raise ValueError(f"invalid line: {line}")
        board.append(row_numbers)
    if len(board) > 0:
        if len(board) != 5:
            raise ValueError(f"invalid board: {board}")
        boards.append({"nums": board, "won": False})
        board = []
    return boards, numbers

def calculate_score(board, extracted):
    sum = 0
    for row in board:
        for item in row:
            if not item["extracted"]:
                sum += item["number"]
    return sum * extracted

def check_win(board):
    for x in range(5):
        won = True
        for y in range(5):
            if not board[x][y]["extracted"]:
                won = False
                break
        if won:
            return True
    for y in range(5):
        won = True
        for x in range(5):
            if not board[x][y]["extracted"]:
                won = False
                break
        if won:
            return True
    return False
    

boards, numbers = parse_input(lines)

for number in numbers:
    for board in boards:
        if board["won"]:
            continue
        for row in board["nums"]:
            for board_item in row:
                if board_item["number"] == number:
                    board_item["extracted"] = True
        if check_win(board["nums"]):
            board["won"] = True
            winning_board = board["nums"]
            winning_extracted = number

print(calculate_score(winning_board, winning_extracted))
