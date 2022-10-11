#coding:utf-8
"""Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21"""

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))