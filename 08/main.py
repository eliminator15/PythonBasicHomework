import random
count = 0 # 이긴 횟수

while True:
  print('-------------------------------------------')
  if player == (1):
    player = '가위'  
  elif player == (2):
    player = '바위'
  elif player == (3):
    player = '보'
if player == '그만':
        break
       
  com = random.randint(1, 3):
  if com == 1:
     com = '가위'
  elif com == 2:
     com = '바위'
  elif com == 3:
     com = '보'

  print('사용자 ( {} vs {} ) 컴퓨터'.format(player, com))

  if player == '가위' or player == '보' or player == '바위' :
        if (com == '가위' and player == '보') or (com == '바위' and player == '가위') or (com == '보' and player == '바위'):
            print('컴퓨터 승')
        elif if (player == '가위' and com == '보') or (player == '바위' and com == '가위') or (player == '보' and com == '바위'): 
            print('플레이어 승')
            count += 1  # count = count + 1 코드와 동일
            if @@@ :
                print("player 3승으로 종료합니다.")
                break
        else:
            print('비겼습니다.')                  
  else:
      print("잘못 입력했습니다.")
      continue
