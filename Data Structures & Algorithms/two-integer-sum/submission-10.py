class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i == j:
                    if nums.count(diff) > 1:
                        j = nums.index(diff, i+1)
                    else:
                        continue
                return [i, j]