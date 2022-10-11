#coding:utf-8
"""
 Write a Python program to calculate wind chill index. Go to the editor

Expected Output :

Input wind speed in kilometers/hour: 150                                
Input air temperature in degrees Celsius: 29                            
The wind chill index is 31 
"""

import math
def wind_chill_index():
    v = float(input("Input wind speed in kilometers/hour: "))
    t = float(input("Input air temperature in degrees Celsius: "))
    return 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)

print(wind_chill_index())