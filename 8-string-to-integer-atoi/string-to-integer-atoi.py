
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        n = len(s)
        i = 0

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Determine sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits and check overflow
        num = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Check overflow before multiplying by 10
            if num > INT_MAX // 10 or (
                num == INT_MAX // 10 and digit > 7
            ):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        # Step 4: Apply sign
        return sign * num
