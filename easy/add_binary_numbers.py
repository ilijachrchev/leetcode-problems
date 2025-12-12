class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = ""

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(
                a) else 0  # ord translates to ASCII so - ord("0") we ensure that we got the real int as res 5-0=5
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            result = char + result
            carry = total // 2

        if carry:
            result = "1" + result

        return result
