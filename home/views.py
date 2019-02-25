'''
all() 테이블 데이타를 전부 가져오기
get() 하나의 row만 갖고오기
filter() 특정 조건에 맞는 row 가져오기
exclude() 특정 조건s 제외한 나머지 row 가져오기

'''

from bs4 import BeautifulSoup as bs
from django.shortcuts import render, render_to_response
from home.models import *
import requests
import logging

logger = logging.getLogger(__name__)

data = {}

class crawling:
    def __init__(self):
        LOGIN_INFO = {
            'userid': 'hpyho',
            'userPassword': '7513aa',
        }

        with requests.Session() as s:
            # 크롤링 한 데이터 가져오기
            Req = s.get("https://www.clien.net/service/")

            # 크롤링된 데이터를 분류
            html = Req.text

            #html코드를 python객체로 변환
            soup = bs(html, 'html.parser')

            # input 태그 중 name이 _csrf인 값을 찾는다
            csrf = soup.find('input', {'name': '_csrf'})
            print(csrf['value'])

            #로그인 객채 매핑 이유 모름.
            LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}
            print(LOGIN_INFO)

            #로그인 요청
            login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
            print(login_req.status_code)
            # header = Req.headers
            # status = Req.status_code


#가져온 데이터 가공하기 (html 코드를 파이썬 객체로 변환)
'''
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h3 > a'
)
'''
'''for title in my_titles:
    data[title.text] = title.get('href')
    print(title.text)   
'''


def index(req, *args, **kwargs):
    msg = 'my message'my
    #use singleton pattern
    cr = crawling()


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