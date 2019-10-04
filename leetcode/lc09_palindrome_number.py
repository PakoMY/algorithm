class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0 or (x % 10 == 0 and x != 0)): return False
        tmp = 0
        while(x > tmp):
            tmp = tmp * 10 + x % 10
            x /= 10
        return tmp == x or x == tmp / 10

if __name__=="__main__":
    print(Solution().isPalindrome(1211))
