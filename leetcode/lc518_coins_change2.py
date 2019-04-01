# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.
import sys

"""
base case
f[0][0] = 1
f[0][1...m] = 0
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array = []
        for i in range (len(coins) + 1):
            array.append([0] * (amount + 1))


        array[0][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(amount + 1):
                array[i][j] = 0
                k = 0
                while(k * coins[i - 1] <= j):

                    array[i][j] += array[i-1][j-k*coins[i-1]]
                    k += 1
        print(array)
        return array[len(coins)][amount]

    def coinChange_2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array = []
        for i in range (len(coins) + 1):
            array.append([0] * (amount + 1))


        array[0][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(amount + 1):
                array[i][j] = 0
                # k = 0
                if coins[i-1] <= j:
                    array[i][j] = array[i-1][j] + array[i][j - coins[i-1]]
                else:
                    array[i][j] = array[i-1][j]
                # while(k * coins[i - 1] <= j):
                #     array[i][j] += array[i-1][j-k*coins[i-1]]
                #     k += 1
        print(array)
        return array[len(coins)][amount]


if __name__ == "__main__":
    print(Solution().coinChange_2([1,2,5], 5))
