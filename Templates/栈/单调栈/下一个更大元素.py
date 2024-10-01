#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 16:01
# @Author :wyb
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """下一个更大元素

        """
        res = []
        num_map=dict()
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                num_map[stack[-1]] = num
                stack.pop()
            stack.append(num)
        for num in nums1:
            res.append(num_map.get(num, -1))
        return res

