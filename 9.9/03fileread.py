# 3fileread.py

# 임포트문장 X import file~~~
# pathName = '경로/파일.txt'
# 리턴변수 = open(파일명, 모드w/r/a, 인코딩)
# 리턴변수.close()
# ff=open(1,2,3) 대체 with open(1,2,3) as ff: 
import time


# 파일읽기 처리  read()대신 readline()한라인씩 읽기
pathName = 'C:/Mtest/sample.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
# data = rfile.read()
data = rfile.readline()#한줄씩처리
print(data)
print(pathName,'파일읽기성공했습니다\n')
print('- ' * 50)
rfile.close()


time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
    #권장 my = myfile.read() 전체읽어서 출력 
    my = myfile.readline() #한줄씩처리 
    while my != '':
        print(my, end='')
        my = myfile.readline()
        

print(fileName,'파일읽기성공했습니다')
print()
print()





