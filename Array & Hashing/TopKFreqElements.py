from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        array = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)

        for key, v in hashmap.items():
            array[v].append(key)

        output = []

        for i in range(len(array) - 1, -1, -1):
            for r in array[i]:
                output.append(r)
                k-=1
                if k == 0:
                    return output