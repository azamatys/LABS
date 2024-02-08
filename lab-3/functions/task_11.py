def Palindrome(word):
    cnt = 0
    n = len(word)
    for i in range(0, len(word)//2):
        if word[i] == word[n-i-1] :
            cnt+=1
    if cnt == len(word)//2:
        return True
    else:
        return False
    
word = input()
print(Palindrome(word))


# def Palindrome(word):
#     n = len(word)
#     for i in range(n // 2):
#         if word[i] != word[n - i - 1]:
#             return False
#     return True

# word = input()
# print(Palindrome(word))