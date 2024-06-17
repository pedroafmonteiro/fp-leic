def palindrome_index(s):
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            y = s[:i] + s[i+1:]
            if y == y[::-1]:
                return i
    return -1

print(palindrome_index('radgar'))