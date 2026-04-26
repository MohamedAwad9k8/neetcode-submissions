class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(len(nums))
        for i in range(len(nums)):
            print(f"new iteration: i = {i}")
            if i == 0:
                print(f"i = {i}, skipping")
                continue
            if nums[i] == nums[i-1]:
                print(f"current iterator is {i}, previous iterator is {i-1}")
                print(f"current num is {nums[i]}, previous num is {nums[i-1]}")
                return True
        return False
     


# Solution 1: Sorting then compare each value with previous value


# Solution 2: Hash Set, check if number inside return true, else put number continue
# {
#     hs_nums = set()
#         for num in nums:
#             if num in hs_nums:
#                 return True
#             else:   
#                 hs_nums.add(num)
#         return False
# }

# Solution 3: Initialize Hash Set from input array, and compare lengths 
# {
#     hs_nums = set(nums)
#         return len(hs_nums) < len(nums)
# }