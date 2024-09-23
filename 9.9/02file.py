# 2file.py

# 임포트문장 X import file~~~
# pathName = '경로/파일.txt'
# 리턴변수 = open(파일명, 모드w/r/a, 인코딩)
# 리턴변수.close()
# ff=open(1,2,3) 대체 with open(1,2,3) as ff: 
import time


# 파일읽기 처리 
pathName = 'C:/Mtest/sample.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
data = rfile.read()
# 주석 data = rfile.readline()
print(data)
print(pathName,'파일읽기성공했습니다\n')
print('- ' * 50)
rfile.close()


time.sleep(2)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
    my = myfile.read()
    print(my)
        

print(fileName,'파일읽기성공했습니다')
print()
print()





