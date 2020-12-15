# [923. 3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity)

[中文文档](/leetcode/0900-0999/0923.3Sum%20With%20Multiplicity/README.md)

## Description

<p>Given an integer array <code>A</code>, and an integer <code>target</code>, return the number of&nbsp;tuples&nbsp;<code>i, j, k</code>&nbsp; such that <code>i &lt; j &lt; k</code> and&nbsp;<code>A[i] + A[j] + A[k] == target</code>.</p>

<p>As the answer can be very large, return it <strong>modulo</strong>&nbsp;<code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> A = [1,1,2,2,3,3,4,4,5,5], target = 8
<strong>Output:</strong> 20
<strong>Explanation: </strong>
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> A = [1,1,2,2,2,2], target = 5
<strong>Output:</strong> 12
<strong>Explanation: </strong>
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= A.length &lt;= 3000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 100</code></li>
	<li><code>0 &lt;= target &lt;= 300</code></li>
</ul>


## Solutions

<!-- tabs:start -->

### **Python3**

```python

```

<!-- tabs:end -->