#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 16:24
# @Author :wyb
class Solution:
    def dailyTemperatures(self,T):
        n = len(T)
        stack = []
        ans = []
        for i in range(n):
            while stack and T[i]>T[stack[-1]]:
                index = stack.pop()
                ans[index] = (i-index)
            stack.append(i)

        return ans
