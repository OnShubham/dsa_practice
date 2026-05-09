
def nse_num(n):
    
    rev = 0
    
    while n > 0:
        digits = n % 10  # get last digits 
        rev = rev * 10 + digits
        n = n //10    # removed the last digis
    
    return print(rev)


n = 123
nse_num(n)