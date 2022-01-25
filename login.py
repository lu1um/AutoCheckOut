#!/usr/bin/env python

from time import sleep

from selenium.webdriver import Chrome

LOGIN = 1
SURVEY = 2

MAIN_PATH = __file__ + '\\..\\'

class AutoCheckOut:
    def __init__(self, urltxt, idtxt, surveytxt):
        self.__url = str()
        self.__checkout = str()
        self.__checkin = str()
        self.__id = str()
        self.__password = str()
        self.__surveyUrl = str()
        self.__surveyXpath = list()

        self.idtxt = idtxt
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')

        self.driver.minimize_window()
        self.__loadURL(urltxt, surveytxt)
        self.__loadID()

    def __loadURL(self, urltxt, stxt):
        with open(MAIN_PATH + urltxt, 'r') as F:
            self.__url = F.readline()
            self.__url = self.__url.strip('\n')
            self.__checkout = F.readline()
            self.__checkout = self.__checkout.strip('\n')
            self.__checkin = F.readline()
        with open(MAIN_PATH + stxt, 'r') as S:
            pass
            # self.__surveyUrl = S.readline()
            # self.__surveyUrl = self.__surveyUrl.strip('\n')
            # __surveyxpath 반복문으로 저장하기
        # survey #

    def __loadID(self):
        try:
            with open(MAIN_PATH + self.idtxt, 'r') as F:
                self.__id = F.readline()
                self.__id = self.__id.strip('\n')
                self.__password = F.readline()
        except:
            self.__id = ''
            self.__password = ''

    def receiveID(self, id, pw):
        with open(MAIN_PATH + self.idtxt, 'w') as F:
            F.write(f'{id}\n{pw}')

    def openURL(self, url=LOGIN):
        if url==LOGIN:
            self.driver.get(self.__url)
            self.driver.implicitly_wait(5)
        elif url==SURVEY:
            # open __surveyURL
            # self.driver.implicitly_wait(5)
            pass
        # survey #

    def login(self):
        _id = self.driver.find_element_by_xpath('//*[@id="userId"]')
        _password = self.driver.find_element_by_xpath('//*[@id="userPwd"]')

        _id.send_keys(self.__id)
        _password.send_keys(self.__password)

        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
        self.driver.implicitly_wait(5)
        return True
    
    def checkOut(self):
        self.driver.find_element_by_xpath(self.__checkout).click()

    def checkIn(self):
        self.driver.find_element_by_xpath(self.__checkin).click()

    def survey(self):
        # survey페이지에서 알맞은 설문조사를 선택하는 것부터 만들어야됨
        # self.driver.find_element_by_xpath(self.__surveyXpath[0]).click()
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.driver.implicitly_wait(5)
        pass

    def maximize(self):
        self.driver.maximize_window()

    def thisURL(self): # 지금 이 페이지가 뭔지 알려주는 함수
        pass
    
    def getIDPW(self):
        return self.__id, self.__password
