# main.py

import configparser
import datetime
import requests
from PIL import ImageGrab

dt_now = datetime.datetime.now()
filename = dt_now.strftime('%H_%M_%S')

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

ImageGrab.grab().save('screenshots/' + filename + '.png')

TOKEN = config_ini['AUTH']['TOKEN']
CHANNEL = config_ini['AUTH']['CHANNEL']

files = {'file': open('screenshots/' + filename + '.png', 'rb')}
param = {
    'token':TOKEN, 
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}
requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

print('screenshots/' + filename)