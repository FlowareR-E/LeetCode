def countTriplets(nums):
    n = len(nums)
    count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                continue
            for k in range(j + i, n):
                if nums[i] != nums[k] and nums[j] != nums[k]:
                    count += 1
    return count

# Note: this method is very time complex n^3 THIS IS A TEST
