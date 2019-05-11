# 【本期题目】
# 给定一个数组 {3, 1, 2, 1} 和一个数字k =4。求这个数组的一个最长连续子数组，这个最长连续子数组中所有数字的和必须小于或等于k。
#
# 例如，上面这个例子中，连续子数组有这么多种情况：
# {3}, {1}, {2}, {1}, {3, 1}, {1, 2}, {2, 1}, {3, 1, 2}, {1, 2, 1}, {3, 1, 2, 1}。
# 其中符合条件的就只有{1, 2, 1}。

class Solution():
    def longest_subarray(self, array, k):
        result = []
        sum = 0
        length = 0
        left = right = 0
        for i in range(len(array)):
            sum += array[right]
            length += 1
            if(sum <= k):
                result.append((sum, length))
                right += 1
            else:
                sum -= array[left]
                length -= 1
                result.append((sum, length))
                left += 1
                right += 1
        print(result)

        sum = 0
        length = 0
        for i in range(len(result)):
            if result[i][0] > sum and result[i][0] <= k and result[i][1] > length:
                sum = result[i][0]
                max = i
                print(result[i][0],sum, max)
        right = max
        left = right - result[max][1] + 1
        goal = []
        for i in range(left, right + 1):
            goal.append(array[i])
        print(goal)
if __name__ == "__main__":
    Solution().longest_subarray([1,2,1,3,1,1,1], 4)
