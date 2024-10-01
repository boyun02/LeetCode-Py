#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 10:26
# @Author :wyb
class Solution:
    def reverseList(selfself,head):
        """反转链表
        临时节点记录快指针下一节点，快节点指向慢节点，慢节点等于快节点，快节点等于临时节点
        """
        pre = head
        fast = head
        node = head
        while fast.next:
            node = fast.next
            node =fast
            fast.next = pre
            pre = fast
            fast = node
        return head
