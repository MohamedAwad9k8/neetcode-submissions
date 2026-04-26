class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            nums_sum = 1
            for j in range(len(nums)):
                print(i, j)
                if j == i:
                    continue
                if nums[j] == 0:
                    nums_sum = 0
                    break
                nums_sum *= nums[j]

            res.append(nums_sum)
        return res