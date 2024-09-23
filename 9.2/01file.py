# 1file.py

# return = open(파일명, 모드w/r/a, encoding = '')
# w는 덮어쓰기, a는 입력한 내용 모두 출력, 
# 임포트문장 없어요
# 리턴변수.close()

wfile = open('C:/Mtest/sample.txt','a', encoding = 'UTF-8')
name = input('이름 입력 >>> ')
age = input('나이 입력 >>> ')
address = input('주소 입력 >>> ')

wfile.write(name + '\n')
wfile.write(age + '\n')
wfile.write(address + '\n')
wfile.close()

pathName1 = 'C:/Mtest/sample2.txt'
with open(pathName1,'a', encoding = 'UTF-8') as myfile:
    name = input('이름 입력 >>> ')
    age = input('나이 입력 >>> ')
    address = input('주소 입력 >>> ')

    myfile.write(name + '\n')
    myfile.write(age + '\n')
    myfile.write(address + '\n')