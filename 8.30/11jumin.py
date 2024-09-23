import re

jumin = '981024-1674938'

gender = re.search('(-)(\d{1})', jumin)
print(gender)

genderNum = int(gender.group(2))
print(genderNum)
if genderNum == 1 or genderNum == 3:
    print('남자')
elif genderNum == 2 or genderNum == 4:
    print('여자')