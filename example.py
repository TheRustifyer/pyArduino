import pyArduino

if __name__ == "__main__":

    
    info = pyArduino.ShowConnectionInfo()
    info.show_info()
    info.board_config()
    max_pins = info.max_total_pins

    board = info.board

    total_pins = info.board_number_pins()
    print(total_pins)