# 1file.py

# return = open(파일명, 모드w/r/a, encoding = '')
# w는 덮어쓰기, a는 입력한 내용 모두 출력, 
# 임포트문장 없어요
# 리턴변수.close()
pathname = 'C:/Mtest/sample.txt'
rfile = open(pathname,'r', encoding = 'UTF-8')
data = rfile.read()
print(data)
# data = rfile.readline()
# print(data)
rfile.close()
print(pathname, '파일 읽기 성공!')



pathName1 = 'C:/Mtest/kakao.txt'
with open(pathName1,'r', encoding = 'UTF-8') as myfile:
    my = myfile.read()
    print(my)
