#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/7 10:21
# @Author :wyb
class Solution:
    def deleteDuplicates(self, head):
        """
        遍历链表，下一节点和当前节点元素相同，当前节点指向下一节点的下一节点
        """
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head