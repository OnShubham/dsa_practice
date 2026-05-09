def palindrome(n):
    
    rev = 0
    orignal = n
    while n > 0:
        
        get_digits = n % 10
        
        rev = rev * 10 + get_digits
        
        n = n // 10
        
    if orignal == rev:
        return print(True)
    else:
        print(False)


n = 124
palindrome(n)
        
    