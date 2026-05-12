def rever_num(arr):
    
    rev = 0
    while arr > 0:
        ld = arr % 10
        rev = rev * 10 + ld
        arr = arr // 10
        
    return print(rev)

arr = 123
rever_num(arr)