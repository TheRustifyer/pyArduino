# pyArduino

![PyPI License](https://img.shields.io/pypi/l/pyArduino)
![PyPI version](https://img.shields.io/pypi/v/pyArduino)

Welcome to the implementation of PyArduino on Python as handler for Arduino boards.

[Find it Here](https://pypi.org/project/pyArduino/0.2.2/)

## Description

pyArduino it's a library on current development to allow programmers to easy handle data and actions over Arduino hardware.

## Purpose

This package allows you to automate several things:

1. Autodetect COM or TTY port when Arduino is detected.
2. Get info about the board, like his name, protocols, firmware versions...
3. Handling data directly from your Python interpreter.

## About

You can now use the implemented classes for friendly manage your board from Python.
At 01(day)/12(month)/2020, when package it's released on his 0.1.0 version,
you can send data to a 16x2 LCD Screen, being able to send strings to it throught a buffer as main feature, or get data and OPEN and CLOSE serial ports
or autodetect whenever Arduino (or a copy of him it's connected.)

## Download

· First of all, install Python if you're not.

· Type on your CMD or Terminal:
```pip install pyArduino```

Wait until download finishes... and... It's ready.

NOTE: If you dont have pip package manager installated, go google it and install it.
 
## Examples

You have a folder inside project's folder called 'examples', with current up-to-date code based on what modules are being deployed over time.

### Little example


if __name__ == '__main__':
    
    # 1st instanciate the ShowConnectionInfo Class, which autoconnect your board via Serial module
    # due to inheritance properties, and will give you a full review of your board capabilities.
    info = pyArduino.ShowConnectionInfo()

    # This 'show_info()' method gives you back basic info about the status
    info.show_info()

    # Shows you current layout config of your board
    info.board_config()

    # if you need to get for your software how many pins you have without hardcoring the number  
    total_pins = info.board_number_pins()
    print(total_pins)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/Pyzyryab/pyArduino/blob/master/LICENSE)

# Credits

Libraries used here for build this project are pyfirmata and pyserial, so thanks to his
creators for his hard work.
