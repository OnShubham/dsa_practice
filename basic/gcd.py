def gcd(n1,n2):
    
    while n2 != 0:
        n1, n2 = n2, n1 % n2
        
    return print(n1)
    
n1 = 6
n2 = 3
gcd(n1,n2)
        