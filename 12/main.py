#1
숫자형
문자형
리스트
문자형
튜플
문자형
숫자형
딕셔너리
숫자형
딕셔너리
튜플
리스트 -> 집합
문자형
숫자형

#2
철수는 13살입니다.
영희는 12살입니다.

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
    
  def get_age(self):
    return self.age
    
  def __str__(self):
      sentence = '{}는 {}살 입니다.'.format(self.name, self.age)
      return sentence
    
a = Person('철수', 13);
b = Person('영희', 12);
 
print(a)
print(b)

#4
import random

class Eevee:
    def __init__(self, name, age, hp):
        self.name = name
        self.age = age
        self.hp = hp
    
    def 이판사판태클(self):
        print('{}의 이판사판태클!'.format(self.name))
        num = random.randint(1, 1000)
        if num <= 750:
            print('효과는 굉장했다!')
        elif 750 < num < 999:
            print('효과는 괜찮았다.')
        else:
            print('효과는 미미했다.') 
    
    def __str__(self):
        sentence = '이름: {}, 나이: {}살, 체력: {}'.format(self.name, self.age, self.hp)
        return sentence


random.randint(100, 1000000)

eevee1 = Eevee('브이1', '3', 1000000)
eevee2 = Eevee('브이2', '3', random.randint(100, 1000000))
eevee3 = Eevee('브이3', '3', random.randint(100, 1000000))
eevee4 = Eevee('브이4', '3', random.randint(100, 1000000))
eevee5 = Eevee('브이5', '3', random.randint(100, 1000000))
eevee6 = Eevee('브이6', '3', random.randint(100, 1000000))
eevee7 = Eevee('브이7', '3', random.randint(100, 1000000))
eevee8 = Eevee('브이8', '3', random.randint(100, 1000000))
eevee9 = Eevee('브이9', '3', random.randint(100, 1000000))
eevee10 = Eevee('브이10', '3', random.randint(100, 1000000))


print(eevee1)
print(eevee2)
print(eevee3)
print(eevee4)
print(eevee5)
print(eevee6)
print(eevee7)
print(eevee8)
print(eevee9)
print(eevee10)
