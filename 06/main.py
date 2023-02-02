1
2
3
4
5
6
7
8
9

3
6
9
12
15

5
6
7
8
9
10

0
1
2
3
4

10
8
6
4
2

i == "I love Python"
for i in range(1, 1000001):
    print(i)
    
number = int(input('숫자를 입력하세요.'))

for i in range(0, number, 1):
    print('I love Python')
    
for x in range(2002, 2054, +4):
    print(x)

while True:
    score = int(input('점수 : '))
    
    if score == -1:
        break
    
    if score >= 60:
        print('합격')
    else :
        print('불합격')
        
for i in range(10):    
    if i == 7:
        break 
    print("The Number is :" , i)
    
for i in range(10):    
    if i == 7:
        continue
    print("The Number is :" , i)

for i in range(8, 10):
        print("The Number is :" , i)
      
n = 200

for i in range(2, n+1):
    is_prime = True
    
    for i in range(1, 200, is_prime):
        if i == 0:
            is_prime = False
    
    if is_prime:
        print(i, end=' ')
