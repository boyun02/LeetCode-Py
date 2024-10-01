#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/1 11:23
# @Author :wyb
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        遍历数组，元素为1 当前个数加一，元素为0，比较当前个数和最大个数，最大个数取最大值，当前个数设为0
        :type nums: List[int]
        :rtype: int
        """
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0

        maxCount = max(maxCount, count)
        return maxCount

