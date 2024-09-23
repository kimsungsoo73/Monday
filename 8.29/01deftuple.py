# 01deftuple.py

# def data_hap(x,y):
#     print('x id', type(x))
#     print('y id', type(y))

# print(data_hap(1,2))


# def h():
#     data_split = data_hap.split(',')
#     print(data_split)
#     for i in range(len(data_split)):
#         pass
        

def my_hap(*args): # 여러개 매개인자를 받을 때 같은 타입에만 가능 
    print('*args타입', type(args))
    hap = 0
    for num in args:
        hap += num
    return hap

data = my_hap(6,9,21,7,3,21)
print(data)
