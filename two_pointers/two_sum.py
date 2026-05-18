def two_sum(nums, target):
    
    for i in range(len(nums)):
        
        for j in range(i + 1, len(nums)):
            
            if nums[i] + nums[j] == target:
                return print("true")
            
    return print("f")


nums = [1,3,4,6,8,10,13]
target = 6

two_sum(nums, target)