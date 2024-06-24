class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ls = [1] * length
        rs = [1] * length

        prev = 1

        for i in range(length):
            ls[i] = prev
            prev = prev * nums[i]

        prev = 1

        for i in range(length-1, -1, -1):
            rs[i] = prev
            prev = prev * nums[i]

        total = [1] * length

        for i in range(len(nums)):
            total[i] = ls[i] * rs[i]

        return total