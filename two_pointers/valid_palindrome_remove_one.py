def is_palindrome(s):
    left = 0
    right = len(s) - 1
    removed = False
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if removed:
                return False 
            if s[left + 1] == s[right]:
                left += 1
            elif s[left] == s[right - 1]:
                right -= 1
            else: 
                return False
            removed = True
    return True