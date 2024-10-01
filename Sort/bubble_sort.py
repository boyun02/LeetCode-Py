#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 0:11
# @Author :wyb
class Solution:
    def bubbleSort(self, nums):
        """冒泡排序
        通过多次迭代，比较和交换相邻元素，使较大元素从前面移动到后面。
        最佳时间复杂度：O(n),最好情况下秩序比较n次元素，不移动元素。
        最坏时间复杂度：O(n^2),经过n次迭代，总共进行n(n-1)/2次元素比较，因此最坏时间复杂度为O(n^2)。
        空间复杂度：O(1),冒泡排序是原地排序。
        使用情况：适用数据量小的情况，不会改变相对顺序，是一种稳定排序算法。

        """
        for i in range(len(nums)-1):
            flag = False
            for j in range(len(nums)-i -1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break
        return nums


nums = [1,3,2,5,4]
print(Solution().bubbleSort(nums))
