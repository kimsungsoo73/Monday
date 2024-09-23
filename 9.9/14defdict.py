# 14defdict.py
import os
import pandas as pd
import cx_Oracle  

def test(**my):
    print('test함수(my)')
    print('my타입', type(my))



test(code=2400, title='summer', grade='A')
# 첫번째 함수이름 test(매개인자)
# 두번째 test('code'=2400, 'title'='summer', 'grade'='A')
# 세번째 test함수에서  코드 : 2400 제목 : summer  등급 :A
# 세번째 test함수에서  code : 2400 title : summer  grade : A

# 파이썬 함수이름(*매개인자): 
# 파이썬 함수이름(**매개인자):  