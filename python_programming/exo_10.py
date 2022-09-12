#coding:utf-8
"""Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace. Go to the editor
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())'
"""
def test(combined):
   ls = []
   s2 = ""
   for s in combined.replace(' ', ''):
       s2 += s
       if s2.count("(") == s2.count(")"):
           ls.append(s2)
           s2 = ""
   return ls
print(test("( ()) ((()()())) (()) ()"))