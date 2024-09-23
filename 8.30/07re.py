import re

url = 'www.google.com'

print(url.split('.'))

ct = ' '
print(ct.join(url))

msg = 'my best blue apple my java mypython cherry'

# print(re.findall('%', msg)) ['%', '%']
# print(re.findall('[a-zA-Z]{3,7}', msg)) ['best', 'Flu', 'blue', 'cherry']
# print(re.findall('[a-zA-Z0-9]{3,7}', msg))  ['best', '2400', 'Flu', 'blue', '357cher']    

x = re.findall('red',msg)
print(x) # 만약 없으면 []표시

# 원래내용을 덮어씌우는 재할당
msg = 'my best blue apple my java mypython cherry 2400 %#$!$^&!'

ret1 = re.findall('[\w]', msg)
ret2 = re.findall('[\W]', msg)
ret3 = re.findall('[a-zA-Z0-9가-힣]', msg)
print(ret1)
print(ret2)
print(ret3)