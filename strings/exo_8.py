#coding:utf-8
"""
Write a Python function that takes a list of words and return the longest word and the length of the longest one. Go to the editor
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""
def test(liste):
    return f"Longest word: {max(liste,key=len)}\nLength of the longest word:{len(max(liste,key=len))}"
print(test(["PHP", "Exercises", "Backend"]))