"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

"""


def containsDuplicate(nums) -> bool:
    
    frequencies = {}
    for number in nums: 
        if number not in frequencies: 
            frequencies[number] = 1
        else:
            return True 
    
    
    return False 



