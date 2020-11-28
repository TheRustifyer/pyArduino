import serial as pySerial
from serial.tools import list_ports
import pyfirmata

class AutoSetUp:

    def __init__(self):

        self.port = None
        self.total_finded_ports = []

    def found_ports(self):

        self.ports = list_ports.comports()

        for port in self.ports:

            self.total_finded_ports.append(port)

        return self.ports


    def find_board(self, founded_ports):
        
        com_port = 'None'
        num_founded_ports = len(founded_ports)
        
        for num in range(0, num_founded_ports):
            
            port = self.ports[num]
            
            str_port = str(port)
            
            if 'Arduino' in str_port or 'USB-SERIAL CH340' in str_port: #Check for more Chinese motherboards
                
                splitted_str_port = str_port.split(' ')
                com_port = (splitted_str_port[0])

        return com_port
            
    def autoconnect_board(self):                
        
        founded_ports = self.found_ports()       
        connect_to_port = self.find_board(founded_ports)

        if connect_to_port != 'None':

            try:
                
                pySerial.Serial(connect_to_port, baudrate = 9600, timeout=1)

                print(f'Connected to {connect_to_port} succesfully!')

            except IOError as error:

                raise RuntimeError(f'''Can't not open a connection to your board.\n'
                                                Please, verify your set up and try again.\n
                                                {error}''')

        self.port = connect_to_port

        self.board = pyfirmata.Arduino(self.port) #Firmata Board instance (Arduino inherits from Board)

        return self.board