#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 13:19
# @Author :wyb
class Solution:
    """插入排序
    将数组左侧分为已排序区间，右侧分为未排序区间，每次从未排序去区间拿一个元素，插入到已排序区间适当位置
    最佳时间复杂度：O(n),总比较次数为n-1
    最坏时间复杂度：O(n^2),总比较次数为n(n-1)/2
    平均时间复杂度：O(n^2),
    空间复杂度：O(1)
    排序稳定性：在插入过程操作中，每次都讲元素插入到相邻元素的相对顺序，并且不会改变相邻元素的相对顺序。因此，插入排序方法是一种稳定排序算法。
    """
    def insertionSort(self, nums):
        for i in range(1,len(nums)):
            temp = nums[i]
            j = i
            while j>0 and nums[j-1]>temp:
                nums[j] = nums[j-1]
                j-=1

            nums[j] = temp
        return nums
nums = [1,3,2,5,4]
print(Solution().insertionSort(nums))