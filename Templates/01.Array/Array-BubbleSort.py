class Solution:
    def bubbleSort(self, nums: [int]) -> [int]:
        # 第 i 趟「冒泡」
        for i in range(len(nums) - 1):
            flag = False    # 是否发生交换的标志位
            # 对数组未排序区间 [0, n - i - 1] 的元素执行「冒泡」
            for j in range(len(nums) - i - 1):
                # 相邻两个元素进行比较，如果前者大于后者，则交换位置
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
            if not flag:    # 此趟遍历未交换任何元素，直接跳出
                break
        
        return nums
    
    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)



class SolutionWork:
    """冒泡排序

    迭代n次，每次通过交换相邻元素，将未排序部分的最大值移动到最后，
    1.时间复杂度平均是O(n*n)
    """
    def bubbleSort(self, nums: [int])->[int]:
        # 第n排序
        for i in range(len(nums)-1):
            flag = False
            # 未排序部分
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.bubbleSort(nums)
    
# print(Solution().sortArray([5, 2, 3, 6, 1, 4]))
print(SolutionWork().sortArray([5, 2, 3, 6, 1, 4]))