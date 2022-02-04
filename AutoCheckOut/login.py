#!/usr/bin/env python

from time import sleep, localtime

from selenium.webdriver import Chrome

LOGIN = 1
SURVEY = 2

TODAY = 1
FUTURE = 2
PAST = 3

MAIN_PATH = __file__ + '\\..\\'
ID_PATH = '//*[@id="userId"]'
PW_PATH = '//*[@id="userPwd"]'
LOGIN_PATH = '//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a'
FIND_PATH = '//*[@id="wrap"]/form/div/div[2]/div/div/ul/li[10]/div/div[1]/dfn'

class AutoCheckOut:
    def __init__(self, urltxt=None, idtxt=None, surveytxt=None, debug=False):
        self.__url = str()
        self.__checkout = str()
        self.__checkin = str()
        self.__id = str()
        self.__password = str()
        self.__where = str()
        self.__surveyUrl = str()
        self.__surveyXpath = str()
        self.__surveyOutXpath = list()
        self.__surveyInXpath = list()
        self.debug = debug
        self.sleepTime = 0

        self.idtxt = idtxt
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')

        if not debug:
            self.driver.minimize_window()
            self.__loadURL(urltxt, surveytxt)
            self.__loadID()

    def __loadURL(self, urltxt, stxt):
        temp = list()
        with open(MAIN_PATH + urltxt, 'r') as F:
            self.__url = F.readline()
            self.__url = self.__url.strip('\n')
            self.__checkout = F.readline()
            self.__checkout = self.__checkout.strip('\n')
            self.__checkin = F.readline()
        with open(MAIN_PATH + stxt, 'r') as S:
            self.__surveyUrl = S.readline()
            self.__surveyUrl = self.__surveyUrl.strip('\n')
            self.__surveyXpath = S.readline()
            self.__surveyXpath = self.__surveyXpath.strip('\n')
            temp = S.readlines()
            temp = list(map(lambda s: s.strip('\n'), temp))
            self.__surveyOutXpath = temp[:10]
            del temp[:10]
            self.__surveyInXpath = temp

    def __loadID(self):
        try:
            with open(MAIN_PATH + self.idtxt, 'r') as F:
                self.__id = F.readline()
                self.__id = self.__id.strip('\n')
                self.__password = F.readline()
                self.__password = self.__password.strip('\n')
                self.__where = F.readline()
        except:
            self.__id = 'example@hello.com'
            self.__password = '1q2w3e4r'
            self.__where = '서울/역삼동/자택'

    def rebootDriver(self):
        self.driver.quit()
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')
        self.driver.minimize_window()

    def receiveID(self, id, pw, wh=None):
        self.__id = id
        self.__password = pw
        self.__where = wh
        if not self.debug:
            with open(MAIN_PATH + self.idtxt, 'w') as F:
                F.write(f'{id}\n{pw}\n{wh}')

    def receiveURL(self, url):
        self.__url = url

    def openURL(self, url=LOGIN):
        if url==LOGIN:
            self.driver.get(self.__url)
            self.driver.implicitly_wait(5)
            sleep(self.sleepTime)
        elif url==SURVEY:
            self.driver.get(self.__surveyUrl)
            self.driver.implicitly_wait(5)
            sleep(self.sleepTime)

    def login(self, idpath=ID_PATH, pwpath=PW_PATH, loginpath=LOGIN_PATH):
        _id = self.driver.find_element_by_xpath(idpath)
        _password = self.driver.find_element_by_xpath(pwpath)

        _id.send_keys(self.__id)
        _password.send_keys(self.__password)

        sleep(1)

        self.driver.find_element_by_xpath(loginpath).click()
        self.driver.implicitly_wait(5)
        sleep(self.sleepTime)
        return True
    
    def checkOut(self):
        self.driver.find_element_by_xpath(self.__checkout).click()
        sleep(1)

    def checkIn(self):
        self.driver.find_element_by_xpath(self.__checkin).click()
        sleep(1)

    def _findSurvey(self, isOut):
        survey_txt = self.driver.find_element_by_xpath(FIND_PATH).text
        survey_date = survey_txt[:6]
        if isToday(survey_date) == TODAY:   # 마지막 설문조사 날짜가 오늘일 때
            if isOut:                       # 퇴실일 경우
                if '오후 건강현황' in survey_txt:
                    pass # 일단 10번쨰거 확인하고, 미래꺼면 2페이지로 넘어가기
                         # today면 10을 return하고, 과거꺼면 원래 방식대로 찾아서 i(행 number) 출력


    def survey(self, isOut):
        print('설문조사시작')
        sleep(1)
        for i in range(10, 0, -1):
            _xpath = self.__surveyXpath.replace('/li[10]', f'/li[{i}]')
            try:
                if self.driver.find_element_by_xpath(_xpath):
                    self.driver.find_element_by_xpath(_xpath).click()
                    sleep(2)
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.implicitly_wait(5)
                    sleep(2)
                    sleep(self.sleepTime)
                    break
            except:
                print(f'survey line {i} is disable')
        else:
            return False
        try:
            if isOut:       # 퇴실하기
                self.driver.find_element_by_xpath(self.__surveyOutXpath[0]).click()
                self.driver.implicitly_wait(5)
                sleep(self.sleepTime)
                outwhere = self.driver.find_element_by_xpath(self.__surveyOutXpath[1])
                outwhere.send_keys(self.__where)    #서울/역삼동
                sleep(self.sleepTime)
                for xpath in self.__surveyOutXpath[2:]:
                    self.driver.find_element_by_xpath(xpath).click()
                    self.driver.implicitly_wait(5)
                    sleep(self.sleepTime)
            else:           # 입실하기
                self.driver.find_element_by_xpath(self.__surveyInXpath[0]).click()
                self.driver.implicitly_wait(5)
                sleep(self.sleepTime)
                inwhere = self.driver.find_element_by_xpath(self.__surveyInXpath[1])
                inwhere.send_keys(self.__where)    #서울/역삼동
                sleep(self.sleepTime)
                for xpath in self.__surveyInXpath[2:]:
                    self.driver.find_element_by_xpath(xpath).click()
                    self.driver.implicitly_wait(5)
                    sleep(self.sleepTime)
        except:
            return False
        return True

    def maximize(self):
        self.driver.maximize_window()

    def slowMode(self, isSlow=True):
        if isSlow:
            self.sleepTime = 2
        else:
            self.sleepTime = 0
    
    def getIDPW(self):
        return self.__id, self.__password, self.__where

    def clickXpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

def today():
    year = str(localtime().tm_year)[2:]
    month = str(localtime().tm_mon)
    day = str(localtime().tm_mday)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return year + month + day

def isToday(day):
    _today = int(today())
    _date = int(day)
    if _today == _date:
        return TODAY
    elif _today > _date:
        return PAST
    elif _today < _date:
        return FUTURE
