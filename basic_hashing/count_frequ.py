def count_frequ(t):
    
    freq = {}
    
    for char in t:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return print(freq)   
    

n = "shubhamsdfsd"
t = [10,5,10,15,10,5]
count_frequ(t)