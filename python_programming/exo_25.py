#coding:utf-8
"""
 Write a Python program to find the XOR of two given strings interpreted as binary numbers. Go to the editor
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
"""
def test(nums):
    return bin(int(nums[0],2) ^ int(nums[1],2))

print(test(['0001', '1011']))