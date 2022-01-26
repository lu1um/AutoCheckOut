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
        self.__where = str()
        self.__surveyUrl = str()
        self.__surveyXpath = str()
        self.__surveyOutXpath = list()
        self.__surveyInXpath = list()
        self.sleepTime = 0

        self.idtxt = idtxt
        self.driver = Chrome(MAIN_PATH + 'chromedriver.exe')

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

    def receiveID(self, id, pw, wh):
        self.__id = id
        self.__password = pw
        self.__where = wh
        with open(MAIN_PATH + self.idtxt, 'w') as F:
            F.write(f'{id}\n{pw}\n{wh}')

    def openURL(self, url=LOGIN):
        if url==LOGIN:
            self.driver.get(self.__url)
            self.driver.implicitly_wait(5)
            sleep(self.sleepTime)
        elif url==SURVEY:
            self.driver.get(self.__surveyUrl)
            self.driver.implicitly_wait(5)
            sleep(self.sleepTime)

    def login(self):
        _id = self.driver.find_element_by_xpath('//*[@id="userId"]')
        _password = self.driver.find_element_by_xpath('//*[@id="userPwd"]')

        _id.send_keys(self.__id)
        _password.send_keys(self.__password)

        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
        self.driver.implicitly_wait(5)
        sleep(self.sleepTime)
        return True
    
    def checkOut(self):
        self.driver.find_element_by_xpath(self.__checkout).click()
        sleep(1)

    def checkIn(self):
        self.driver.find_element_by_xpath(self.__checkin).click()
        sleep(1)

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