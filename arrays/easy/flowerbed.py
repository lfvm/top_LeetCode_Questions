"""

605. Can Place Flowers


You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Need to track 3 adjacent places at same time, we add extra places 
        # So we do not overflow while looping
        f = [0] + flowerbed + [0]


        for i in range(1, len(f)-1): #Skip first and last elements 

            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                n-=1
                f[i] = 1

        return n <=0

