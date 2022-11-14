"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""



def lengthOfLongestSubstring( s: str ) -> int:
    
    maxLength = 0 
    i = 0 
    j = 0 
    
    currentFrequencies = {}
    currentMax = 0 
    
    while i < len(s):
        
        if j == len(s):
            return maxLength
    
        currentLetter = s[j]
        #Se encontro un valor repetido, resetear todo y mover i 
        #A la siguient letra y resetar j
        if currentLetter in currentFrequencies:
            
            currentFrequencies.clear()
            currentMax = 0 
            i+= 1 
            j = i
            
        else:
            currentMax +=1 
            currentFrequencies[currentLetter] = 1 
            maxLength = max(maxLength, currentMax)
            j+= 1
        
    
    return maxLength
            

"""
Solucion 1:

Utilizar dos pointers y un hasmap para ver si se encuentran elementos repetidos:

Mover j hasta que encuentre un elemento repetido, en ese caso resetar la cuenta 
y mover i a la siguiente letra 
"""