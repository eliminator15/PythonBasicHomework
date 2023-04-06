#1
while True:
  try:
    string = input('숫자를 입력하세요.')
  
    number = int(string)
  
    print(number + 10)
  except:
    print( '숫자를 입력해주세요.' )

#2
정상적으로 종료되었습니다.

#3
-함수 블록 또는 클래스 블록 내부에서 변수를 만들어야 한다.
-블록 밖에서 변수를 만들어야 한다.

#4
함수 실행 전 var1: 전역변수 1 - 전역변수의 영향
함수 실행 전 var2: 전역변수 2 - 전역변수의 영향
함수 안 var1: global 명령어의 역할
함수 안 var2: 로컬변수
함수 실행 후 var1: global 명령어의 역할 - global var1의 영향
함수 실행 후 var2: 전역변수 2 - 전역변수의 영향
  
#5
전역변수  [ scope() 함수 실행 전 출력 ]
함수 내 지역변수  [ scope() 함수에서 출력 ]
함수 내 지역변수  [ if문에서 출력 ]
for 지역변수  [ for문에서 출력 ]
for 지역변수  [ for문에서 출력 ]
for 지역변수  [ for문에서 출력 ]
전역변수  [ scope() 함수 밖에서 출력 ]


