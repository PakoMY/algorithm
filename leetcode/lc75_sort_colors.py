
''' Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

 Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

 Note: You are not suppose to use the library's sort function for this problem.

 Example:

 Input: [2,0,2,1,1,0]
 Output: [0,0,1,1,2,2]

 思想 ： partition sort
 '''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                self.swap(nums, left, i)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(nums, right, i)
                right -= 1
        return nums
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

if __name__ == '__main__':
    Solution().sortColors([2,0,2,1,1,0])
