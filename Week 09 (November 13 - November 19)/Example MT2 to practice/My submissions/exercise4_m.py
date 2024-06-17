def add(num1, num2):
    # Find the length of the numbers
    len1 = len(num1)
    len2 = len(num2)

    # Find the position of the decimal point in each number
    decimal1 = num1.index('.')
    decimal2 = num2.index('.')

    # Calculate the number of digits to the left and right of the decimal point
    left1 = decimal1
    right1 = len1 - decimal1 - 1
    left2 = decimal2
    right2 = len2 - decimal2 - 1

    # Make the lengths of the numbers equal by adding zeros
    if left1 < left2:
        num1 = '0' * (left2 - left1) + num1
        left1 = left2
    elif left2 < left1:
        num2 = '0' * (left1 - left2) + num2
        left2 = left1

    if right1 < right2:
        num1 = num1 + '0' * (right2 - right1)
        right1 = right2
    elif right2 < right1:
        num2 = num2 + '0' * (right1 - right2)
        right2 = right1

    # Perform the addition digit by digit
    carry = 0
    result = ''
    for i in range(len(num1) - 1, -1, -1):
        if num1[i] == '.':
            result = '.' + result
            continue

        digit1 = int(num1[i])
        digit2 = int(num2[i])
        sum_digits = digit1 + digit2 + carry
        result = str(sum_digits % 10) + result
        carry = sum_digits // 10

    # Add the carry if it is greater than 0
    if carry > 0:
        result = str(carry) + result

    # Remove unnecessary zeros at the beginning and end of the result
    result = result.lstrip('0').rstrip('0')

    return result

print(add('123.456', '0.124'))