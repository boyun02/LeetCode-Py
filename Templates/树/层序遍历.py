#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 13:24
# @Author :wyb
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(level)
        return order
