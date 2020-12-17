class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        a, b = 0, 1
        res = 0
        for _ in range(2, n + 1):
            res = a + b
            a, b = b, res
        return res % 1000000007


if __name__ == '__main__':
    n = 5
    res = Solution().fib(n)
    print("res: ", res)
