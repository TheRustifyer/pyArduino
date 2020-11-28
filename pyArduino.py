import pyfirmata
import time
from auto_connect import AutoSetUp

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

    def sketch_availiable_layout_config(self):

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
        
        self.max_total_pins = max(digital)
        return self.max_total_pins

if __name__ == "__main__":

    info = ShowConnectionInfo()
    info.show_info()
    info.sketch_availiable_layout_config()
    max_pins = info.max_total_pins

    board = info.board


it = pyfirmata.util.Iterator(info.current_port)
it.start()


input, output = 'i', 'o'
options = [input, output]

for idx, option in enumerate(options):

    if idx == 0:
        
        print(f'Checking input pins\n')

    else:

        print(f'\nChecking output pins\n')
    
    for number in range(0, max_pins + 1):
        
        str_number = str(number)

        try:
            
            digital = board.get_pin(f'd:{str_number}:{options}')
            
            if digital != None:
                
                print(f'Digital Pin nº {str_number} is responsing {digital.read()}')

            else:

                print('''You probably set PIN on an incorrect way.\n
                Check I/O are correct.''')

        except:

            print(f'Pin {str_number} is not connected to motherboard. \n Trying next...')

