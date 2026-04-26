class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
    
        while l <= r:
            m = (l + r) // 2
            if (matrix[m][0] < target) and (matrix[m][-1] < target):
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] == target:
                return True
            if l > r:
                return False
            
            if (matrix[m][0] < target) and (matrix[m][-1] >= target):
                l2, r2 = 0, len(matrix[m])-1
                while l2 <= r2:
                    n = (l2 + r2) // 2
                    if matrix[m][n] < target:
                        l2 = n + 1
                    elif matrix[m][n] > target:
                        r2 = n - 1
                    else:
                        return True
                    if l2 > r2:
                        return False


        