#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/1/28 12:23
# @Author :wyb
class Solution:
    def postorderTraversal(self, root):
        res = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.apped(root.val)
        postorder(root)
        return res