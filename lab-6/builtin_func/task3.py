def is_palindrome(s):
    s = ''.join(char.lower() for char in s)
    pal = (s == s[::-1])
    return pal

x = str(input())
print(is_palindrome(x))