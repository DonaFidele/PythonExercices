#coding:utf-8
"""Write a Python program to find the occurrences of 10 most common words in a given text. Go to the editor
Sample Output:
[('Python', 6), ('the', 6), ('and', 5), ('We', 2), ('with', 2), ('The', 1), ('Software', 1), ('Foundation', 1), ('PSF', 1), ('is', 1)]"""

from collections import Counter
text="""The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""
a=Counter(text.split()).most_common(10)
print(a)