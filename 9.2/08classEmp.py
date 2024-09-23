# 08classEmp.py
# 파이썬에서 클래스 이름만 명서
# 클래스 안에 있는 메소드매개인자(self)
# 클래스 안에 있는 메소드호출 ob = 클래스

class Emp:
    user_pwd = '1111'
    user_id = '아이디'
    def __init__(self, id, pwd):
        self.user_id = id
        self.user_pwd = pwd

    def insert(self, nick, age):
        print('아이디', self.user_id)
        print('비밀번호', self.user_pwd)
        print('insert into처리\n')
        print('전달된 이름', nick)
        print('전달된 나이', age)
        
    def delete(self):
        print('삭제')
        print('딕트 삭제, delete where처리')



ob = Emp('sky','7789')
ob.insert('홍길동',7)
ob.delete()


print()
print('9월 2일 월요일 123')
print('9월 2일 월요일 456')
print('9월 2일 월요일 789')