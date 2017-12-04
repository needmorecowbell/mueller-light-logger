# Serial Light Controller / Logger #

## Requirements ##
- Python 3.6

## Setup ##
1. Clone this repository

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
