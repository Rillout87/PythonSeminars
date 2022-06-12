
def create_board():
    with open('board_status.txt', 'w') as file:
        board = list(range(1,10))
        for cell in board:
            file.write(f'{cell}\n')

def get_board_status():
    with open('board_status.txt', 'r') as status:
        board = [line.rstrip('\n') for line in status.readlines()]
        
    return board

def change_board(cell, value):
    with open('board_status.txt', 'r') as status:
        board = [line.rstrip('\n') for line in status.readlines()]
        board[cell] = value
    with open('board_status.txt', 'w') as file:    
        for cl in board:
            file.write(f'{cl}\n')


