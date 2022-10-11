#coding:utf-8
"""
Write a Python program to find the substrings within a string.

Sample text :

'Python exercises, PHP exercises, C# exercises'

Pattern :

'exercises'

Note: There are two instances of exercises in the input string.
"""
from collections import Counter
import re
regex=re.compile("exercises")
result=regex.findall('Python exercises, PHP exercises, C# exercises')
print(Counter(result))
