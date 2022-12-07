import sys

with open('d4-input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

def parse_input(lines):
    numbers = [int(x) for x in lines.pop(0).split(',')]
    lines.pop(0)
    boards = []
    board = []
    for line in lines:
        if line == "":
            if len(board) != 5:
                raise ValueError(f"invalid board: {board}")
            boards.append(board)
            board = []
            continue
        row_numbers = [{"number": int(n), "extracted": False} for n in line.split(' ') if n]
        if len(row_numbers) != 5:
            raise ValueError(f"invalid line: {line}")
        board.append(row_numbers)
    if len(board) > 0:
        if len(board) != 5:
            raise ValueError(f"invalid board: {board}")
        boards.append(board)
        board = []
    return boards, numbers

def calculate_score(board, extracted):
    sum = 0
    for row in board:
        for item in row:
            if not item["extracted"]:
                sum += item["number"]
    return sum * extracted

def check_win(board, extracted):
    for x in range(5):
        won = True
        for y in range(5):
            if not board[x][y]["extracted"]:
                won = False
                break
        if won:
            print(calculate_score(board, extracted))
            sys.exit(0)
    for y in range(5):
        won = True
        for x in range(5):
            if not board[x][y]["extracted"]:
                won = False
                break
        if won:
            print(calculate_score(board, extracted))
            sys.exit(0)
    

boards, numbers = parse_input(lines)

for number in numbers:
    for board in boards:
        for row in board:
            for board_item in row:
                if board_item["number"] == number:
                    board_item["extracted"] = True
        check_win(board, number)
