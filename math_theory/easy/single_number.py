"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

https://leetcode.com/problems/single-number/description/?envType=featured-list&envId=top-100-liked-questions
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0 
        for num in nums:
            result ^= num
        
        return result
    
"""
Explanation: 
use xor binary operator:

lets remember that if we do an xor operation on the binary values of two repeated numbers we are always going to get 0:

2 in binary:

1 0 
1 0 

xor operation: 
0 0  to decimal -> 0 

if we have an xor operation with 0 and any other number, the result will allways be the other number

0 and 2 for example 
0 0 
1 0 

xor operation:
1 0 to decimal -> 2 


which means:

2^2 = 0 
2^2^3 = 3 
2^2^3^3^1 = 1
"""