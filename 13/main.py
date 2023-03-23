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


