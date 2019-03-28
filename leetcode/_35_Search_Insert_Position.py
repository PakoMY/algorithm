class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            if target == nums[left]:
                return left
            m = left + (right-left)//2
            if nums[m] == target:
               # print(m, '~~~~~~m')
                return m
            elif nums[m] < target:
                #print(left, '~~~~~~left')
                left = m + 1
                #print(left, '~~~~~~left~~~')
                #print(right, '~~~~~~right~~~')

            else:
                #print(right, '~~~~~~right')
                right = m
        if target < nums[left]:
            if left == 0:
                return 0
            return left
        elif target > nums[right]:
            return right + 1

        elif target == nums[right] or (target > nums[left] and target < nums[right]):
            return right

        elif target == nums[left]:
            return left
if __name__=="__main__":
    print(Solution.searchInsert([1,2,6,8,12], 4))
