# 버블 
a = [4,7,5,1,2]
# for i in range(0,4):
#     for j in range(i,5):
#         if a[i]>a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
#     print(a)


# 이진
for i in range(0,4):
    for j in range(i,5):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    print(a)