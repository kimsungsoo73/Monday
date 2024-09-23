# pip install pymysql
import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    # 'dsn' : '127.0.0.1:1521/xe'
    'database' : 'naver',
    'port' : 3306
}

conn = pymysql.connect(**config) 
cursor = conn.cursor()

def GoodsInsert():
    dcode = int(input('코드 입력 >> '))
    dname = input('이름 입력 >> ')
    dsu = int(input('숫자 입력 >> '))
    ddan = int(input('단 입력 >> '))
    cnt = f"insert into goods values({dcode},'{dname}', {dsu}, {ddan},now())"
    cursor.execute(cnt)
    conn.commit()
    print(dcode, '등록 성공')

def GoodSelectAll():
    dcode = int(input('코드 입력 >> '))
    cnt = f"select * from goods where code = {dcode}"
    cursor.execute(cnt)
    rows = cursor.fetchall()
    conn.commit()
    print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
    for r in rows:
        print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))

def GoodsUpdate():
    while True:
        num1 = int(input('1.이름 수정 2.숫자 수정 3.단 수정 4.종료'))
        if num1 == 1:
            dcode = int(input('코드 입력 >> '))
            dname = input('이름 입력 >> ')
            cnt = f"update goods set name = '{dname}' where code = {dcode}"
            cursor.execute(cnt)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))
        elif num1 == 2:    
            dcode = int(input('코드 입력 >> '))
            dsu = int(input('숫자 입력 >> '))
            cnt1 = f"update goods set su = {dsu} where code = {dcode}"
            cursor.execute(cnt1)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))
        elif num1 == 3:
            dcode = int(input('코드 입력 >> '))
            ddan = int(input('단 입력 >> '))
            cnt2 = f"update goods set dan = {ddan} where code = {dcode}"
            cursor.execute(cnt2)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))
        elif num1 == 4:
            break

def GoodsDelete():
    while True:
        num2 = int(input('1.코드 삭제 2.이름 삭제 3.숫자 삭제 4.단 삭제 5.종료'))
        if num2 == 1:
            dcode = int(input('코드 입력 >> '))
            cnt = f"delete from goods where code = {dcode}"
            cursor.execute(cnt)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))
        elif num2 == 2:
            dname = input('이름 입력 >> ')
            cnt1 = f"delete from goods where name = '{dname}'"
            cursor.execute(cnt1)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))    
        elif num2 == 3:
            dsu = int(input('숫자 입력 >> '))
            cnt2 = f"delete from goods where su = {dsu};"
            cursor.execute(cnt2)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3]))  
        elif num2 == 4:
            ddan = int(input('단 입력 >> '))
            cnt3 = f"delete from goods where dan = {ddan}"
            cursor.execute(cnt3)
            rows = cursor.fetchall()
            print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
            for r in rows:
                print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3])) 
        elif num2 == 5:
            break

def GoodsSearchName():
    dname = input('찾고 싶은 단어 입력 >> ')
    cnt = f"select * from goods where name like '%{dname}%'"
    cursor.execute(cnt)
    rows = cursor.fetchall()
    print('%s\t %s\t %s\t %s\t' %('dcode', 'dname', 'dsu', 'ddan'))
    for r in rows:
        print('%s\t %s\t %s\t %s\t' %(r[0],r[1],r[2],r[3])) 

def main():
    while True:
        num = int(input('1.입력 2.전체출력 3.수정 4.삭제 5.조회 9.종료'))
        if num == 1:
            print(GoodsInsert())
        elif num == 2:
            print(GoodSelectAll())
        elif num == 3:
            print(GoodsUpdate())
        elif num == 4:
            print(GoodsDelete())
        elif num == 5:
            print(GoodsSearchName())
        elif num == 9:
            break
print(main())