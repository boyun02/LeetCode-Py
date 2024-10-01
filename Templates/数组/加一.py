#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/1 11:15
# @Author :wyb
class Solution(object):
    def plusOne(self, digits):
        """从末尾开始反向遍历数组，进位标志初始值设为1， 每个元素等于元素加进位标志取余，进位标志取整，最后判断进位标志是否为1，为1则在最前面插入1
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        carry = 1
        for i in range(n):
            temp = (digits[n-i-1]+carry)%10
            carry = (digits[n-i-1]+carry)/10
            digits[n-i-1] = temp
        if carry==1:
            digits.insert(0,1)
        return digits

