

def start_message ():
    print("*" * 10, " Игра Крестики-нолики для одного ", "*" * 10)

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def mess (text):
    print(text)

def insert(text):
    return input(text)