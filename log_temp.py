#!/usr/bin/python

from datetime import datetime
import os
import glob
 
os.system('sudo modprobe w1-gpio')
os.system('sudo modprobe w1-therm')
 
BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_FOLDER = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_FOLDER + '/w1_slave'

if __name__ == '__main__':
    LOG_FILENAME = 'temps.csv'
    LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), LOG_FILENAME)
    
    if not os.path.exists(LOG_PATH):
        open(LOG_PATH, 'w').close()
        
    with open(DEVICE_FILE) as sensor_file, open(LOG_PATH, 'a') as log_file:
        lines = sensor_file.readlines()
        temp = float(lines[1].strip().split('=')[1]) / 1000
        log_file.write('{},{}\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), temp))
        
    exit()