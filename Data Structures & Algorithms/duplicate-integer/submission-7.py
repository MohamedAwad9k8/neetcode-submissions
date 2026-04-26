class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs_nums = set(nums)
        return len(hs_nums) < len(nums)


# Solution 1: Sorting then compare each value with previous value

# Solution 2: Hash Set, check if number inside return true, else put number continue

# Solution 3: Initialize Hash Set from input array, and compare lengths 