class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlength = 0

        for i in nums:
            if i-1 not in s:
                length = 0
                n = i
                while n in s:
                    length += 1
                    n += 1
                maxlength = max(length, maxlength)
        return maxlength
