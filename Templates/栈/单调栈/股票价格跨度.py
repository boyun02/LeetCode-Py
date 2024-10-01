#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/14 12:37
# @Author :wyb
class StockSpanner(object):

    def __init__(self):
        self.stack = [(0, inf)]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 0
        while self.stack and self.stack[-1][1] <= price:
            ans += self.stack.pop()[0]
        self.stack.append((ans + 1, price))
        return ans + 1
