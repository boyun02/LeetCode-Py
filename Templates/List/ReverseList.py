#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/12/25 21:18
# @Author :wyb
class Solution():
    def reverseList(self, head):
        """反转链表

        """
        fast = head
        slow = None
        while fast:
            tmp = fast.next
            fast.next = slow
            slow = fast
            fast = tmp
        return fast