"""
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].
"""

def plusOne(digits):
    i = len(digits) - 1

    while (i >= 0):
        
        if digits[i] == 9: 
            digits[i] = 0
        
        else: 
            digits[i] += 1 
            return digits
        i -=1
        
        
    digits.insert(0,1)

    
    return digits
plusOne([9])