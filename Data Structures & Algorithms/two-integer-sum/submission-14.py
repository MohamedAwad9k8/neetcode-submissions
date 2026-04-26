class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for num in nums:
            print(f"new iteration: num = {num}")
            diff = target - num
            print(f"diff = {diff}")
            if diff in num_dict:
                print(f"diff found in dict: key = {diff}, value = {num_dict.get(diff)}")
                indx1 = nums.index(diff)
                indx2 = nums.index(num_dict.get(diff), indx1+1)
                return [indx1, indx2] 
            print(f"Adding new key: key = {num}, value = {diff}")
            num_dict[num] = diff
            print(num_dict)
            

# Solution 1: Use hash Table -> [key=number -> value=target-number]
# with each number check for (target-number) exists in key
# 10 -> 3, 7 -> dict row [3,7], on 7 check (10-7) -> 3 key found - > return key first, value second