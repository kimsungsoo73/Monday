import re

url = 'www.google.com'

phone = '010-1234-1234 빅이썬'
# re.sub('1패턴','2변경, 적용', phone)

model = re.sub( '-[0-9]{4}-','-****-', phone)
print(model) # 010-****-1234, phone


