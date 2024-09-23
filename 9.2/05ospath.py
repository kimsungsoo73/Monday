# 05ospath.py
import time
import sys
import os.path

file = 'C:/Mtest/kakao.txt'
save_path = os.path.abspath('C:/Mtest/my.txt')
try:
    if not os.path.exists(save_path):
        print(save_path, '대상 파일이 존재하지 않다.')
        sys.exit()
    else:
        pass 
except Exception as EX:
    print('에러확인 이유', EX)

print()