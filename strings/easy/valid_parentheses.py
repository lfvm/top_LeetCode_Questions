"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


def matchesCharacter( opening, closing ):
        if opening == "{" and closing == "}":
            return True
        if opening == "(" and closing == ")":
            return True
        if opening == "[" and closing == "]":
            return True
        return False 

   
def isValid(s: str) -> bool:
    stack = []
    
    for char in s:

        if char in "{[(":
            stack.append(char)
        else:
            
            #Llegamos a un punto donde no hay elementos de apertura que coincidan con uno de cierre
            if len(stack) == 0:
                return False 

            openingChar = stack.pop()

            #Verificar que un elemento de cierre coincida con el elemento de apertura
            if not matchesCharacter(openingChar, char):
                return False

    #Sobraron elementos en el stack
    if len(stack) != 0:
        return False
    return True
    
             


