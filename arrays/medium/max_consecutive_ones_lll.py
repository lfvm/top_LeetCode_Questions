"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
         
        zeroCount = 0 
        longestWindow = 0 
        l = 0 

        for r in range(len(nums)):
            zeroCount += 1 if nums[r] == 0 else 0 

            while zeroCount > k:
                
                zeroCount -= 1 if nums[l] == 0 else 0 
                l += 1 
                
            longestWindow = max(longestWindow, r-l +1)


        return longestWindow 