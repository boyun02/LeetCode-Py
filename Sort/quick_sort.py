#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 14:34
# @Author :wyb
import random

import random


class Solution:
    def partition(self,nums,low,high):
        pivot = nums[low]
        i,j=low,high
        while i<j:
            while i<j and nums[j] >=pivot:
               j-=1
            while i<j and nums[i]<=pivot:
                i+=1
            nums[i],nums[j] = nums[j],nums[i]
        nums[i],nums[j]=nums[low],nums[i]
        return i

    def randomPartition(self,nums,low,high):
        """快速排序
        随机选择一个基准元素，将当前数组分成两个数组，分别执行快速排序，再合并。
        最佳时间复杂度：O(nxlogn)
        最坏时间复杂度：O(n^2)
        空间复杂度：O(log2n)
        排序稳定性：在进行哨兵划分时，基准数可能会被交换至相邻元素的右侧。，因此快速排序是一种静止排序算法。


        """
        i = random.randint(low,high)
        nums[i],nums[low]= nums[low],nums[i]
        return self.partition(nums,low,high)

    def quickSort(self, nums,low,high):
        """快速排序
        采用经典的分治策略，选择数组中某个元素作为基准数，通过一趟排序将数组分为独立的两个子数组，一个子数组中所有元素值都比基准数小，
        另一个子数组中所有元素值都比基准数大。然后再按照同样的方式递归的对两个子数组分别进行快速排序，以达到整个数组有序
        """
        if low<high:
            pivot_i = self.randomPartition(nums, low, high)
            self.quickSort(nums, low, pivot_i - 1)
            self.quickSort(nums, pivot_i+1,high)

        return nums
nums = [1,3,2,5,4]
print(Solution().quickSort(nums,0,len(nums)-1))