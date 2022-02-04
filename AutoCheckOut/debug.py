#!/usr/bin/env python

from time import sleep, localtime

import login

URL_TEXT_DIRECTORY = 'URL.txt'
ID_TEXT_DIRECTORY = 'PASSWORD.txt'
SURVEY_TEXT_DIRECTORY = 'SURVEY.txt'

def main():
    s = '220207(월)_오전 건강현황 조사_7기'
    year = str(localtime().tm_year)[2:]
    month = str(localtime().tm_mon)
    day = str(localtime().tm_mday)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    date = year + month + day
    print(date in s)

    xpathText()


def xpathText():
    aco = login.AutoCheckOut(URL_TEXT_DIRECTORY, ID_TEXT_DIRECTORY, SURVEY_TEXT_DIRECTORY)
    aco.maximize()
    aco.openURL()
    aco.login()
    aco.openURL(login.SURVEY)
    txt = aco.driver.find_element_by_xpath('//*[@id="wrap"]/form/div/div[2]/div/div/ul/li[10]/div/div[1]/dfn').text[:6]
    intTxt = int(txt)
    print(intTxt, type(intTxt))
    sleep(5)


if __name__ == '__main__':
    main()
