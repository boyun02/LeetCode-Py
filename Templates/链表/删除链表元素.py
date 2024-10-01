#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 10:49
# @Author :wyb
class Solution:
    def removeElement(self, head, val):
        """
        添加虚拟节点，遍历链表，删除满足条件的节点
        """
        dummy_head = ListNode
        dummy_head.next = head
        cur = dummy_head
        while(cur.next):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                return dummy_head.next