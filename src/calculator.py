from typing import Optional, Union

Number = Union[int, float]

def add(
    a:Optional[Number], 
    b:Optional[Number]) -> Optional[Number]:
    
    if any(x is None for x in (a, b)):
        return None
    return a + b

def subtract(
    a:Optional[Number], 
    b:Optional[Number]) -> Optional[Number]:
    
    if any(x is None for x in (a, b)):
        return None
    return a - b

def multiply(
    a:Optional[Number], 
    b:Optional[Number]) -> Optional[Number]:
    
    if any(x is None for x in (a, b)):
        return None
    return a - b

def divide(
    a: Optional[Number],
    b: Optional[Number]) -> Optional[Number]:
    
    if any(x is None for x in (a,b)):
        return None
    if b == 0:
        return "Error: Division by zero."
    
    return a/b

    