def arr_sorted(arr,n):
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return print("False")
    return print("True")


arr = [6,1,2,3,4,6]
n = len(arr)
arr_sorted(arr,n)


def check_sorted(arr,n):
    
    for i in range(n):
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                return print("f")
    return print("t")


arr = [6,1,2,3,4,6]
n = len(arr)
check_sorted(arr,n)



def find_arr_sor(arr,n):
    
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                return print("false")
    return print("true")


arr = [1,2,3,4,6]
n = len(arr)
find_arr_sor(arr,n)