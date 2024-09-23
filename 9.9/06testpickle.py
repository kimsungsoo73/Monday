# 06testpickle.py

# open(1파일명, 모드wb/rb, 인코딩)
# dump쓰기/load읽기
# 피클로 파일처리 import

import pickle
import time

fileName = 'C:/Mtest/movie.pckl'
mybest = {'슈퍼super':9.2, '아이iron':7.4, '손흥민':5.3}

pickle.dump(mybest, open(fileName, 'wb'))
print(fileName, ' 피클저장 성공했습니다')
print('-' * 60)
print()


time.sleep(1)
data = pickle.load(open(fileName, 'rb'))
print(data)
print(fileName, ' 피클읽기 성공했습니다')
print()




