def threeSum(nums):
    nums.sort()
    result = set()
    n = len(nums)

    for i in range(n - 2):
        j = i + 1
        k = n - 1

        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                result.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif s < 0:
                j += 1
            else:
                k -= 1

    return [list(_) for _ in result]

print(threeSum([-1,0,1,2,-1,-4]))
