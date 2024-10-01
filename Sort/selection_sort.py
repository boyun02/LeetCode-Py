#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 11:19
# @Author :wyb
class Solution:
    def selectionSort(self, nums):
        """选择排序
        将数组左侧氛围已排序区间，右侧氛围未排序区间，每次从右侧选最小元素放到已排序区间末尾，也就是未排序区间最前面。
        时间复杂度：O(n^2),比较次数和初始排序状态无关，为n(n-1)/2。
        空间复杂度：O(1),为原地排序算法。
        适用情况：在空间复杂度要求较高时，可以选择排序。
        排序稳定性：由于值最小元素与未排序区间第
        一个元素的交换动作是在不相邻的元素之间进行的，因此很有可能会改变某个元素的相对顺序，因此，选择排序法是一种静止排序算法。。
        """
        for i in range(len(nums)-1):
            min_i = i
            for j in range(i+1,len(nums)):
                if nums[j]< nums[min_i]:
                    min_i = j
            if i != min_i:
                nums[i],nums[min_i] = nums[min_i], nums[i]

        return nums

nums = [1,3,2,5,4]
print(Solution().selectionSort(nums))
