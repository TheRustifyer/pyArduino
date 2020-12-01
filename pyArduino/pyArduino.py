import pyfirmata
import time

import serial as pySerial
from serial.tools import list_ports

class AutoSetUp:

    def __init__(self):

        self.port = None
        
        self.total_finded_ports = []
        
        self.my_serial = None

    def found_ports(self):

        self.ports = list_ports.comports()

        for port in self.ports:

            self.total_finded_ports.append(port)

        return self.ports


    def find_board(self, founded_ports=0):

        try:

            founded_ports = len(self.found_ports())

            if founded_ports != 0:
    
                com_port = 'None'
                
                for num in range(0, founded_ports):
                    
                    port = self.ports[num]
                    
                    str_port = str(port)
                    
                    if 'Arduino' in str_port or 'USB-SERIAL CH340' in str_port: #Check for more Chinese motherboards
                        
                        splitted_str_port = str_port.split(' ')
                        com_port = (splitted_str_port[0])

                    else:

                        raise pySerial.SerialException('Cannot find compatible boards.')
        
        except IOError as error:

            print(f'No port with board founded.\n{error}')

        return com_port
            
    def autoconnect_board(self):                
        
        founded_ports = self.found_ports()       
        self.port = self.find_board(founded_ports)

        if self.port != 'None':

            try:
                
                self.my_serial = pySerial.Serial(self.port, baudrate = 9600, timeout=1)

                print(f'Connected to {self.port} succesfully!')

                self.my_serial.close()

            except IOError as error:

                raise RuntimeError(f'''Can't not open a connection to your board.\n'
                Please, verify your set up and try again.\n
                {error}''')

        self.board = pyfirmata.Arduino(self.port) #Firmata Board instance (Arduino inherits from Board class)

        return self.board

class AutoConnection(AutoSetUp):

    def __init__(self):

        super().__init__()

        self.board = self.autoconnect_board()
        
        self.current_port = self.port

        if self.board.name == self.current_port:
            self.board.name = 'Chinese Arduino'
       

class ShowConnectionInfo(AutoConnection):
    
    def __init__(self):

        super().__init__()

        self.layout = self.board._layout
                
    def show_info(self):
        
        print(f'\nConnected board has been identified as {self.board.name}, has {self.board.firmware} as firmware.')
        print(f"It's connected to {str(self.current_port)} port and it's using the version ")
        print(f"{str((self.board.get_firmata_version())).strip('()').replace(',','.').replace(' ','')} of Arduino's FIRMATA PROTOCOL.\n")

    def board_config(self):

        if 'digital' in self.layout:

            digital = self.layout['digital']
            digital_str = ", ".join(list(map(str, digital))).replace('()', ' ') #I know, i know... just for fun :)

        else:

            print(f'No digital ports availiables for this {self.board.name}')

        if 'analog' in self.layout:

            analogic = self.layout['analog']
            analogic = ", ".join(list(map(str, analogic))).replace('()', ' ')

        else:

            print(f'No analogic ports availiables for this {self.board.name}')

        if 'pwm' in self.layout:

            pwm = self.layout['pwm']
            pwm = ", ".join(list(map(str, pwm))).replace('()', ' ')

        else:

            print(f'No pwm ports availiables for this {self.board.name}')

        if 'use_ports' in self.layout:

            servo = self.layout['use_ports']
            
        else:

            print(f'No servo functionality for this {self.board.name}')

        if 'disabled' in self.layout:

            disabled = self.layout['disabled']
            disabled = ", ".join(list(map(str, disabled))).replace('()', ' ')
            
        else:

            print('All ports showed are availiable!')

        print(f'''Availiable pre-builded connections for {self.board.name} are:\n
        Digital ports: {digital_str}
        Analogic Ports: {analogic}
        PWM ports: {pwm}
        Servo enabled?: {servo}
        Disabled Ports: {disabled}\n''')

    def board_number_pins(self):
        '''Method that returns an int with total board pins'''
        targets = [self.layout['digital'], self.layout['analog'], self.layout['pwm']]

        number_of_ports_by_category = [num for value in targets for num in value]
        
        return max(number_of_ports_by_category)

    def pin_status(self):

        input, output = 'i', 'o'
        options = [input, output]
        max_pins = self.board_number_pins()

        for idx, _ in enumerate(options):

            if idx == 0:
                
                print(f'Checking input pins\n')

            else:

                print(f'\nChecking output pins\n')
            
            for number in range(0, max_pins + 1):
                
                str_number = str(number)

                try:
                    
                    digital = self.board.get_pin(f'd:{str_number}:{options}')
                    
                    if digital != None:
                        
                        print(f'Digital Pin nº {str_number} is responsing {digital.read()}')

                    else:

                        print('''You probably set PIN on an incorrect way.\n
                        Check I/O are correct.''')

                except:

                    print(f'Pin {str_number} is not connected to motherboard. \n Trying next...')
