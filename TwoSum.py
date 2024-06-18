from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return [i, hashtable[nums[i]]] 
            hashtable[target-nums[i]] = i
