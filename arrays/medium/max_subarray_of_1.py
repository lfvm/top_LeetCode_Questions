"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeroCount = 0 
        longestWindow = 0 
        l = 0 

        for r in range(len(nums)):
            zeroCount += 1 if nums[r] == 0 else 0 

            while zeroCount > 1:
                
                zeroCount -= 1 if nums[l] == 0 else 0 
                l += 1 
                
            longestWindow = max(longestWindow, r-l)


        return longestWindow