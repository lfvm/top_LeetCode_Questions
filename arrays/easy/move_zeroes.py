"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #Fast pointer approach

        #slow
        i = 0 

        #fast
        j = i+1

        while j < len(nums):

            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
            
            # Means that i is in a position tha has been swaped at this point 
            # So we can move to the next number
            if nums[i] != 0:
                i+=1 
            j+=1 


