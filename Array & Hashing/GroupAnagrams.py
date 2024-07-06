from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord("a")] += 1
            
            hashmap[tuple(count)].append(s)
        
        return hashmap.values()