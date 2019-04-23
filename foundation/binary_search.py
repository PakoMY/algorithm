def bsearch(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    if n == 0 or target < nums[l] or target > nums[r]:
        return False
    while l < r:
        ans = (l + r) // 2
        if target > nums[ans]:
            l = ans + 1
        if target == nums[ans]:
            return ans
        else:
            right = ans - 1
    if targrt > nums[l]: return l + 1
    else:   return l 
