# 05ospath.py

# 임포트문장 X import file~~~
# pathName = '경로/파일.txt'
# 리턴변수 = open(파일명, 모드w/r/a, 인코딩)
# 리턴변수.close()
# ff=open(1,2,3) 대체 with open(1,2,3) as ff: 

# 파일읽기 read(), readline(), readlines()
import sys 
import os.path


save_path = os.path.abspath('C:/Mtest/my.txt')
try:
    if not os.path.exists(save_path):
        print(save_path, '대상 파일이 존재하지 않습니다')
        sys.exit()
    else:
        pass
except Exception as EX:
    print('에러이유 확인', EX)





print()


