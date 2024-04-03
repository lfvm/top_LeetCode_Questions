"""

28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == needle:
            return 0
        
        k = len(needle)
        l = 0 
        for i in range(len(haystack)):

            substring = haystack[l:l+k]
            if substring == needle:
                return i 
            
            l+= 1

        return -1