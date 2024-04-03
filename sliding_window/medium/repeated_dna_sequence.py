"""
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

https://leetcode.com/problems/repeated-dna-sequences/description/

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        visited = defaultdict(int)

        if len(s) < 10:
            return []
        

        for i in range(len(s) - 9):
            key = s[i:i+10]
            visited[key] +=1

        return [key for key in visited if visited[key] > 1]


        



