# HWpickle.py

# open(파일명, wb/rb, 인코딩)
# dump쓰기/load읽기 # 적재

import pickle
import time

fileName = 'C:/Mtest/mydaily.pckl'

while True:
    if num == 1:
        string = input('스케줄을 입력하세요>>> ')
        num = int(input('1. 스케줄기록 2. 스케줄읽기 9. 종료>>> '))
        file = open(fileName, 'ab')
        file_dump = pickle.dump(string,file)
        print(fileName, '저장 완료')
    elif num == 2:
        file = open(fileName, 'rb')
        file_load = pickle.load(file)
        print(fileName, '읽기 완료')
        print(file_load)
    elif num == 9:
        print('스케줄을 종료합니다.')
        break
    else:
        print('작업오류입니다.')

