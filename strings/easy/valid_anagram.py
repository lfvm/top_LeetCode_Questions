"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

"""

def isAnagram( s: str, t: str ) -> bool:
    
    #Las palabras deben tener la misma longitud 
    if len(s) != len(t):
        return False
    
    #Contar las frecuencias de cada letra en ambas palabras
    sFrequencies = getFrequencies(s)
    tFrequencies = getFrequencies(t)
    
    for letter in sFrequencies.keys():
        # Si en cualquier momento las frecuencias son diferentes entonces no es un anagrama
        if sFrequencies.get(letter) != tFrequencies.get(letter):
            return False
        
    return True 



def getFrequencies( string ):
    # Guarda en un mapa la frecuencia de cada letra en un string
    frequencies = {}
    
    for letter in string:
        if letter in frequencies:
            frequencies[letter] += 1 
        else:
            frequencies[letter] = 0 
    
    return frequencies
    
    
   