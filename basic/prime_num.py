def print_num(n):
    
    cnt = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    
    return cnt == 2

n = 10
prime = print_num(n)

if prime:
    print(f"{n} prime")
else:
    print(f"{n} not")
    