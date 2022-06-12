import view
import board_status_controller as bsc

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False


def take_input(player_token):
   valid = False
   board = bsc.get_board_status()
   while not valid:
      player_answer = view.insert(f"Куда поставим {player_token}?")
      try:
         player_answer = int(player_answer)
      except:
         view.mess("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            bsc.change_board(player_answer-1, player_token)
            valid = True
         else:
            view.mess("Эта клетка уже занята!")
      else:
        view.mess("Некорректный ввод. Введите число от 1 до 9.")

def run(board):
    counter = 0
    win = False
    while not win:
        view.draw_board(bsc.get_board_status())
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(bsc.get_board_status())
           if tmp:
              view.mess(f'{tmp}, выиграл!')
              win = True
              break
        if counter == 9:
            view.mess(f'Ничья!')
            break
    view.draw_board(bsc.get_board_status())


