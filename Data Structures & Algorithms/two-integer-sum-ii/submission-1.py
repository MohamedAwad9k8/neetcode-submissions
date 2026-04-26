class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            indx = i+1
            val = numbers[i]
            diff = target - val
            if diff in seen:
                return [seen[diff], indx]
            else:
                seen[val] = indx