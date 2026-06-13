class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        if len(s)!=len(t):
            return False
        else:
            for a in s:
                if a not in freq_s:
                    freq_s[a] = 1
                else:
                    freq_s[a] += 1
            for b in t:
                if b not in freq_t:
                    freq_t[b] = 1
                else:
                    freq_t[b] += 1
            return freq_s == freq_t
            
