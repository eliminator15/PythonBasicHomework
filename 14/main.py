f = open('pokemonModule.py', 'w', encoding = 'UTF-8')

import random

class Pokemon:
  def __init__(self, name, gender, age, hp):
    self.name = name
    self.gender = gender
    self.age = age
    self.hp = hp

  def cry(self):
    print('낑')

  def walk(self):
    print('포켓몬이 걷는다.')

class Pikachu(Pokemon):
    def __init__(self, name, gender, age, hp):
        super().__init__(name, gender, age, hp)
    
    def 볼트태클(self):
        print('{}의 볼트태클!'.format(self.name))
        num = random.randint(1, 1000)
        if num <= 750:
            print('효과는 굉장했다!')
        elif 750 < num < 999:
            print('효과는 괜찮았다.')
        else:
            print('효과는 미미했다.')

  
    def __str__(self):
        sentence = '이름: {}, 성별: {}, 나이: {}, 체력: {}'.format(self.name, self.gender, self.age, self.hp)
        return sentence

class Eevee(Pokemon):
    
    def __init__(self, name, gender, age, hp):
        super().__init__(name, gender, age, hp)
    
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
        sentence = '이름: {}, 성별: {}, 나이: {}살, 체력: {}'.format(self.name, self.gender, self.age, self.hp)
        return sentence

import main.py
pikachu1 = new Pikachu('용선생', '남', 37, 100000000)
pikachu2 = new Pikachu('나선애', '여', 13, 95000000)

#2
새파일.txt에 
1번째 줄입니다.
2번째 줄입니다.
etc
등이 저장된다.

#3
-1. 안녕하세요가 저장됨.
-2. 읽을 수 있음
-3. 안녕하세요가 추가됨.
-2. 
