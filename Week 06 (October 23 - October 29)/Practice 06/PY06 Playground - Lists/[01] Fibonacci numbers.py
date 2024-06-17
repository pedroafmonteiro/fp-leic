def fib(n):
    fib_list = [0, 1]  # Initialize the list with the first two numbers
    
    if n <= 2:
        return fib_list[:n]  # Return the list up to n if n is less than or equal to 2
    
    for i in range(2, n):
        next_num = fib_list[i-1] + fib_list[i-2]  # Calculate the next number
        fib_list.append(next_num)  # Add the next number to the list
    
    return fib_list