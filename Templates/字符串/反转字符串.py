#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 10:52
# @Author :wyb
class Solution:
    def reverseString(self, s):
        i, j = 0, len(s)-1
        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1