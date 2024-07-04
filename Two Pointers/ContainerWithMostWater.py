class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lp = 0 
        rp = len(height) - 1

        area = 0

        while lp < rp:

            taller = 0
            rpTemp = rp
            lpTemp = lp
            if height[lp] < height[rp]:
                taller = lp
                lp += 1
            else:
                taller = rp
                rp -=1

            area = max(area, (rpTemp - lpTemp) * height[taller])

        
        return area