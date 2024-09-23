import re

url = 'www.google.com'

print(url.split('.'))

ct = ' '
print(ct.join(url))

msg = 'my best% 2400 Flu_it is blue%#357cherry'

print(re.findall('%', msg))
print(re.findall('[a-zA-Z]{3,7}', msg))
print(re.findall('[a-zA-Z0-9]{3,7}', msg))

my = re.findall('[a-zA-Z]{7,10}', msg)
if my:
    print(my)
else:
    print(('없어'))