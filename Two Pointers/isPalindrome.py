class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for i in s:
            if i.isalnum():
                array.append(i.lower())

        lp = 0
        rp = len(array) - 1

        while lp < rp:
            if array[lp] != array[rp]:
                return False
            lp += 1
            rp -= 1
        
        return True