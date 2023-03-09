# 1
scores = [0] * 5

for i in range(5):
    scores[i] = int(input('{}번 학생의 성적 입력: '.format(i+1)))

print('--- 입력된 값 ---')

for i in range(5):
    print('{}번 학생의 성적: {}'.format(i+1, score))
    
   @@@
        print('{}번 학생 불합격'.format(i+1))  

# 2

scores = [0] * 5

for i in range(5):
    scores[i] = int(input('{}번 학생의 성적을 입력하세요: '.format(i+1)))

for i in range(5):
    if scores[i] >= 60:
        print('{}번 학생 합격'.format(i+1))
    else:
        print('{}번 학생 불합격'.format(i+1)) 

        total = 0 # 총합

scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
for score in scores:
    @@@@@@@@@@@@@@@
    
print(total) # 481

price_list = [1000, 2300, 9900, 15000]
for price in price_list:
    sale_price = price*1.1
    print("{}원의 결제 금액은 {}원 입니다.".format(price, sale_price))
    
import random

foods = ['짬뽕', '자장면', '탕수육']

title = '''1. 메뉴 추가
2. 메뉴 삭제
3. 메뉴 출력
4. 메뉴 추천
5. 종료'''

while True:
    print(title)
    command = input('어떤 작업을 하시겠습니까?')
    if command == '1':
        food = input('추가할 메뉴 : ')
        foods.append(food)
    elif command == '2':
        food = input('삭제할 메뉴 : ')
        foods.remove(food)
    elif command == '3':
        print('='*100)
        print(food) # 음식 출력
        print('='*100)
    elif command == '4':
        pick = random.choice(foods)
        print(pick)
    elif command == '5':
        break
        
