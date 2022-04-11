import urllib
from urllib.parse import unquote
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import requests
import json
import os

from china_golden import china_golden
from china_top import china_top
from create_top import create_top
from europe_new_songs import europe_new_songs
from europe_top import europe_songs
from farm_songs import farm_songs
from hongkong_top import hongkong_top
from hot_songs import new_songs, hot_songs

from japan_top import japan_top
from old_school_songs import old_school_songs
from rock_songs import rock_songs
from south_korea_top import south_korea_top
from speak_songs import speak_songs
from speed_up_songs import speed_up_songs


def download_music():
    music_sets = {
        'china_golden': china_golden,
        'china_top': china_top,
        'create_top': create_top,
        'europe_new_songs': europe_new_songs,
        'europe_top': europe_songs,
        'farm_songs': farm_songs,
        'hongkong_top': hongkong_top,
        'hot_songs': hot_songs,
        'new_songs': new_songs,
        'japan_top': japan_top,
        'old_school_songs': old_school_songs,
        'rock_songs': rock_songs,
        'south_korea_top': south_korea_top,
        'speak_songs': speak_songs,
        'speed_up_songs': speed_up_songs
    }
    for key in music_sets:
        print(key + ':')
        os.system('mkdir ' + key)
        down_task(key, music_sets[key])


def down_task(key, value):
    url = 'https://api.zhuolin.wang/api.php?callback=jQuery111305275055645768552_1649501603997&types=url&id='
    urlTail = '&source=netease&_=1649501604001'
    board = json.loads(value)['playlist']
    tracks = board['tracks']
    print(len(tracks))
    for index, item in enumerate(tracks):
        print('下载：' + str(item['name']) + ' : ' + str(item['id']))
        querySongUrl = url + str(item['id']) + urlTail
        print(querySongUrl)
        print('***************')
        songUrlResp = requests.get(querySongUrl)
        print(songUrlResp.content)
        songBody = str(songUrlResp.content).split('(')[1].split(')')[0]
        print('***************')
        print(songBody)
        songBean = json.loads(songBody)
        download_url = str(songBean['url']).replace('\/', '/')
        print(download_url)
        if not download_url.startswith('http'):
            print('skip')
            continue
        response = requests.get(download_url)
        open(str(item['name']).replace('/', '') + ".mp3", "wb").write(response.content)
        time.sleep(1)
    os.system('mv *.mp3 ' + key)



if __name__ == '__main__':
    download_music()
