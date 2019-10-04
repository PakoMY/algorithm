"""
一般用hashmap的话key存储的是具体的输入的值，value存储的是序号
"""

def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in dic.keys():
            return [dic.get(comp), i]
        dic[nums[i]] = i

twoSum([2,7,11,15], 9)
