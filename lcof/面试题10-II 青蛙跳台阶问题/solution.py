class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        a, b = 1, 1
        res = 0
        for _ in range(2, n + 1):
            res = a + b
            a, b = b, res
        return res % 1000000007


if __name__ == '__main__':
    n = 7
    res = Solution().numWays(n)
    print("res: ", res)
