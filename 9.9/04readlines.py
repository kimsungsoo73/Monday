# 04readlines.py

# 임포트문장 X import file~~~
# pathName = '경로/파일.txt'
# 리턴변수 = open(파일명, 모드w/r/a, 인코딩)
# 리턴변수.close()
# ff=open(1,2,3) 대체 with open(1,2,3) as ff: 

# 파일읽기 read(), readline(), readlines()

file = 'C:/Mtest/kakao.txt'
with open(file,'r',encoding='UTF-8') as myfile:
    for data in myfile.readlines():
        print(data, end='')
        
        


print(file,'파일읽기성공했습니다')
print()






