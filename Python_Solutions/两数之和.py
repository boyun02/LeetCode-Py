class Solutions:
    def towSums(self,nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
        return []
class Solutions(Solutions):
    def towSums(self, nums, target):
        numdict = dict()
        for i in range(len(nums)):
            if target-nums[i] in numdict:
                return i, numdict[target-nums[i]]
            numdict[nums[i]] = i
print(Solutions().towSums([1,2,3],5)    )

