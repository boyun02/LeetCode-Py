#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/12/24 11:57
# @Author :wyb
arr = ['python', 'java', ['asp', 'php'], 'c']

# 访问元素
def value(nums, i):
    if 0 <= i <= len(nums) - 1:
        print(nums[i])

# 查找元素
# 从数组 nums 中查找元素值为 val 的数据元素第一次出现的位置
def find(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1

arr = [0, 5, 2, 3, 7, 1, 6]
value(arr, 3)
print(find(arr, 5))

# 插入元素
val = 4
arr.append(val)
print(arr)

# 改变元素
def change(nums, i, val):
    if 0 <= i <= len(nums) - 1:
        nums[i] = val


arr = [0, 5, 2, 3, 7, 1, 6]
i, val = 2, 4
change(arr, i, val)
print(arr)

# 删除元素
arr = [0, 5, 2, 3, 7, 1, 6]
arr.pop()
print(arr)

arr = [0, 5, 2, 3, 7, 1, 6]
arr.remove(5)
print(arr)