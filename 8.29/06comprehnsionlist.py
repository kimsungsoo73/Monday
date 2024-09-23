# 06comprehensionlist.py

lotto = list()
import random

for i in range(6):
    su1 = i**2
    print(su1, end = '\t')

for k in range(1,10):
    su2 = pow(k,2)
    print(su2, end = '\t')

mylist = [pow(a,2) for a in range(1,10)]
mytuple = (pow(b,2) for b in range(1,10))
myset = {pow(c,2) for c in range(1,10) }

