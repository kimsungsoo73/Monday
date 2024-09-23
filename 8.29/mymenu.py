# 09dictmenu.py
# 예외처리 try: ~~ except: ~ 일단 생략
import time
import sys # 프로그램 종료 sys.exit()

menu = dict()
flag = True
num, su, sel = 0,0,0
msg, info, message = '','',''

def menuAddition():
    name = input('이름입력 >>> ')
    price = input('가격입력 >>> ')
    menu[name] = price
    print(name, '등록 성공!')

def menuPrint():
    for i,v in menu.items():
        print(i,':',v)

def menuAdvise():
    name = input('수정 이름입력 >>> ')
    price = input('수정 가격입력 >>> ')
    if menu.get(name) == None:
        print('편집대상 X')
    else:
        price = input('수정 가격입력 >>>')
        menu[name] = price
        print(name, '수정 성공!')

def menuDel():
    name = input('삭제 이름입력 >>> ')
    if menu.get(name) == None:
        print('편집대상 X')
    else:
        menu.pop(name)
        print(name, '삭제 성공!')

def menuCheck():
    msg = input('메뉴를 조회해보세요 >>> ')
    if menu.get(msg) == None:
        print('조회하신 내용이 없습니다.')
    else:
        print(f'{msg} :', menu.get(msg))
        print(msg, '조회 성공!')

def menuFinish():
    print('딕트처리를 종료합니다')
    flag = False

# ---------------------------------------------------------------------------------------------------------------
while flag:
    pass
    num = int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료 >>>'))
    if num == 9:
        menuFinish()
    elif num == 1:
        menuAddition()
    elif num == 2:
        menuPrint()
    elif num == 3:
        menuAdvise()
    elif num == 4:
        menuDel()
    elif num == 5:
        menuCheck()
    else:
        print('처리번호를 다시 입력하세요\n')


