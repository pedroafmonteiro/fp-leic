def find_me(f, limits):
    left, right = limits
    count = 0
    
    while left <= right:
        mid = (left + right) // 2
        result = f(mid)
        
        if result == 0:
            return count + 1
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1
        count += 1