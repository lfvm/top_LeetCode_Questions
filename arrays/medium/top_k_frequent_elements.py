"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


https://leetcode.com/problems/top-k-frequent-elements/description/

Explanation: https://www.youtube.com/watch?v=YPTqKIgVk-k

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #Getting the frequency of every element
        count = {}

        # We are going to store in a list a mapping where the index in the list is equal to te 
        # Frequency of a number, and the value is going to be a list of all of the elements 
        # With that frequency. The value in the index is a list and not a number because there 
        # Can be many numbers in the original array with the same frequency  

        # We initialize an empty lists with lists. This list will alway be the same lenght of the 
        # Original array 
        indexes = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            count[num] = 1 + count.get(num,0)
        
        # Populating our helper list, mapping the index with frequency
        for number, frequency in count.items():
            indexes[frequency].append(number)

        result = []

        #Iterate from the end of the array. Naturally the most frequent elements will alway be at the end
        #
        for i in range(len(indexes) -1, 0, -1):
            
            for n in indexes[i]:
                result.append(n)
                if len(result) == k: 
                    return result
        