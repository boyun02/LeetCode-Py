#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/1 10:57
# @Author :wyb
class Solution(object):
    def rotate(self, nums, k):
        """将后k个元素移动到最前面
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法1
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]

