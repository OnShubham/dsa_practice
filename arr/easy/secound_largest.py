def secound_largest(arr,n):
    
    rev = 0
    
    while n > 0:
        
        ld = n % 10
        rev = rev * 10 + ld
        n = n // 10
    
        return print(rev)
    
    
    
    
    
    
arr = 1,2,5,6
n = len(arr)
secound_largest(arr,n)