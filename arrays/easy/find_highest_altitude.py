"""
1732. Find the Highest Altitude


There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        max_altitude = 0 
        current_altitude = max_altitude 

        for point in gain: 
            current_altitude += point
            max_altitude = max(max_altitude,current_altitude)


        return max_altitude