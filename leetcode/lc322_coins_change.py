# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
import sys
"""
dp的思想就是归纳假设
n = number of types of coins
m = desired amount
f[i][j] means min number of coins make up the amount of j with only coins[i...n-1]
f[i][j] = min(f[i+1][j-k*coins[i]] + k)

base case
f[n][0] = 0
f[n][1...m] = infinity
"""

class Solution(object):
    """
    dp
    """
    def coinChange_dp(self, coins, amount):
        array = []
        for i in range(len(coins)+1):
            array.append([sys.maxsize] * (amount + 1))
        array[len(coins)][0] = 0

        for i in range(len(coins)-1, -1, -1):
            for j in range(amount + 1):
                array[i][j] = array[i+1][j]
                maxK = j // coins[i]
                # print('maxk', maxK)
                for k in range(1, maxK+1):
                    # print('i', i, 'j', j)
                    prev = array[i+1][j - coins[i] * k]
                    # print(i+1, j - coins[i] * k)
                    if prev < sys.maxsize:
                        array[i][j] = min(array[i][j], prev + k)
        print(array)
        return array[0][amount]

    def coinChange_dp2(self, coins, amount):
        array = []
        for i in range(len(coins)+1):
            array.append([sys.maxsize] * (amount + 1))
        array[len(coins)][0] = 0

        for i in range(len(coins)-1, -1, -1):
            for j in range(amount + 1):
                array[i][j] = array[i+1][j]
                if j >= coins[i]:
                    prev = array[i][j - coins[i]]
                    if prev < sys.maxsize:
                        array[i][j] = min(array[i][j], prev + 1)
                    # maxK = j // coins[i]
                    # print('maxk', maxK)
                    # for k in range(1, maxK+1):
                    #     # print('i', i, 'j', j)
                    #     prev = array[i+1][j - coins[i] * k]
                    #     # print(i+1, j - coins[i] * k)
                    #     if prev < sys.maxsize:
                    #         array[i][j] = min(array[i][j], prev + k)
        # print(array)
        # print(array[0][amount])
        if array[0][amount] == sys.maxsize:
            return -1
        return array[0][amount]

    """
    bruce force : O(S^n)
    """
    def coinChange_bruce_force(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.coinChanges(0, coins, amount)
    def coinChanges(self, idxCoin, coins, amount):
        if(amount == 0):
            return 0
        if idxCoin < len(coins) and amount > 0:
            maxVal =  amount//coins[idxCoin]
            minCost = sys.maxsize
            for i in range(maxVal + 1):
                if amount >= i * coins[idxCoin]:
                    res = self.coinChanges(idxCoin+1, coins, amount - i*coins[idxCoin])
                    # res = -1 代表没有结果
                    if res != -1:
                        minCost = min(minCost, res + i)
            if minCost == sys.maxsize:
                return -1
            else:
                return minCost
            # return minCost == sys.maxsize ? -1 : minCost
        return -1





if __name__ == "__main__":
    # print(Solution().coinChange_bruce_force([1,2,5], 11))
    Solution().coinChange_dp2([2], 3)
