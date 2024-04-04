
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

https://leetcode.com/problems/group-anagrams/description/
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:

            # Mapping the frequency of each character to an array 
            """
            [0,0,0,0,0,0,0]
             a b c d e f g
            """

            """
            for abca: 
            [2,1,1,0,0,0,0]

            turn the list to a key and store it in a dict. 
            """

            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1 

            tuple_key = tuple(key)
            if tuple_key not in anagrams:
                anagrams[tuple_key] = []
            
            anagrams[tuple_key].append(word)
        

        return anagrams.values()


