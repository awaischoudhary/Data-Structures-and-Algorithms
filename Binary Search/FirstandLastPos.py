class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # binary search 
        # middle - middle is less than target?, lp = m
        # if middle is target then we check lp and rp one by one and increase/decreease to find first target


        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            i = (lp + rp)//2
            if nums[i] < target: 
                lp = i+1
            elif nums[i] > target:
                rp = i-1
            else:
                while nums[lp] != target and lp <= i:
                    lp += 1
                while nums[rp] != target and rp >= i:
                    rp-=1
                    
                return [lp, rp]


        return [-1, -1]