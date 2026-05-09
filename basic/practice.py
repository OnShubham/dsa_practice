def gcd(n1,n2):
    
    while n2 != 0:
        n1, n2, = n2, n1 % n2
        
    return print(n1)


n1 = 9
n2 = 6    
gcd(n1,n2)


def devisor(n):
    
    res = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            res.append(i)
    return print(res)

n = 54
devisor(n)



def reverse(n):
    
    rev = 0
    
    while n > 0:
        ld = n % 10
        rev = rev * 10 + ld
        n = n // 10
    
    return print(rev)

n = 123
reverse(n)
        
        