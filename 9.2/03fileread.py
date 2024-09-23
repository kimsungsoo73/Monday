# 1file.py
import time
# return = open(파일명, 모드w/r/a, encoding = '')
# w는 덮어쓰기, a는 입력한 내용 모두 출력, 
# 임포트문장 없어요
# 리턴변수.close()
pathname = 'C:/Mtest/sample.txt'
rfile = open(pathname,'r', encoding = 'UTF-8')
data = rfile.readline() # 한줄씩 처리
# data = rfile.read()
print(data)
rfile.close()
print(pathname, '파일 읽기 성공!')
time.sleep(1)


pathName1 = 'C:/Mtest/kakao.txt'
with open(pathName1,'r', encoding = 'UTF-8') as myfile:
    # my = myfile.read() 전체읽어서 출력
    my = myfile.readline()
    while my != '':
        print(my)
        my = myfile.readline()
