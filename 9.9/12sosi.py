# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    # 'dsn' : '127.0.0.1:1521/xe'
    'dsn' : 'localhost:1521/xe'
}


# conn = oracledb.connect(**config) #오류
# conn = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
# conn = cx_Oracle.connect(**config)
conn = cx_Oracle.connect(**config) 
cursor = conn.cursor()

print("database version: ", conn.version)
print("oracle connect ok success")
print()

# 코드데이터 입력 후 code필드 값 중복체크 / 함수탈출 / 재입력
# 신규등록하기전에 select ~~ 
# 아무거나 코드 1개 

# dcode = int(input('코드 입력>> '))
# cnt = f"select count(code) from sosi where code = {dcode}"
# cursor.execute(cnt)
# rows = cursor.fetchall()
# conn.commit()
# for r in rows:
#     list1 = list(r)
#     print(list1, type(list1))

def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    cnt = f"select count(code) from sosi where code = {dcode}"
    cursor.execute(cnt)
    rows = cursor.fetchall()
    conn.commit()
    for r in rows:
        list1 = list(r)
        if list1[0] == 0:
            break
        elif list1[0] == 1:
            print('error : unique constraint violated')
            print(int(input('코드 입력 >> ')))
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'D')"    
    cursor.execute(msg)
    conn.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)



def sosiSelectAll():
    msg = 'select * from sosi order by code'
    cursor.execute(msg)
    rows = cursor.fetchall()
    print('rows타입 ', type(rows))
    print()

    print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        # print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    time.sleep(1)

def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    pass
    print('code조회후 삭제처리하세요')

def main():
    push = int(input('1.데이터 삽입 2.전체선택 3.제목선택 4.데이터삭제'))
    if push == 1:
        sosiInsert()
    elif push == 2:
        sosiSelectAll()
        time.sleep(0.5)
    elif push == 3:
        sosiSelectTitle()
    elif push == 4:
        sosiDelete()    
        print()

print(main())