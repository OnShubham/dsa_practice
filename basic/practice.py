# def gcd(n1,n2):
    
#     while n2 != 0:
#         n1, n2, = n2, n1 % n2
        
#     return print(n1)


# n1 = 9
# n2 = 6    
# gcd(n1,n2)


# def devisor(n):
    
#     res = []
    
#     for i in range(1, n + 1):
        
#         if n % i == 0:
#             res.append(i)
#     return print(res)

# n = 54
# devisor(n)



# def reverse(n):
    
#     rev = 0
    
#     while n > 0:
#         ld = n % 10
#         rev = rev * 10 + ld
#         n = n // 10
    
#     return print(rev)

# n = 123
# reverse(n)
        
        
        
        
vovel = "aouel"
name = "shubam"
res = ""

for char in name:
    if char in vovel:
        res += "*"
    else:
        res += char
print(res)



def reverse_nu(n):
    
    k = 0
    
    while n > 0:
        
        digits = n % 10
        
        k = k * 10 + digits
        
        n = n // 10
        
    return print(k , "s")

n = 234
reverse_nu(n)




voevl = "voevl"

name = "shuiobvel"

result = ""

for char in name:
    if char in vovel:
        result += "*"
    else:
        result += char
print(result)



def find_repeatetd_word(n):
    
    dict = {}
    
    for char in n:
        
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char, count in dict.items():
        print(char, count)
            
        
        
    






n = "shubamssdsh"
find_repeatetd_word(n)



def find_char_count(text):
    
    char_count = {}
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char, count in char_count.items():
        print(f"{char} -> {count}")
    # return print(char_count)

text = "asdfghjkasdfghjksdfghj"
find_char_count(text)



def divisor_num(n):
    
    if n == 0:
        return
    
    res = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            res.append(i)
            
    print(res)

n = 12
    
divisor_num(n)
    
        
        
        
        