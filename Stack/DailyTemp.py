class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # stack with index of the largest element when decreasing down the array

        stack = []
        array = [0] * len(temperatures)
        

        for i in range(len(temperatures) - 1, -1, -1):
            
            if not stack:
                array[i] = 0
            elif temperatures[stack[-1]] > temperatures[i]:
                array[i] = stack[-1] - i
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                
                if stack:
                    array[i] = stack[-1] - i
                else:
                    array[i] = 0
                
            stack.append(i)
        
        return array
