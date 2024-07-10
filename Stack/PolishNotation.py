class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push every item until operator, if operator apply to top 2 then remove top 2 and push result

        stack = []

        for i in tokens:
            if i == "+":
                total = stack[-2] + stack[-1]
            elif i == "-":
                total = stack[-2] - stack[-1]
            elif i == "*":
                total = stack[-2] * stack[-1]
            elif i == "/":
                total = float(stack[-2] / stack[-1])
            else:
                stack.append(int(i))
                continue
            
            stack.pop()
            stack.pop()
            stack.append(int(total))

        
        return stack[0]
            
        
