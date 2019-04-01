
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.

"""思路：bruce force O(n^3), sort + for O(nlogn), hashset O(n)"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        length = 0
        for i in num_set:
            if not i - 1 in num_set:
                currrent = i
                currrent_length = 1
                while (currrent + 1 in num_set):
                    currrent_length += 1
                    currrent += 1
                length = max(length, currrent_length)
        return length
if __name__ == "__main__":
    Solution().longestConsecutive([0,-1])
