# 07comprehensionlist.py

# lotto = list()
# import random

# for i in range(6):
#     su1 = i**2
#     print(su1, end = '\t')

# for k in range(1,10):
#     su2 = pow(k,2)
#     print(su2, end = '\t')

# mylist = [pow(a,2) for a in range(1,10)]
# mytuple = (pow(b,2) for b in range(1,10))
# myset = {pow(c,2) for c in range(1,10) }

# 문제 1. for반복 ~ if
# 문제 2. comprehension처리

message = ['spam','spam','ham','spam','spam','ham','spam','ham']
item = 'spam'

# 방법 1.
# for i in range(len(message)):
#     if message[i] == item:
#         print(f'{i}번', end = '\t')
#         print(f'{item} = {item.count()}')
#     else:
#         pass

# # 방법 2.
# data = [k for k in message if 'spam' in k]
# print(data)
# 문제 3. spam = 0, ham = 1, dummy


# for i in range(len(message)):
#     if message[i] == item:
#         message[i] = 0
#     else:
#         message[i] = 1
#     print(message)

list = []
for i in message:
    if i == item:
        list.append(0)
    else:
        list.append(1)
print(list)

data = [0 if i == 'spam' else 1 for i in message ]
print(data)