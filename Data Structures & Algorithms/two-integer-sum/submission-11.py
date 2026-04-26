class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_index = {} # value : index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_index:
                return [prev_index[diff], i]
            prev_index[num] = i
            