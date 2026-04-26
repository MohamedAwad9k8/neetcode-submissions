class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr = []
        max_arr = []
        i = 0
        # Store Min and Max Values from each array in two arrays, one for min_values and one for max_values
        for array in arrays:
            array.sort()
            n = len(array)

            min_arr.append(array[0])
            max_arr.append(array[n-1])
            
            i += 1

        # Compare the two possible values, and choose the most optimal (greedy algorithm)
        possible_max_distance = (self.check_from_max(max_arr, min_arr), self.check_from_min(max_arr, min_arr))
        return max(possible_max_distance)


    def check_from_max(self, max_arr, min_arr):    
        # Get Max Number "a"
        max_num = max(max_arr)

        # Eliminate corrosponding value from min_arr to avoid picking value from the same array
        arr_index = max_arr.index(max_num)
        poped_value = min_arr.pop(arr_index)

        # Get Min Number "b"
        min_num = min(min_arr)

        # re-add the value removed from array
        min_arr.insert(arr_index, poped_value)

        return max_num - min_num
        
    def check_from_min(self, max_arr, min_arr):
        # Get Min Number "b"
        min_num = min(min_arr)

        # Eliminate corrosponding value from max_arr to avoid picking value from the same array
        arr_index = min_arr.index(min_num)
        poped_value = max_arr.pop(arr_index)

        # Get Max Number "a"
        max_num = max(max_arr)

        # re-add the value removed from array
        max_arr.insert(arr_index, poped_value)

        return max_num - min_num
