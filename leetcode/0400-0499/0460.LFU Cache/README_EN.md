# [460. LFU Cache](https://leetcode.com/problems/lfu-cache)

[中文文档](/leetcode/0400-0499/0460.LFU%20Cache/README.md)

## Description

<p>Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache.</p>

<p>Implement the&nbsp;<code>LFUCache</code> class:</p>

<ul>
	<li><code>LFUCache(int capacity)</code> Initializes the object with the <code>capacity</code> of the data structure.</li>
	<li><code>int get(int key)</code> Gets the value&nbsp;of the <code>key</code> if the <code>key</code> exists in the cache.&nbsp;Otherwise, returns <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Sets or inserts the value if the <code>key</code> is not already present. When the cache reaches its <code>capacity</code>, it should invalidate the least frequently used item before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), <strong>the least recently</strong> used <code>key</code> would be evicted.</li>
</ul>

<p><strong>Notice&nbsp;that</strong> the number of times an item is used is the number of calls to the&nbsp;<code>get</code>&nbsp;and&nbsp;<code>put</code>&nbsp;functions for that item since it was inserted. This number is set to zero when the item is removed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LFUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

<strong>Explanation</strong>
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);
lfu.put(2, 2);
lfu.get(1);      // return 1
lfu.put(3, 3);   // evicts key 2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.put(4, 4);   // evicts key 1.
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
lfu.get(4);      // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;=&nbsp;capacity, key, value &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you do both operations in <code>O(1)</code> time complexity?<span style="display: none;">&nbsp;</span>

## Solutions

<!-- tabs:start -->

### **Python3**

```python

```

<!-- tabs:end -->
