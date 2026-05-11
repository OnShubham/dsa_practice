def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n -1 , -1, -1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        
        if not did_swap:
            break
        
    
    print(arr)
    
arr = [22,3,2,1,44,2]
bubble_sort(arr)