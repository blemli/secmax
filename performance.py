#!/usr/bin/env python3

import random
import timeit
from icecream import ic
from secmax import secmax,secmax_col,secmax_oneline

mylist = []
for i in range(100000):
    mylist.append(random.randint(-100000,100000))

smalllist = []
for i in range(200):
    smalllist.append(random.randint(-100000,100000))



time_secmax = timeit.timeit(stmt="secmax([random.randint(-10000,10000) for x in range(200)])", globals=globals(), number=1000)
time_secmax_col= timeit.timeit(stmt="secmax_col([random.randint(-10000,10000) for x in range(200)])", globals=globals(), number=1000)
time_secmax_oneline= timeit.timeit(stmt="secmax_oneline([random.randint(-10000,10000) for x in range(200)])", globals=globals(), number=1000)
#time_secmax = timeit.timeit(stmt="secmax.secmax(smalllist)", globals=globals(), number=10000)
#time_secmax_col = timeit.timeit(stmt="secmax.secmax_col(smalllist)", globals=globals(), number=10000)
ic(time_secmax)
ic(time_secmax_col)
ic(time_secmax_oneline)
