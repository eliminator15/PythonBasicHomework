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
리스트
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
