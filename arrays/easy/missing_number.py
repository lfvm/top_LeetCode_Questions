"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

"""


def missingNumber1( nums ) -> int:
    """
        Solucion:
        1. Realizar la suma de los numeros de 1 hasta n (longitud de array)
        2. Realizar la suma de los numeros dentro del array 
        3. el numero que falta sera la resta de los valores anteriores
    """
        
    #Obtener la suma de los numeros desde 1 hasta n usando
    #Formula para reducir complejidad de tiempo
    n = len(nums)
    totalSum = int((n * (n+1) )/ 2)
    
    arraySum = 0
    # Sumar los valores de la lista 
    for num in nums:
        arraySum += num
    
    #El numero que falta es la resta del total menos la suma de 
    #los numeros de la lista
    return totalSum - arraySum


def missingNumber2( nums ) -> int:
    """
        Solucion:
        Utilizar el operador xor para encontrar el valor faltante 

        recordemos que el xor cancela dos numeros iguales: 5 ^ 5 = 0 
        sin embargo si tenemos la operacion 5^3^5 el resultado sera 3 ya que los 5 se cancelan 
        y unicamente quedara el numero no repetido.

    """

    result = 0
    
    for counter,value in enumerate(nums):
        
        result ^= counter+1 # XOR result with numbers from the complete series
        result ^= value # XOR with the numbers given in num series
        
    return result

