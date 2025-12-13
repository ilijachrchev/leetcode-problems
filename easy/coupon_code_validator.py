class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid_coupons = []

        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]

            if not active: continue
            if not b in priority: continue
            if c == "": continue

            isOk = True
            for ch in c:
                if not (ch.isalnum() or ch == '_'):
                    isOk = False
                    break

            if not isOk: continue

            valid_coupons.append((b, c))

        valid_coupons.sort(key=lambda x: (priority[x[0]], x[1]))

        return [c for (b, c) in valid_coupons]
