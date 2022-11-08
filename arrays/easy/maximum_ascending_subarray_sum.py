"""
1800. Maximum Ascending Subarray Sum
https://leetcode.com/problems/maximum-ascending-subarray-sum/

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.


Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65

"""


def maxAscendingSum( nums ) -> int:
        
    maxSum = 0 
    currentSum = 0
    
    for i, num in enumerate(nums):
        
        #No tomar en cuenta el primer elemento de la lista
        if i > 0:
            #Si ya no es ascendiente resetear la cuenta  y
            #Comenzar la cuenta nueva con el numero actual
            if nums[i-1] >= num:
                currentSum = 0 
                currentSum += num 
            else:
                currentSum += num 
                maxSum = max(maxSum,currentSum)
        else:
            currentSum += num
            maxSum = max(maxSum,currentSum)
    
    return maxSum 