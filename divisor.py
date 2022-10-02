def divisible_by(numbers, divisor):
    result = []
    
    for e in numbers:
        
        if (e / divisor) == int(e / divisor): 
            result.append(e)
    
    return result