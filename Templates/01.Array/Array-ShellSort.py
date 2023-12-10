class Solution:
    """希尔排序
      将整个数组切按照一定的间隔取值划分为若干个子数组，每个子数组分别进行插入排序。然后逐渐缩小间隔进行下一轮划分子数组和对子数组进行插入排序。直至最后一轮排序间隔为
    ，对整个数组进行插入排序。
    """
    def shellSort(self, nums: [int]) -> [int]:
        size = len(nums)
        gap = size // 2
        # 按照 gap 分组
        while gap > 0:
            # 对每组元素进行插入排序
            for i in range(gap, size):
                # temp 为每组中无序数组第 1 个元素
                temp = nums[i]
                j = i
                # 从右至左遍历每组中的有序数组元素
                while j >= gap and nums[j - gap] > temp:
                    # 将每组有序数组中插入位置右侧的元素依次在组中右移一位
                    nums[j] = nums[j - gap]
                    j -= gap
                # 将该元素插入到适当位置
                nums[j] = temp
            # 缩小 gap 间隔
            gap = gap // 2
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.shellSort(nums)
    
print(Solution().sortArray([7, 2, 6, 8, 0, 4, 1, 5, 9, 3]))