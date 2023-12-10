class Solution:
    """
    将数组分为两个区间：左侧为有序区间，右侧为无序区间。每趟从无序区间取出一个元素，然后将其插入到有序区间的适当位置。
    1.时间复杂度O(n*n)
    2.空间复杂度O(1)
    """
    def insertionSort(self, nums: [int]) -> [int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的所有元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp

        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.insertionSort(nums)
    
print(Solution().sortArray([5, 2, 3, 6, 1, 4]))



class SolutionWork:
    def insertSort(self, nums:[int])->[int]:
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            while j>0 and nums[j - 1]>temp:
                nums[j] = nums[j - 1]
                j-=1
            nums[j] = temp
        return nums

    def sortArray(self, nums: [int]) -> [int]:
        return self.insertionSort(nums)

print(SolutionWork().sortArray([5, 2, 3, 6, 1, 4]))
