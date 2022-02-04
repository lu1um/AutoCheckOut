# AutoCheckOut by python

Github : https://github.com/lu1um/AutoCheckOut.git

** 참고 문헌 **
1. https://sir.kr/so_python/273
2. https://pythondocs.net/selenium/셀레니움-wait-개념-이해하기-implicitly-wait-vs-explicitly-wait/
3. https://hwan001.tistory.com/119

사용법은 폴더내의 설명서.txt 참고  

<details>
  <summary>패치노트</summary>
  
  <div markdown="1">  

### 01.18
같은 폴더내의 URL.txt, PASSWORD.txt를 만들고, 클릭하기 원하는 URL, XPath, ID, 비번을 저장해놓았다     

문제점 : Path.cwd()는 현재 터미널의 작업공간 주소를 불러온다..  
 -> __file__ 객체를 사용함으로 해결


### 01.24 
#### v0.1.1
출첵기능 완료  
xpath.txt에 매일 설문조사 xpath가 어떻게 바뀌는지 확인해보고 규칙찾기  
login.py에서 survey xpath를 불러와서 리스트로 정리한다음 사용하기 


### 01.25 
#### v0.1.2
출석, 퇴실 구현  
출석 xpath는 확실하지않음  
login만 하는법 구현

#### v0.1.3
schedule 라이브러리 제거  

#### v0.1.4
TIL repo와 분리.  
switch_window구문 추가, 이제 survey xpath를 얻는일만 남았다

#### v0.1.5
survey 약간 추가, test필요  


### 01.26
#### v0.1.6
test필요 저녁테스트해보기!  

#### v0.1.7
설문조사 문항 불러오기 실패하는 오류수정

#### v0.1.8
reboot chrome버튼 및 기능 생성   

#### v0.2.0
출석시간이 넘었을 때 실행안되도록 하는 기능 추가  
슬로우모드 추가 예정

#### v0.2.1
슬로우모드 추가  
설명서, 설명사진 추가  
실제 테스트 필요  

#### v0.2.2
login.py의 오타 수정  
저녁 테스트결과 잘됨  


### 02.04
debug.py추가, 설문조사가 2페이지에 있을 경우 고려  
#### v0.2.3
debug를 위해 login.py 코드 수정  
2페이지에 해당 설문조사가 있을 떄 & 탐색속도 향상 코드 추가, 미완성
  </div>
</details>