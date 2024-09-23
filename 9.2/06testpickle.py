# 06testpickle.py

# open(파일명, wb/rb, 인코딩)
# dump쓰기/load읽기 # 적재
# 피클로 파일처리

import pickle
import time

fileName = 'C:/Mtest/music.pckl'
mybest = {'발라드ballad' : 4.9, '팝송popsong' : 4.7, 'R&B' : 3.8}
file = open(fileName, 'wb')
pickle.dump(mybest, open(fileName, 'wb'))
print(fileName, '피클 저장 성공!')
print()
time.sleep(1)


data = pickle.load(open(fileName, 'rb'))
print(data)


mybest1 = {}
