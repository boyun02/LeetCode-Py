#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/4 10:27
# @Author :wyb
class Solution:
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp

        return nums
    def bucketSort(self, nums, bucket_size=5):
        """桶排序
        将待排序元素分散到不同桶中，再对每个桶分别排序
        时间复杂度：
        空间复杂度：
        排序稳定性：桶排序的稳定性取决于桶内使用的排序算法。如果桶内使用稳定的排序算法（比如插入排序算法），并且在桶内的过程中保持某个元素的相对顺序不变，则桶排序是一种稳定排序算法。相反，则桶排序是一种静止排序算法。
        """
        nums_min, nums_max = min(nums), max(nums)
        bucket_count=(nums_max-nums_min)//bucket_size+1
        buckets = [[] for _ in range(bucket_count)]

        for num in nums:
            buckets[(num - nums_min)//bucket_size].append(num)
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)

        # 返回结果数组
        return res