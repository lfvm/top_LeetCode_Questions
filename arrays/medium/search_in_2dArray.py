"""
74. Search a 2D Matrix

matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        
        # Binary search in matrix to find the target list 
        
        targetList = None
        l = 0 
        r = len(matrix) - 1
        
        while l <= r:
            
            mid = (l+r) // 2
            currentList = matrix[mid]
            targetList = currentList

            if target > currentList[-1]:
                l = mid +1 
            elif target < currentList[0]: 
                r = mid - 1 
            else: 
                break
                
        #binary search on resulting list 
        
        l = 0 
        r = len(targetList) - 1
        
        while l <= r:
            
            mid = (l+r) // 2            
            if target < targetList[mid]:
                r = mid -1 
            elif target > targetList[mid]:
                l = mid + 1 
            else: 
                return True
                
            