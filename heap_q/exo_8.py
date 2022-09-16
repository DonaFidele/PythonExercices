#coding:utf-8
#Write a Python program to compute maximum product of three numbers of a given array of integers using Heap queue algorithm. 
def maximumProduct(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
arr_nums = [12, 74, 9, 50, 61, 41]
print("Original array elements:")
print(arr_nums)
print("Maximum product of three numbers of the said array:")
print(maximumProduct(arr_nums))