

class Pikachu:
    def __init__(self, 이름, 성별, 체력):
        self.이름 = 이름
        self.성별 = 성별
        self.체력 = 체력
    
    def 백만볼트(self):
        print('{}의 백만볼트!'.format(self.이름))
        num = random.randint(1, 1000)
        if num <= 750:
            print('효과는 굉장했다!')
        elif 750 < num < 999:
            print('효과는 괜찮았다.')
        else:
            print('효과는 미미했다.')
    
    def __str__(self):
        sentence = '이름: {}, 성별: {}, 체력: {}'.format(self.이름, self.성별, self.체력)
        return sentence

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
