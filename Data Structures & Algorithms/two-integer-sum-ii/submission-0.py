class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for val, indx in seen:
                if val == diff:
                    return [indx, i+1]
            else:
                seen.add((numbers[i],i+1))