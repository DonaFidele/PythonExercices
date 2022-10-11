#coding:utf-8
"""Write a Python class to find the three elements that sum to zero from a set of n real numbers. Go to the editor
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]"""

class SumZero:
    def findElement(self,liste):
        result,cleanResult=[],[]
        for i in liste:
            for j in liste[1:]:
                for k in liste[2:]:
                    if i+j+k==0:               
                        result.append(list(set([i,j,k])))
        for results in result:
            if results not in cleanResult:
                cleanResult.append(results)
        
        return cleanResult

print(SumZero().findElement([-25, -10, -7, -3, 2, 4, 8, 10]))