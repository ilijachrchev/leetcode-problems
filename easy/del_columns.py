class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        rows = len(strs)
        columns = len(strs[0])

        for i in range(columns):
            for j in range(rows - 1):
                if strs[j][i] > strs[j+1][i]:
                    counter += 1
                    break
        return counter