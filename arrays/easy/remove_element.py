"""

    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Exapmle 1:
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Your function should return k = 2, with the first two elements of nums being 2.
        It does not matter what you leave beyond the returned k (hence they are underscores).

"""

def removeElement( nums, val ) -> int:
        
        
    end = len(nums)
    i = 0 
    
    while i < end:
        
        if (nums[i] == val):
            
            nums[i] = nums[end - 1]
            end -= 1 
        
        else:
            
            i +=1 
    
    return end


"""
    SOLUCION:

        Se debe tener un pointer al final del arreglo y uno en el indice actual de iteración

        si el elemento actual es igual al valor, entonces movemos el elemento actual al final del arreglo y decrementamos el valor del final para poner los elementos que no nos interesan hasta el fondo del arrgelo.

        Si el numero actual no es igual al valor entonces continuamos iterando, para ello se incrementa i 

        Por ultimo se regresa la variable de longitud

"""