class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0: return 0
        count = 0
        mem = 0

        for i in range(len(s)):
            if s[i] != " ":
                count += 1
                mem = count
            elif s[i] == " ":
                count = 0
        return mem