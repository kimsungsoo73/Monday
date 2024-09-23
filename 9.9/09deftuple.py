# 09deftuple.py

def data_hap(x,y,z,a,b,c):
    hap = 0
    hap = x+y+z+a+b+c
    return hap


def my_hap(*args):
    print('*args타입', type(args)) #'tuple'
    hap = 0 
    for num in args:
        hap = hap + num
    return hap 


data = my_hap(6,11,24,7,3,21) 
print('데이터 결과 ', data)
print('데이터 결과 ', my_hap(6,11,24,7,3,21))
print()
print('- ' * 50)


total = data_hap(6,11,24,7,3,21)  
print('계산처리 합계 ', total)
print('계산처리 합계 ', data_hap(6,11,24,7,3,21))














print()
