# 문제 리스트 1 ~ 10까지 출력
# for, while 반복문 사용금지

# 1.
data = list(range(1,11,1))
print(data)

# print((lambda su: pow(su,2)(6)))
my = list(map(lambda su: pow(su,2),(data)))
print(my)
print(list(my))

# list_1 =[]
# num = 0
# if num % 11 == 