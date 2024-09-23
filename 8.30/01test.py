# 01test.py

# def gugudan(dan):
#     while True:
#         if data < 0:
#             a = 1000
#             data = dan - a
#             print('잔액 부족')
#             break
#         else:
#             pass
#         return data

# print(gugudan(int(input('숫자 입력 >>> '))))
# print(lambda dan : dan - a)(int(input('숫자 입력 >>> ')))


# def myAdd(x,y):
#     hap = x+y
#     return hap

# print(myAdd(3,5))
# print((lambda x,y : x+y)(3,5))

# my1 = lambda x,y : x+y
# print(my1)


# def odd(num):
#     if num % 2 == 0:
#         print('짝수')
#     else:
#         print('홀수')
# print(odd(int(input('숫자'))))


print((lambda num : '짝수' if num % 2 == 0 else '홀수')(7))