class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        for i in range(len(nums) - 1):
            # 记录未排序区间中最小值的位置
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.selectionSort(nums)
    
print(Solution().sortArray([5, 2, 3, 6, 1, 4]))



class SolutionWork:
    """选择排序
    将数组分为两个区间：左侧为已排序区间，右侧为未排序区间。每趟从未排序区间中选择一个值最小的元素，放到已排序区间的末尾，从而将该元素划分到已排序区间。
    1.时间复杂度 O(n*n)
    2.空间复杂度 O(1)
    """
    def selectionSort(self, nums: [int]) -> [int]:
        for i in range(len(nums) - 1):
            # 记录未排序区间中最小值的位置
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums


    def sortArray(self, nums: [int]) -> [int]:
        return self.selectionSort(nums)

print(SolutionWork().sortArray([5, 2, 3, 6, 1, 4]))


