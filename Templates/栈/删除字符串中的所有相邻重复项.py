#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 16:10
# @Author :wyb
class Solution:
    def removeDuplicates(self,s):
        """删除字符串中的所有相邻重复项

        """
        stack = []
        for cha in s:
            if stack and cha == stack[-1]:
                stack.pop()
            else:
                stack.append(cha)

        return "".join(stack)