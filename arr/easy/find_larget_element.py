def largets_elements(arr):
    
    max = arr[0]
    n = len(arr)
    
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return print(max)

arr = [4,5,3,2,5,2,3,1,3]
largets_elements(arr)
        
    
    
    
def max_arr(arr,n):
    
    max = arr[0]
    
    for i in range(1, n):
        
        if arr[i] > max:
            max = arr[i]
    return print(max)


arr = [5,4,3,2,5,6,3]
n = len(arr)
max_arr(arr,n)