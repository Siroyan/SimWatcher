# main.py

import configparser
import datetime
import requests
import time
from PIL import ImageGrab

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
TOKEN = config_ini['AUTH']['TOKEN']
CHANNEL = config_ini['AUTH']['CHANNEL']

while True:
    dt_now = datetime.datetime.now()
    comment = dt_now.strftime('%Y/%m/%d(%A)%H:%M:%S')
    filename = dt_now.strftime('%H_%M_%S')

    ImageGrab.grab().save('screenshots/' + filename + '.png')
    files = {'file': open('screenshots/' + filename + '.png', 'rb')}
    param = {
        'token':TOKEN, 
        'channels':CHANNEL,
        'filename':filename + '.png',
        'initial_comment': comment,
        'title': "title"
    }
    requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
    time.sleep(30 * 60)