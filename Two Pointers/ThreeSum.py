class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        array = set()
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i -1] == nums[i]:
                continue
            target = -1 * nums[i]
            
            hashmap = {}
            j = i + 1
            while j < len(nums):
                if nums[j] in hashmap:
                    sol = (target * -1, nums[hashmap[nums[j]]], nums[j])
                    array.add(sol)
                else:
                    hashmap[target - nums[j]] = j
                j+=1

        
        return list(array)