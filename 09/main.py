books = ['모모', '어린왕자', '별', '돈키호테', '마당을 나온 암탉']

books.append('일리아드 오디세이')

books.insert(1, '데미안')

del books [3]

books.remove('돈키호테')
-----------------------------------------
family = []
while True:
  name = input('가족 구성원의 이름 : ')
  if family == '끝':
    break
    
  family.append(name)

print(family)
-----------------------------------------
movies = ('보스베이비', '어벤져스')
# 1
movies[0] = '슈퍼배드'
# 2
movies.append('겨울왕국')
# 3
print(movies[2])
# 4
del movies[0]
# 5
print(movies[0])

1,2,3,4번 #튜플은 수정할 수 없음
