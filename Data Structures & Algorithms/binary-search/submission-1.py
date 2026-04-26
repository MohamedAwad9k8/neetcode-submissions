class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rec_bin_search(0, len(nums)-1, nums, target)





    def rec_bin_search(self, l, r, nums, target):
        if l > r:
            return -1
        m = l + ((r-l)//2)

        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            return self.rec_bin_search(l, r, nums, target)
        else:
            r = m - 1
            return self.rec_bin_search(l, r, nums, target)
