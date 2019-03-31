
import logging
from selenium import webdriver as webb
#webdirver path setting module
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
from bs4 import BeautifulSoup as bs


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

