# Serial Light Controller / Logger #

## Requirements ##
- Python 3.6

## Setup ##
i1. Clone this repository

 `git clone https://github.com/needmorecowbell/mueller-light-logger.git`

2. Install the repository's required libraries

  `pip install -r requirements.txt`

3. Run calibrate.py or controller.py

  `python calibrate.py` or `python controller.py`

## Configuration ##

  Most of the configuration has been done for you. To alter the time/intensity periods,
  go to the logging_template.csv file and edit the values there. You can add as many as you
  want, but only use integers, and don't remove the first line. Time delay is set in minutes.

  Make sure Arduino is plugged in **before** running this software.

## Calibration (Windows) ##

1. Enter this directory (ex: C:/users/darren/desktop/mueller-light-logger/)
2. Double click calibrate.py
3. Enter in COM Port Displayed on screen
4. Type in 9600 as baudrate
5. Upon connection, follow instructions and press q to exit when prompted
6. When finished, data will be in a csv file with a timestamp as the name.
7. This csv file can be imported as a data source in excel and then graphed

## Controller (Windows) ##

1. Enter this directory (ex: C:/users/darren/desktop/mueller-light-logger/)
2. Double click controller.py
3. Enter in COM Port Displayed on screen
4. Type in 9600 as baudrate
5. Upon connection, the light will be dimmed in accordance to the timeschedule provided in logging_template.csv
6. When finished, you can unplug the controller to turn off the lights.





