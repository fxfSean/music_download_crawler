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
from hot_songs import new_songs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from japan_top import japan_top
from old_school_songs import old_school_songs
from rock_songs import rock_songs
from south_korea_top import south_korea_top
from speak_songs import speak_songs
from speed_up_songs import speed_up_songs


def download_music():
    url = 'https://api.zhuolin.wang/api.php?callback=jQuery111305275055645768552_1649501603997&types=url&id='
    urlTail = '&source=netease&_=1649501604001'
    singleSong = 'jQuery111305275055645768552_1649501603997({"url":"https:\/\/m701.music.126.net\/20220409193638\/7d420735903e072e05bf934b9177e223\/jdymusic\/obj\/wo3DlMOGwrbDjj7DisKw\/11983356173\/ed2f\/6024\/be41\/2dc456563c5f9c9535b75ecb066c0325.mp3","size":4096941,"br":128.001})'
    bean = singleSong.split('(')[1].split(')')[0]
    print(bean)
    board = json.loads(south_korea_top)['playlist']
    tracks = board['tracks']
    print(len(tracks))
    for index, item in enumerate(tracks):
        # if index < 100:
        #     continue
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


if __name__ == '__main__':
    download_music()
