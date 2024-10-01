#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/1 11:18
# @Author :wyb
class Solution(object):
    def pivotIndex(self, nums):
        """中心下标初始值为0，左侧数之和为0，右侧数之和为所有元素和减去下标为0的元素值，像右遍历数组，左侧数之和加中下下标元素值，右侧减去
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        left, right_ = 0, sum(nums)

        while idx < len(nums):
            if left == right_-nums[idx]:
                return idx
            else:
                left += nums[idx]
                right_ -= nums[idx]
                idx += 1

        return -1