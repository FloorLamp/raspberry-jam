Raspberry Jam
===========================

This will eventually be a home control center. Right now it only has temperature logging.

# Installation

The web app uses flask, uwsgi and nginx.

Install dependencies:

    pip install -r requirements.txt
    apt-get install nginx uwsgi uwsgi-plugin-python
    
Edit `deploy/uwsgi.ini` to point to your project directory.
    
Copy config files:

    sudo cp deploy/uwsgi.ini /etc/uwsgi/apps-enabled/
    sudo cp deploy/nginx.conf /etc/nginx/sites-enabled/jam
    
Restart uwsgi and nginx:

    sudo service uwsgi restart
    sudo service nginx restart
    
## Temperature Control

This uses a DS18B20 temperature sensor. For the full parts list, see [here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/parts). Assembly instructions can be found [here](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/hardware).

To collect temperature every minute, add the following to your crontab:

    * * * * * project_dir/log_temp.py



