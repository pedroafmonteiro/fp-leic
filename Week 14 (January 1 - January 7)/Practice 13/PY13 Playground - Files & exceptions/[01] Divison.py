def division(a, b):
    try:
        result = a / b
        return f'{a}/{b} = {result}'
    except ZeroDivisionError:
        return "can't divide by 0!"
    except TypeError:
        return "unsupported operand type(s) for division"
    
print(division(10, 'b'))