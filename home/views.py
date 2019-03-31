'''
all() 테이블 데이타를 전부 가져오기
get() 하나의 row만 갖고오기
filter() 특정 조건에 맞는 row 가져오기
exclude() 특정 조건s 제외한 나머지 row 가져오기

'''

from django.shortcuts import render, render_to_response
from home.models import *
import requests
import logging
from selenium import webdriver as webb
#webdirver path setting module
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
sys.path.append('/home/chanho/pysrc/myweb/home/')

from my_module import crawling, chat_bot, auction_crawling
import telegram
import time

logger = logging.getLogger(__name__)
data = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



#가져온 데이터 가공하기 (html 코드를 파이썬 객체로 변환)


def index(req, *args, **kwargs):
    msg = 'my message'
    #use singleton pattern
    cd = crawling.Crawling()
    cr = cd.get_latest()

    chat_bot1 = chat_bot.Chat_Bot(cr)

    with open(os.path.join(BASE_DIR, 'latest.txt'),'r') as f_read:
        before = f_read.readline()
        if before != cr:
            chat_bot1.New_content()
        else:
            chat_bot1.No_new()

    return render(req, 'index.html', {'message':msg})
    #return render_to_response('index.html', {'html':html})

def auction(req):

    Pr = auction_crawling
    Product_item = Pr.get_product_item()
    product_item, item_name = Product_item.get_value()
    saved_dict = {}

    for i in range(len(item_name)):
        saved_dict[item_name[i]] = product_item[i]

    print(saved_dict)

    msg = "success"
    return render(req, 'auction_crawling.html', {'message':msg})



def test(req):
    msg = 'my message'
    fb = Home(name = "kim", email = "hpyho33@naver.com", show = "test")
    fb.save()
    return render(req, 'test.html', {'message':msg})



def create(req):
    if req.method=='POST':
        form = HomeForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/list')
    else:
        form = HomeForm()
    return render(req, 'test2.html', {'form':form})