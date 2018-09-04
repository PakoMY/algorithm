def findShortestSubArray(nums):
    left, right, count = {}, {}, {}
    result = len(nums)
    for i, element in enumerate(nums):
        if element in left:
            right[element] = i
        else:
            left[element] = i
        count[element] = count.get(element, 0) + 1
    frequency = max(count.values())
    if len(nums) == 1 or right == {}:
        return 1
    for i in count:
        if count[i] == frequency:
            result = min(result, right[i] - left[i] + 1)
    
    return result
