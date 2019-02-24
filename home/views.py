'''
all() 테이블 데이타를 전부 가져오기
get() 하나의 row만 갖고오기
filter() 특정 조건에 맞는 row 가져오기
exclude() 특정 조건을 제외한 나머지 row 가져오기

'''

from django.shortcuts import render
from home.models import *
from datetime import datetime

def index(req):
    msg = 'my message'
    return render(req, 'index.html', {'message':msg})

def test(req):
    msg = 'my message'
    fb = Home(name = "kim", email = "hpyho33@naver.com", show = "test")
    fb.save()
    return render(req, 'test.html', {'message':msg})
def test2(req):
    msg = "success"
    return render(req, 'test2.html', {'messate':msg})