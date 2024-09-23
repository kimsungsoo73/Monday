import re

data = '''
kim 840916-1094852
lee 921207-2059326
goo 981024-1674938
'''
# 문자열함수 for ~~ if ~ data[시작위치]
# 정규식 re.sub( '[0-9]{4}-', '-****-', phone)

# compile('\d{6}-\d{7}')
# print(data[12:19])

# for i in range(3):
#     a = 19 + 19*i
#     data1 = data.replace(data[(a-6):a], '*******')
#     print(data1)

pattern = re.compile('-\d+')
first = pattern.sub('-*******', data)
print(first)

two = re.sub('[0-9]{7}','*******',data)
print(two)




# 정규식 compile(), sub(1,2,3), 다른 방법
# kim 840916-1******
# lee 921207-2******
# goo 981024-1******





