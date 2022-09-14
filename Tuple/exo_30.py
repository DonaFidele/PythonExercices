#coding:utf-8
"""Write a Python program to check if a specified element presents in a tuple of tuples. Go to the editor
Original list:
(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
Check if White presenet in said tuple of tuples!
True
Check if White presenet in said tuple of tuples!
True
Check if Olive presenet in said tuple of tuples!
False
"""
def check_in_tuples(colors, c):
    result = any(c in tu for tu in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
print("Original list:")
print(colors)
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
