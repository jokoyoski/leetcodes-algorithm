''' Here’s a clear and refined version of your explanation:

---

**Problem Statement**  
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

- Each input will have exactly one solution.
- You cannot use the same element twice.
- You can return the answer in any order.

---

### Approach:

We solve this using a hash map (dictionary) to store visited numbers and their indices. For each number in the array, we calculate the difference between the target and the current number (`diff = target - num`). If the `diff` is already in the map, it means the pair exists, and we can return the indices.

---

### Example:
**Input:**  
`nums = [9, 7, 2]`, `target = 9`  

**Steps:**  
1. **First Iteration:**  
   - Current number: `9`  
   - Calculate `diff = target - num = 9 - 9 = 0`  
   - `0` is not in the map, so we add `9` with its index to the map: `{9: 0}`  

2. **Second Iteration:**  
   - Current number: `7`  
   - Calculate `diff = target - num = 9 - 7 = 2`  
   - `2` is not in the map, so we add `7` with its index to the map: `{9: 0, 7: 1}`  

3. **Third Iteration:**  
   - Current number: `2`  
   - Calculate `diff = target - num = 9 - 2 = 7`  
   - `7` is in the map (with index `1`), so we return `[1, 2]` as the result.  

---

### Final Solution:  
The indices of the two numbers that add up to the target are `[1, 2]`. '''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          map_value = { } 
          final_array = []
          for index, num in enumerate(nums):
            diff = target - num
            if diff not in map_value:
                map_value[num] = index
            else:
                final_array.append(index)
                final_array.append(map_value[diff])
                break
          return final_array