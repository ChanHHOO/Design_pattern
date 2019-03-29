'''
all() 테이블 데이타를 전부 가져오기
get() 하나의 row만 갖고오기
filter() 특정 조건에 맞는 row 가져오기
exclude() 특정 조건s 제외한 나머지 row 가져오기

'''

from django.shortcuts import render, render_to_response
from home.models import *

import logging
from selenium import webdriver as webb
#webdirver path setting module
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
sys.path.append('/home/chanho/pysrc/myweb/home/')

import crawling
import chat_bot
import telegram
import time




logger = logging.getLogger(__name__)
data = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))






class WebdriveSetting:
    def __init__(self):
        self.driver = webb.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        #driver = webdriver.PhantomJS('~/pysrc/myweb/home/phantomjs')
        self.driver.get("http://localhost:8001")



class login_page(WebdriveSetting):
    def __init__(self):
        WebdriveSetting.__init__(self,)
        self.driver.find_element_by_name('email').send_keys('hpyho33@naver.com')
        self.driver.find_element_by_name('password').send_keys('7513aa')
        self.driver.find_element_by_xpath('//*[@id="login"]').click()


class goAnotherPage(login_page):
    def __init__(self):
        login_page.__init__(self,)
        self.driver.get('http://localhost:8001/selled_item')
        self.html = self.driver.page_source
        self.soup = bs(self.html, 'html.parser')
        self.val = self.soup.select('body > div > table > tbody')

    def get_value(self):
        return self.val


class get_product_item(goAnotherPage):
    def __init__(self):
        goAnotherPage.__init__(self,)
        self.tr_data = self.val[0].find_all('th')
        self.tr_list = [i.get_text() for i in self.tr_data]
        #zz

        self.td_data = self.val[0].find_all('td')
        self.td_list = []
        self.td_dic = {}
        index = 0
        self.td_keys = ['seller', 'start_price', 'current_price', 'ended_time']

        for value in range(int(len(self.td_data) / 4)):
            for i in range(4):
                self.td_dic[self.td_keys[i]] = self.td_data[index].get_text()
                index += 1
            # print(td_dic)
            self.td_list.append(self.td_dic.copy())

        print(self.td_list)

    def get_value(self):
        return self.td_list, self.tr_list



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





    '''Product_item = get_product_item()
    product_item, item_name = Product_item.get_value()
    saved_dict = {}

    for i in range(len(item_name)):
        saved_dict[item_name[i]] = product_item[i]

    print(product_item[0])
    '''

    return render(req, 'index.html', {'message':'bb'})
    #return render_to_response('index.html', {'html':html})


def test(req):
    msg = 'my message'
    fb = Home(name = "kim", email = "hpyho33@naver.com", show = "test")
    fb.save()
    return render(req, 'test.html', {'message':msg})

def test2(req):
    msg = "success"
    return render(req, 'test2.html', {'messate':msg})

def create(req):
    if req.method=='POST':
        form = HomeForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/home/list')
    else:
        form = HomeForm()
    return render(req, 'test2.html', {'form':form})