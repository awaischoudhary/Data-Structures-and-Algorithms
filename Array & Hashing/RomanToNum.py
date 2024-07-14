class Solution:
    def romanToInt(self, s: str) -> int:
        romanToNum = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C': 100, 'D' : 500, 'M' : 1000}

        curr = 0
        for i in range(len(s)):
             # check all three cases and if not then take value from hashmap and add it to the curr
            if i + 1 < len(s) and romanToNum[s[i]] < romanToNum[s[i+1]]:
                curr -= romanToNum[s[i]]
            else:
                curr += romanToNum[s[i]]
            
        
        return curr