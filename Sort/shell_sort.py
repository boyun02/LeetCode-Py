#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 13:25
# @Author :wyb
class Solution:
    """希尔排序
    将整个数组切按照一定的间隔取值划分为若干个子数组，每个子数组分别进行插入排序。然后逐渐缩小间隔进行下一轮划分子数组和对子数组进行插入排序
    。直至最后一轮排序间隔为 1m对整个数组进行插入排序。

    """
    def shellSort(self, nums):
        size = len(nums)
        gap = size//2
        while gap>0:
            for i in range(gap,size):
                temp = nums[i]
                j = i
                while j >= gap and nums[j-gap]>temp:
                    nums[j] = nums[j-gap]
                    j-= gap

                nums[j]=temp
            gap = gap//2

        return nums
nums = [1,3,2,5,4]
print(Solution().shellSort(nums))