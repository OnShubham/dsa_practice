def gcd(n1,n2):
    
    while n2 != 0:
        n1, n2, = n2, n1 % n2
        
    return print(n1)


n1 = 9
n2 = 6    
gcd(n1,n2)