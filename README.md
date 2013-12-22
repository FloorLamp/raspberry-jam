Raspberry Pi Command Center
===========================

This will eventually be a home control center. Right now it only has temperature logging.

## Temperature Control

This uses a DS18B20 temperature sensor. For the full parts list, see [here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/parts). Assembly instructions can be found [here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/hardware).

To collect temperature every minute, add the following to your crontab:

    * * * * * project_dir/log_temp.py

## Web app

This uses Flask. To run, just install the requirements and run the server.

    pip install -r requirements.txt
    python server.py
