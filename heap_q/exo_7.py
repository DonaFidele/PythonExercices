#Write a Python program to find the kth (1 <= k <= array's length) largest element in an unsorted array using Heap queue algorithm
import heapq,array
def test(array,n):
    return heapq.nlargest(n,array)[-1]

print(test([1, 63, 5, 38, 7, 1, 9, -3],3))