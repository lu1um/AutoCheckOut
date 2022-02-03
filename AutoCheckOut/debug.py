#!/usr/bin/env python

from time import sleep

import login

URL_TEXT_DIRECTORY = 'URL.txt'
ID_TEXT_DIRECTORY = 'PASSWORD.txt'
SURVEY_TEXT_DIRECTORY = 'SURVEY.txt'

def main():
    aco = login.AutoCheckOut(URL_TEXT_DIRECTORY, ID_TEXT_DIRECTORY, SURVEY_TEXT_DIRECTORY)
    aco.maximize()
    aco.openURL()
    sleep(5)

if __name__ == '__main__':
    main()

# 맨 밑 설문조사 이름 - 220127(목)_오후 건강현황 조사_7기
# //*[@id="wrap"]/form/div/div[2]/div/div/ul/li[10]/div/div[1]/dfn