# 10testlambda.py

# lambda = 익명의 함수 = 함수 이름이 없어요
# lambda는 import가 없음

def mysu(num):
    ret = 3*num +1
    return ret

data = int(input('숫자 입력 >>> '))  
print('일반식', mysu(data))
print('람다식', (lambda num:3*num + 1)(data))
# print('람다식')
# print('일반식', mysu())
