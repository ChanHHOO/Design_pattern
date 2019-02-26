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

from selenium import webdriver as webb

#webdirver path setting module
from webdriver_manager.chrome import ChromeDriverManager




logger = logging.getLogger(__name__)
data = {}


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


class crawling:
    def __init__(self):
        LOGIN_INFO = {
            'userid': '',
            'userPassword': '',
        }

        with requests.Session() as s:#  requests.Session() -> s 치환


            # 크롤링 한 데이터 가져오기
            Req = s.get("https://www.clien.net/service/")

            # 크롤링된 데이터를 분류
            html = Req.text

            #html코드를 python객체로 변환
            soup = bs(html, 'html.parser')

            # input 태그 중 name이 _csrf인 값을 찾는다
            csrf = soup.find('input', {'name': '_csrf'})


            #로그인 객채 매핑 이유 모름.
            LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}

            #로그인 요청
            login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
            print(login_req.status_code)

            #로그인 세션 유지 -> 게시판 글 가져오기
            post_one = s.get('https://www.clien.net/service/board/rule/10707408')
            soup = bs(post_one.text, 'html.parser')

            #공지글 제목과 본문을 가져온다
            title = soup.select('#div_content > div.post_title.symph_row > h3 > span')
            contents = soup.select('#div_content > div.post_view > div.post_content > article > div')

            print(title[0].text +"\n"+contents[0].text)

            # header = Req.headers
            # status = Req.status_code


#가져온 데이터 가공하기 (html 코드를 파이썬 객체로 변환)


def index(req, *args, **kwargs):
    msg = 'my message'
    #use singleton pattern
    #cr = crawling()
    we = goAnotherPage()
    val = we.get_value()



    td_data = val[0].find_all('td')
    td_list = []
    td_dic = {}
    index = 0
    td_keys = ['seller', 'start_price', 'current_price', 'ended_time']
    for value in range(int(len(td_data)/4)):
        for i in range(4):
            td_dic[td_keys[i]] = td_data[index]
            index += 1
        #print(td_dic)
        td_list.append(td_dic.copy())
    print(td_list)

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
