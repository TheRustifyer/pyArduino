import serial
import time
import pyarduino


class LCD(pyarduino.AutoSetUp):

    # Define some device constants
    SCREEN_WIDTH = 16  # Maximum characters per line

    # Identifiying RAM addresses
    SCREEN_LINE_1 = 0
    SCREEN_LINE_2 = 1 

    #Required to not overlap buffer instructtions
    _BUFFER_WAIT = 0.5 #Do not ERASE or set to 0


    def __init__(self, *args, **kwargs):

        self.port = pyarduino.AutoSetUp().find_board()
        self.ser = serial.Serial(self.port)
    
    def lcd_init(self):
    
    # Initialise display
        self.ser.write(str.encode("clear_lcd"))
        time.sleep(2)

    def lcd_clear(self):
        '''Clear screen from previous bytecode'''
        
        self.ser.write(str.encode("clear_lcd"))
        time.sleep(LCD._BUFFER_WAIT)

    def arduino_read(self, times=1):
        '''Read data from PORT buffer''' 
        
        self.data =[]
        
        try:

            # for num in range(times):
                
            self.ser.write(str.encode("read_buff"))
            b = self.ser.readline()         # read a byte string
            string_n = b.decode()  # decode byte string into Unicode  
            string = string_n.strip() # remove \n and \r
            print(string)
            
            for word in string.split(','):                              
                if word.startswith(' '):
                    word = word[1:]
                self.data.append(word)


        except KeyboardInterrupt:

            print('Finished by user.')

        return self.data

    def lcd_write(self, message, line):
        '''Print desired string on LCD.'''
        
        message = message.ljust(LCD.SCREEN_WIDTH," ")
        encoded_msg = f'{message},{str(line)}'.encode()
        self.ser.write(bytes(encoded_msg))
        time.sleep(LCD._BUFFER_WAIT)
         

class DHT22:

    def __init__(self):
    
        self.my_lcd = LCD()
        self.my_lcd.lcd_init()
    
    def DHT22_lectures_to_LCD(self, n_loops):    

        self.my_lcd.lcd_write("Hello!",LCD.SCREEN_LINE_1)
        self.my_lcd.lcd_write("Info availiable",LCD.SCREEN_LINE_2)
        self.my_lcd.lcd_clear()
        self.my_lcd.lcd_write("Waiting for ",LCD.SCREEN_LINE_1)
        self.my_lcd.lcd_write("results...",LCD.SCREEN_LINE_2)
        self.my_lcd.lcd_clear()
        
        for _ in range(n_loops):
            self.my_lcd.arduino_read()
            self.my_lcd.lcd_write(self.my_lcd.data[0], LCD.SCREEN_LINE_1)
            self.my_lcd.lcd_write(self.my_lcd.data[1], LCD.SCREEN_LINE_2)


if __name__ == '__main__':

    try:
        
        sensor = DHT22()
        sensor.DHT22_lectures_to_LCD(50)

    except KeyboardInterrupt:

        print('Stoped by user.')