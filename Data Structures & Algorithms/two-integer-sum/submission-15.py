class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict.get(target-num), i]
            num_dict[num] = i

            

# Solution 1: Use hash Table -> [key=number -> value=target-number]
# with each number check for (target-number) exists in key
# 10 -> 3, 7 -> dict row [3,7], on 7 check (10-7) -> 3 key found - > return key first, value second
# {
#             num_dict = {}
#         for num in nums:
#             diff = target - num
#             if diff in num_dict:
#                 indx1 = nums.index(diff)
#                 indx2 = nums.index(num_dict.get(diff), indx1+1)
#                 return [indx1, indx2]     
#             num_dict[num] = diff
# }

# solution 2: two nested loops, loop 1 index 1, moves from left smaller side, loop 2, index j, moves from right bigger side
# j moves till i+1 postion only.
# i moves till len-1 
# each iteration on J, check if target - num on index j = num on index i
# Assumes sorted, or needs to be sorted first