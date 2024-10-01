#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 22:42
# @Author :wyb
class Solution:
    def reverseString(self, s):
       left = 0
       right = len(s) -1
       while left < right:
           s[left], s[right] = s[right], s[left]
           left +=1
           right -=1
           