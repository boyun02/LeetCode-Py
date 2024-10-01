#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 16:13
# @Author :wyb
class Solution:
    def isValid(self, s):
        dict = {')':'(','}':'{',']':'['}
        stack = []
        for cha in s:
            if stack and  cha in dict:
                if stack[-1]==dict[cha]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cha)
            return not stack