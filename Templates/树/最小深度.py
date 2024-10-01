#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 14:09
# @Author :wyb
# 层序遍历
class Solution:
    def minDepth(self,root):
        if not root:
            return 0
            que = deque()
            que.append(root)
            res =1
            while que:
                for _ in range(len(que)):
                    node = que.popleft()
                    if not node.left and not node.right:
                        return res
                    if node.left is not None:
                        que.append(node.left)
                    if node.right is not None:
                        que.append(node.right)
                res+=1
            return res

# 递归
class solution:
    def minDepth(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10 ** 9
        if root.left:
            min_depth =min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.left), min_depth)
        return min_depth+1