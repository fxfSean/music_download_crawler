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


def drive():
    #     url = 'https:\/\/m10.music.126.net\/20220405202052\/68a3bf1398379f4bc04e25c136fb97e6\/ymusic\/6ce6\/b2c1\/9fac\/ed75227c13e71a49cb885007385d08c2.mp3'
    #     d = "https://m801.music.126.net/20220405222710/759e8f9e884f74484806489a5027be99/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/12606051372/7f1a/d83b/da7b/04d69c5326d7348d58c6940974f96102.mp3"
    #     print(d)
    #     response = requests.get(d)
    # print(response)
    #     open("11.mp3", "wb").write(response.content)
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt)
    driver.get('http://music.zhuolin.wang/')
    time.sleep(5)

    # driver.find_element(by=By.ID, value='kw').send_keys('小米')
    # a = driver.find_element(by=By.XPATH, value="//a[contains(text(),'等会再说')]")
    # print(str(a))
    # a.click()
    print('click after')
    driver.execute_script('''
    elems = document.getElementsByClassName('list-menu');
    for (var i=0;i<elems.length;i+=1){
        elems[i].style.display = 'block';
    }
    ''')
    time.sleep(10)
    parent = driver.find_element(by=By.XPATH, value="//div[@id='mCSB_2_container']")
    names = driver.find_elements_by_class_name('list-item')[1:]
    songIndex = 0
    for name in names:
        print('name: ' + name.text)
        list = str(name.text).split('\n')
        song = list[len(list) - 1]
        print('下载第：' + str(songIndex) + ' 首：' + song)
        # driver.find_element(by=By.XPATH, value="//span[@title='点击下载这首歌']").click()
        # contpayment = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[@title='点击下载这首歌']")))
        # contpayment.click()
        # time.sleep(2)
        # driver.switch_to.window(driver.window_handles[1])
        print('下载连接：' + driver.current_url)
        print('歌名：' + song)
        # response = requests.get(driver.current_url)
        # print(response)
        # open(song + ".mp3", "wb").write(response.content)

    print(str(parent))
    print('execute script')
    # time.sleep(5)
    # driver.switch_to.window(driver.window_handles[1])
    # print(driver.current_url)

    time.sleep(100)
#     print(d)
