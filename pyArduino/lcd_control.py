import serial
import time
import pyArduino


class LCD(pyArduino.AutoSetUp):

    # Define some device constants
    SCREEN_WIDTH = 16  # Maximum characters per line

    # Identifiying RAM addresses
    SCREEN_LINE_1 = 0
    SCREEN_LINE_2 = 1 

    #Required to not overlap buffer instructtions
    _BUFFER_WAIT = 0.5 #Do not ERASE or set to 0


    def __init__(self, *args, **kwargs):

        self.port = pyArduino.AutoSetUp().find_board()
        self.ser = serial.Serial(self.port)
    
    def lcd_init(self):
    
    # Initialise display
        self.ser.write(str.encode("clear_lcd"))
        time.sleep(2)

    def lcd_clear(self):
        '''Clear screen from previous bytecode'''
        
        self.ser.write(str.encode("clear_lcd"))
        time.sleep(LCD._BUFFER_WAIT)


    def lcd_write(self, message, line):
        '''Print desired string on LCD.'''
        
        message = message.ljust(LCD.SCREEN_WIDTH," ")
        encoded_msg = f'{message},{str(line)}'.encode()
        self.ser.write(bytes(encoded_msg))
        time.sleep(LCD._BUFFER_WAIT) 

if __name__ == '__main__':

    try:
        my_lcd = LCD()
        my_lcd.lcd_init()

    except KeyboardInterrupt:

        pass

    finally:

        my_lcd.lcd_write("Hola Luz e Andre",LCD.SCREEN_LINE_1)
        my_lcd.lcd_write("Son o Alex!",LCD.SCREEN_LINE_2)

       