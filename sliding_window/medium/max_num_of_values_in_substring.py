"""
1456. Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        i = 0
        maxVowels = 0
        currCount = 0

        # Initialize the count for the first window
        for j in range(k):
            if s[j] in vowels:
                currCount += 1
        maxVowels = currCount

        # Slide the window, update counts and maxVowels as needed
        for j in range(k, len(s)):
            if s[i] in vowels:
                currCount -= 1
            if s[j] in vowels:
                currCount += 1
            maxVowels = max(currCount, maxVowels)
            i += 1

        return maxVowels