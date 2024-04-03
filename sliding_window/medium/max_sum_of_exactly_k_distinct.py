"""
2461. Maximum Sum of Distinct Subarrays With Length K



You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.


Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
"""

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0  
    
        l = 0 
        window_sum = 0
        total_sum = window_sum
        visit = set()
        
        for r in range(len(nums)):

            while nums[r] in visit:
                window_sum -= nums[l]
                if nums[l] in visit:
                    visit.remove(nums[l])
                l+=1 
            
            window_sum += nums[r]
            visit.add(nums[r])

            if (r-l+1) == k:    
                total_sum = max(window_sum, total_sum)
                window_sum -= nums[l]
                visit.remove(nums[l])
                l+=1

        return total_sum