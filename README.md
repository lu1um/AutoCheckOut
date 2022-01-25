# AutoCheckOut by python

** 참고 문헌 **
1. https://sir.kr/so_python/273
2. https://pythondocs.net/selenium/셀레니움-wait-개념-이해하기-implicitly-wait-vs-explicitly-wait/
3. https://hwan001.tistory.com/119

## to-do list
- survey만들기
- 출석하기 xpath 알기 (지금은 임의로 checkin으로 해놓음)

### 01.18
같은 폴더내의 URL.txt, PASSWORD.txt를 만들고, 클릭하기 원하는 URL, XPath, ID, 비번을 저장해놓았다.\n

문제점 : Path.cwd()는 현재 터미널의 작업공간 주소를 불러온다..
 -> __file__ 객체를 사용함으로 해결\n

로그인까지 했고, 이제 클릭만 해보자!

### 01.24 
#### v0.1.1
출첵은 다 했고, survey 남음\n
xpath.txt에 매일 설문조사 xpath가 어떻게 바뀌는지 확인해보고 규칙찾기\n
login.py에서 survey xpath를 불러와서 리스트로 정리한다음 사용하기\n

### 01.25 
#### v0.1.2
출석, 퇴실 구현\n
출석 xpath는 확실하지않음\n
login만 하는법 구현\n

#### v0.1.3
schedule 라이브러리 제거\n