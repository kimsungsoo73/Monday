# 07testcopy.py

import math
import random
import re
import os.path
import sys
import time
import pickle
import datetime

import copy
apple = 'MS midro soft'
my = apple
print(my)

data = [ 11, 22, 33 ]
mydb = copy.deepcopy(data)
data[0] = 789
print(data)
print(mydb)


