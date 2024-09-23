# !pip install pymysql
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

print("MySQL connect ok success")
print()

def CodeInsert():
    dcode = int(input('코드 입력 >> '))
    dname = input('이름 입력 >> ')
    dhit = int(input('조회 입력 >> '))
    cnt = f"insert into test values({dcode},'{dname}', {dhit}, now())"
    cursor.execute(cnt)
    conn.commit()
    print(dcode, '등록 성공')

def CodeCheck():
    dcode = int(input('코드 입력>> '))
    cnt = f"select * from test where code = {dcode}"
    cursor.execute(cnt)
    rows = cursor.fetchall()
    # cnt1 = f"select count(*) from test where code = {dcode}"
    # cursor.execute(cnt1)
    # rows1 = cursor.fetchall()
    # print(rows1)
    # print(type(rows))
    conn.commit()
    
    print('%s\t %s\t %s\t' %('code','name','hit') )
    for r in rows:
        print(r[0],r[1],r[2])



def CodeAllSelect():
    dcode = int(input('코드입력>> '))
    cnt = f"delete from test where code = {dcode}"
    cursor.execute(cnt)
    rows = cursor.fetchall()
    conn.commit()
    # for r in rows:
    #     if r[0].get(dcode) == None:
    #         print(dcode)
    #     else:
    #         print()
    print('%s\t %s\t %s\t' %('code','name','hit') )
    for r in rows:
        print(r[0],r[1],r[2])

def main():
    dcode = int(input('1.신규 등록 2.조회 3.삭제 4. 종료'))
    while True :
        if dcode == 1:
            CodeInsert()
            CodeAllSelect()
        elif dcode == 2:
            CodeCheck()
            CodeAllSelect()
        elif dcode == 3:
            pass
        elif dcode == 4:
            print('종료합니다.')
print(main())

# web 웹태그 + css = 방명록, 게시판, 인스타 가능
# web 웹태그 code, name, title, 조회수, 날짜, 이미지
# 댓글 
# 로그인처리 userid, password

