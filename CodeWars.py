#Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.
def divisible_by(numbers, divisor):
    result = []
    
    for e in numbers:
        
        if (e / divisor) == int(e / divisor): 
            result.append(e)
    
    return result

numbers = int(input('Введите числа, которые нужно разделить.\n'))
divisor = int(input('Введите делитель.\n'))
print(divisible_by(numbers, divisor))