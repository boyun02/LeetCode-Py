#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/12/10 0:56
# @Author :wyb
class solution:
    def bubbleSort(self, nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)


if __name__ == '__main__':
    print(solution().sortArray([1, 3, 2]))
