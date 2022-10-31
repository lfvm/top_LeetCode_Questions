"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1: 
    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Example 2: 
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
"""

def getNumberValueIfCompound(current, i, string):
    
    # LLegamos al final del numero, por lo tanto no habra un numero adicional a la derecha
    if  len(string) - 1 == i :
        return None

    nextLetter = string[i + 1]
    if current == "I" and  nextLetter == "V":
        return 4
    if current == "I" and  nextLetter == "X":
        return 9
    if current == "X" and nextLetter == "L":
        return 40
    if current == "X" and nextLetter == "C":
        return 90
    if current == "C" and nextLetter == "D":
        return 400
    if current == "C" and nextLetter == "M":
        return 900

    return None
    
def romanToInt(s: str) -> int:
    romanNumbers = {
        "I" : 1,
        "V" : 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    skip = False

    for i in range(len(s)):

        if skip:
            skip = False
            continue

        intNumber = getNumberValueIfCompound(s[i],i,s)
        if intNumber is not None:
            total += intNumber
            skip = True
        else:
            total += romanNumbers[s[i]]
            skip = False

    return total
