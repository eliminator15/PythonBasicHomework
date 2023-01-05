a,b
true
false
false 
true
true
false
true
true
true
false
true
true
true
코딩
1
3
5
user = int(input(""))
if user % 2 == 0:
    print("짝수")
else:
    print("홀수")

num1 = int(input("input number1: "))
num2 = int(input("input number2: "))
num3 = int(input("input number3: "))
big = 0

if num1 > num2 and num1 > num3:
  big = num1
  print(num1)
elif num2 > num1 and num2 > num3:
  big = num2
  print(num2)
elif num3 > num1 and num3 > num2:
  big = num3
  print(num3)
