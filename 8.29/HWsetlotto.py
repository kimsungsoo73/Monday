# HWsetlotto.py

# set항목함수 추가 add()
# list로 변환 금지
# 난수로 로또숫자발생, 중복체크, set추가
# 출력은 오름차순적용 

import random
lotto = set()
num = random.randint(1,45)

while (len(lotto) < 6):
    num = random.randint(1,45)
    if num not in lotto:
        lotto.add(num)
print(sorted(lotto))






