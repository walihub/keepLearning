# [197. 上升的温度](https://leetcode-cn.com/problems/rising-temperature)

[English Version](//leetcode/0100-0199/0197.Rising%20Temperature/README_EN.md)

## 题目描述

<!-- 这里写题目描述 -->

<div class="original__bRMd">
<div>
<p>表 <code>Weather</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id 是这个表的主键
该表包含特定日期的温度信息</pre>

<p> </p>

<p>编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 <code>id</code> 。</p>

<p>返回结果 <strong>不要求顺序</strong> 。</p>

<p>查询结果格式如下例：</p>

<pre>
<code>Weather</code>
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+

Result table:
+----+
| id |
+----+
| 2  |
| 4  |
+----+
2015-01-02 的温度比前一天高（10 -> 25）
2015-01-04 的温度比前一天高（20 -> 30）
</pre>
</div>
</div>


## 解法

<!-- 这里可写通用的实现逻辑 -->

<!-- tabs:start -->

### **Python**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python

```

<!-- tabs:end -->
