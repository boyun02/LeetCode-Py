#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 12:19
# @Author :wyb
class Solution:
    def preorderTraversal(self, root):
        res = []
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res