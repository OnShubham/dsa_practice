def arm(num):
    
    k = len(str(num))
    sum = 0
    
    while num > 0:
        
        ld = num % 10
        
        sum += ld ** k
        
        num = num // 10
        
    return print(sum)

num = 153
arm(num)