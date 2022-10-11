#coding:utf-8
"""
 Write a Python program to get the length and the angle of a complex number. Go to the editor

Expected Output :

Length of a complex number:  5.0                                                 
Complex number Angle:  1.5707963267948966
"""

import cmath
cn = complex(3,4)
#length of a complex number. 
print("Length of a complex number: ", abs(cn))
# gets angle. return in radians, between  [-π, π]
print("Complex number Angle: ",cmath.phase(0+1j) )
