def spy_game(nums):
    target1 = 0
    target2 = 0
    target3 = 0
    for x in nums:
        if x == target1:
            target1 = target2
        elif x == target2:
            target2 = target3
        elif x == target3:
             return True
        else:
            return False 
        
nums = [1,2,4,0,0,7,5]
print(spy_game(nums))