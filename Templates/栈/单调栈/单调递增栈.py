#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/14 11:22
# @Author :wyb
def monotoneIncreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num >= stack[-1]:
            stack.pop()
        stack.append(num)

def monotoneDecreasingStack(nums):
    stack = []
    for num in nums:
        while stack and num<=stack[-1]:
            stack.pop()
        stack.append(num)