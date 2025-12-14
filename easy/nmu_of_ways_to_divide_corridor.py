class Solution:
    def numberOfWays(self, corridor: str) -> int:
        total_seats = corridor.count("S")
        if total_seats == 0: return 0
        if total_seats % 2 == 1: return 0

        seat = 0
        plant = 0
        ans = 1
        module = 10**9 + 7

        for ch in corridor:
            if ch == "S":
                if seat == 2:
                    ans = ans * (plant + 1) % module
                    seat = 0
                    plant = 0
                seat += 1
            else:
                if seat == 2:
                    plant += 1
        return ans