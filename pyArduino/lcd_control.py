import serial
import time
import pyArduino


class LCD(pyArduino.AutoSetUp):

        # Define some device constants
    LCD_WIDTH = 16    # Maximum characters per line

    LCD_LINE_1 = 0 # LCD RAM address for the 1st line
    LCD_LINE_2 = 1 # LCD RAM address for the 2nd line

    #No vaya a ser que me caiga esto a pique
    _BUFFER_WAIT = 0.5 #Do not ERASE or set to 0

    # port = None
    # ser = serial.Serial(port, 9600)

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


    def lcd_string(self, message,line):
        '''Print desired string on LCD.'''
        
        message = message.ljust(LCD.LCD_WIDTH," ")
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

        my_lcd.lcd_string("Hola Luz e Andre",LCD.LCD_LINE_1)
        my_lcd.lcd_string("Son o Alex!",LCD.LCD_LINE_2)

       