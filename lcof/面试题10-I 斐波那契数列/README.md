# [面试题10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof)

## 题目描述

<!-- 这里写题目描述 -->

<p>写一个函数，输入 <code>n</code> ，求斐波那契（Fibonacci）数列的第 <code>n</code> 项。斐波那契数列的定义如下：</p>

<pre>F(0) = 0, F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N &gt; 1.</pre>

<p>斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。</p>

<p>答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>5
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>

<p>注意：本题与主站 509 题相同：<a href="https://leetcode-cn.com/problems/fibonacci-number/">https://leetcode-cn.com/problems/fibonacci-number/</a></p>


## 解法

<!-- 这里可写通用的实现逻辑 -->
定义两个变量a, b用来保存前两个元素的值，根据定义即可解决。需要注意的是遍历的时候需要取到n。
<!-- tabs:start -->

### **Python**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
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
```

<!-- tabs:end -->
