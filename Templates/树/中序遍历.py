#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 12:21
# @Author :wyb
class Solution:
    def inorderTraversal(self, root):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res