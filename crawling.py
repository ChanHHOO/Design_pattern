import requests
from bs4 import BeautifulSoup as bs

class Crawling:
    def __init__(self):
        LOGIN_INFO = {
            'userid': 'hpyho',
            'userPassword': '7513aa',
        }
        self.latest = ""
        with requests.Session() as s:
            #requests.Session() -> s 치환

            # 크롤링 한 데이터 가져오기
            Req = s.get("https://www.clien.net/service/group/allsell")
            Req.encoding = 'utf8'
            # 크롤링된 데이터를 분류
            html = Req.text

            #html코드를 python객체로 변환
            soup = bs(html, 'html.parser')

            # input 태그 중 name이 _csrf인 값을 찾는다
            #csrf = soup.find('input', {'name': '_csrf'})


            #로그인 객채 매핑 이유 모름.
            #LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': csrf['value']}}

            #로그인 요청
            #login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
            #print(login_req.status_code)

            #로그인 세션 유지 -> 게시판 글 가져오기
            #post_one = s.get('https://www.clien.net/service/board/rule/10707408')
            #soup = bs(post_one.text, 'html.parser')

            #공지글 제목과 본문을 가져온다
            title = soup.select('#div_content > div:nth-child(7) > div.list_title > a > span.subject_fixed')
            self.latest = title[0].text

    def get_latest(self):
        return self.latest