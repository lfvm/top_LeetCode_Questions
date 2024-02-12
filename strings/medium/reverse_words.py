"""
151. Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Input: s = "the sky is blue"
Output: "blue is sky the"


https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        tmpWord = ""
        words = []
        for char in s:
            
            if char == " " and len(tmpWord) >= 1:
                words.append(tmpWord)
                tmpWord = ""
            
            if char != " ":
                tmpWord += char

        if len(tmpWord) >= 1:
            words.append(tmpWord)
        words.reverse()

        return " ".join(words)
        