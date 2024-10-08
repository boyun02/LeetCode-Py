#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 10:38
# @Author :wyb
class solution:
    def isPalindrome(self, s):
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n-1

        while left < right:
            if sgood[left]!= sgood[right]:
                return False
            left, right = left+1,right-1

            return True