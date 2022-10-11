#coding:utf-8
"""
 Write a Python program to computing square roots using the Babylonian method. Go to the editor
Perhaps the first algorithm used for approximating √S is known as the Babylonian method, named after the Babylonians, or "Hero's method", named after the first-century Greek mathematician Hero of Alexandria who gave the first explicit description of the method. It can be derived from (but predates by 16 centuries) Newton's method. The basic idea is that if x is an overestimate to the square root of a non-negative real number S then S / x will be an underestimate and so the average of these two numbers may reasonably be expected to provide a better approximation."""
def BabylonianAlgorithm(number):
    if(number == 0):
        return 0;

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;
print('The Square root of 0.3 =', BabylonianAlgorithm(0.3));

