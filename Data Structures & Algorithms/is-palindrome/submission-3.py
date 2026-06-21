class Solution:
    def isPalindrome(self, s: str) -> bool:
        sn = []
        for i in s:
            if i.isalnum():
                sn.append(i.lower())
        l = 0 
        r = len(sn)-1

        while l < r:
            if sn[l] != sn[r]:
                return False
            else:
                l+=1
                r-=1
        return True