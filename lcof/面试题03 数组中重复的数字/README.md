# [面试题03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)

## 题目描述

<!-- 这里写题目描述 -->

<p>找出数组中重复的数字。</p>

<p><br>
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
[2, 3, 1, 0, 2, 5, 3]
<strong>输出：</strong>2 或 3 
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>2 &lt;= n &lt;= 100000</code></p>


## 解法

<!-- 这里可写通用的实现逻辑 -->

<!-- tabs:start -->

### **Python**

<!-- 这里可写当前语言的特殊实现逻辑 -->
`一个萝卜一个坑`的思路，题目中给出`n`个数字的范围在`0～n-1`之间，如果数组中没有重复元素，
那么所有元素排序之后索引与元素相等`i=num`。遍历数组，当`i!=num`时，
如果当前元素与它索引位置相等，则是重复元素；否则将该元素与其索引位置交换，放到元素索引位置，继续遍历。
```python
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[i] = nums[temp]
                    nums[temp] = temp
        return -1
```

`hash方法`，利用hash表检查元素是否重复。
```python
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return num
            else:
                nums_map[num] = 1
        return -1
```
<!-- tabs:end -->
