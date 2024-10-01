#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 14:02
# @Author :wyb
# 方法1 层序遍历
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        queue = [root]
        depth = 0

        while queue:
            n= len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

# 方法2 递归
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        leftHeight = self.maxDepth(root.left)
        righrHeight = self.maxDepth(root.right)

        return max(leftHeight, righrHeight) +1
