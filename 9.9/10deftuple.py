# 10deftuple.py

def two_hap(args):  #리스트데이터 받기
    hap = 0  
    for su in args:
        hap = hap + su
    return hap
 
mylist = [5,3,1,4,6] 
msg = two_hap(mylist) 
print('리스트합계 ' , msg)






# def mycal(x,y,z,l,m,n):
#     hap = x+y+z+l+m+n
#     return hap


# 잠시 비교
# a,b,c,d,e,f =  1,2,3,4,5,6
# ret = mycal(a,b,c,d,e,f)
# print('ret결과' , ret)
  
# 첫번째 *args매개인자 msg = first_hap(1,2,3,4,5)
print()