# 08classEmp.py

class Emp:
    user_id = '아이디'
    user_pwd = '비번번' 

    def __init__(self,id,pwd):
        user_id = id
        user_pwd = pwd  
        

    def insert(self, age):
        print('\n전역변수 user_id = ', self.user_id)
        print('전역변수 user_pwd = ', self.user_pwd)
        print('전달된 나이 ', age)
        print('insert into처리\n')


    def delete(self):
        print('삭제처리')
        print('딕트del, delete where 조건')
        

ob = Emp('wed', '1234')
ob.insert(23)
ob.delete()
      






