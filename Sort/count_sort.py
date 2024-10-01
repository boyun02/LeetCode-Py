#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/4 9:30
# @Author :wyb
class Solution:
    def countingSort(self, nums):
        """计数排序
        统计最大值到最小值区间，每个元素出现次数， 将每个元素放到正确的位置。
        时间复杂度：O(k)
        空间复杂度：
        统计适用排序：统计排序一般用于整数排序情况，非用于按字母顺序、人名顺序排序。
排序稳定性：由于向结果队列中填充元素时采用逆序遍历，可以避免改变元素之间的相对顺序。因此，计数排序是一种稳定排序算法。
        """
        nums_min,nums_max = min(nums), max(nums)
        size = nums_max - nums_min +1
        counts = [0 for _ in range(size)]

        for num in nums:
            counts[num - nums_min] +=1

        for i in range(1, size):
            counts[i] += counts[i-1]

        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            res[counts[num - nums_min]-1]= num
            counts[nums[i]-nums_min]-=1

        return res
