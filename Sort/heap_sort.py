#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/4 0:58
# @Author :wyb
class MaxHeap:
    def __buildMaxHeap(self, nums: [int]):
        size = len(nums)
        # 先将数组 nums 的元素按顺序添加到 max_heap 中
        for i in range(size):
            self.max_heap.append(nums[i])

        # 从最后一个非叶子节点开始，进行下移调整
        for i in range((size - 2) // 2, -1, -1):
            self.__shift_down(i, size)
    def maxHeapSort(self, nums):
        """
        时间复杂度：
        空间复杂度：
        排序稳定性
        """
        self.buildMaxHead(nums)
        size = len(self.max_heap)
        for i in range(size-1,-1,-1):
            self.max_heap[0], self.max_heap[i] = self.max_heap[i], self.max_heap[0]
            self._shift_down(0,i)

        return self.max_heap()