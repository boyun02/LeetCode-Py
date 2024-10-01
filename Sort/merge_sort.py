#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/5/3 13:46
# @Author :wyb
class Solution:
    def merge(self, left_nums, right_nums):
        """归并排序
        将当前数组从中间位置分成两份，分别执行归并排序，然后再合并
        时间复杂度：O(nxlogn),归并排序算法的时间复杂度等于归并趟数与每一趟归并的时间复杂度乘积。子算法merge(left_nums, right_nums):的时间复杂度是
，因此，归并排序算法总的时间复杂度为O(nxlogn)。
        空间复杂度：归并排序方法需要占用与参加排序的内存同样大小的辅助空间。因此，算法的空间复杂度为O(n)。
        排序稳定性：因为在这两个队列中的归并并行过程中，如果两个队列中出现恰好的元素，merge(left_nums, right_nums):算法能够使前一个队列中的某个元素先被复制，从而保证这两个元素的相对关系顺序不会发生改变。因此，归并排序算法是一种稳定排序算法。
        """
        nums=[]
        left_i, right_i = 0,0
        while left_i <len(left_nums)and right_i < len(right_nums):
            # 将两个有序子数组中较小元素依次插入到结果数组中
            if left_nums[left_i] < right_nums[right_i]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_i])
                right_i += 1

            # 如果左子数组有剩余元素，则将其插入到结果数组中
        while left_i < len(left_nums):
            nums.append(left_nums[left_i])
            left_i += 1

            # 如果右子数组有剩余元素，则将其插入到结果数组中
        while right_i < len(right_nums):
            nums.append(right_nums[right_i])
            right_i += 1

            # 返回合并后的结果数组
        return nums
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left_nums = self.mergeSort(nums[0:mid])
        right_nums = self.mergeSort(nums[mid:])
        return self.merge(left_nums, right_nums)


nums = [1,3,2,5,4]
print(Solution().mergeSort(nums))