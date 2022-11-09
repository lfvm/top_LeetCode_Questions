"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix( strs ) -> str:
        
    result = ""
    #Utilizar la primera palabra de la lista para comparar 
    firstWord = strs[0]
    
    for i in range(len(firstWord)):
        #Comparar cada letra del string con las demas palabras del array
        for word in strs:
            
            #Si llegamos al final del primer string 
            #quiere decir que ya no podemos encontrar un prefijo mas grande
            if i == len(word) or firstWord[i] != word[i]:
                # Ademas si la letra de la primera palabra es diferente 
                # a la letra de la comparación actual quiere decir 
                # que ya no existe un prefijo comun mas grande
                return result
        
        result += firstWord[i]
    
    return result
            