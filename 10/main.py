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
