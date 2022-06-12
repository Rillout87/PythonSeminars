import view
import board_status_controller as bsc
import game

def start_game():
    view.start_message()
    bsc.create_board()
    
    game.run(bsc.get_board_status())

    input("Нажмите Enter для выхода!")
