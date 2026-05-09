def palindrome(num):
    
    k = len(str(num))
    sum = 0
    n = num
    
    while n > 0:
        ld = n % 10
        sum += ld ** 10
        n = n // 10
    
    return print(sum)
    
num = 152
palindrome(num)
    
    
    
def palindrome_1(num):
    
    k = len(str(num))
    sum = 0
    value = num
    
    while num > 0:
        
        ld = num % 10 
        
        sum += ld ** k
        
        num = num // 10
        
    return print(sum)

num = 153
palindrome_1(num)