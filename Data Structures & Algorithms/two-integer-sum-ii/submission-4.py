class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
        
# Solution 1: brute force
# i -> outer loop from 0 to n-2 (end -1)
# j -> inner loop from i+ to n-1 (end)
# check sum

# Solution 2: two pointers
# making use of sorted property
