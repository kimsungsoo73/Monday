# 02deftuple.py

def my_hap(*args): # 여러개 매개인자를 받을 때 같은 타입에만 가능 
    print('*args타입', type(args))
    hap = 0
    for num in args:
        hap += num
    return hap

data = my_hap(6,9,21,7,3,21,9,1,2,1,3,1,5,45,7,1,23,6,47,7)
print(data)

mylist = [6,9,21,7,3,21,9,1,2,1,3,1,5,45,7,1,23,6,47,7]
mytuple = (6,9,21,7,3,21,9,5,7,1,23,6,47,7)