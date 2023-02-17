#!/usr/bin/env python3

import random
import profiling

#initial 
@profiling.profile 
def secmax_optimized(l):
	max=float('-inf')
	secmax=max
	for item in l:
		if item > secmax:
			if item < max:
				secmax=item
			elif item > max:
				secmax=max
				max=item
	if secmax == float('-inf'): secmax=None
	return secmax

# using collections
def secmax_collections(l):
	unique=list(set(l))
	unique.sort()
	return ([None]*2 + unique)[-2] 

# slow and ugly, but only one line
def secmax_oneline(l):
	return max([i for i in l if i<max(l)] or [None]) 

secmax=secmax_optimized



if __name__ == "__main__":
	mylist = []
	for i in range(1000000):
		mylist.append(random.randint(-1000,1000))
	secmax(mylist)
	profiling.print_stats()
