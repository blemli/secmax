from secmax import secmax

#select the algorithm to test:

def test_all_same():
	l=[2,2,2,2,2,2]
	assert secmax(l) == None

def test_two_digits():
	l=[1,2,3,1,2,3]
	assert secmax(l) == 2
	l=[1,2,1,2,1,2]
	assert secmax(l) == 1

def test_one_element():
	l=[1]
	assert secmax(l) == None

def test_empty_list():
	l=[]
	assert secmax(l) == None

def test_descending():
	l=[3,2,1]
	assert secmax(l) == 2
	l=[3,2,1,3,1,1,1,2]
	assert secmax(l) == 2

def test_negative():
	l=[-1,-2,-3]
	assert secmax(l) == -2
	
