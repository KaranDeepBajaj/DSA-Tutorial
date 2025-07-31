class Solution:
    def divide(self,dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        negative= (dividend<0) != (divisor <0)
        dividend_abs=abs(dividend)
        divisor_abs=abs(divisor)
        qoutient=0
        while dividend_abs>=divisor_abs:
            temp_divisor=divisor_abs
            multiplier=1
            while dividend_abs >=(temp_divisor<<1):
                temp_divisor<<=1
                multiplier<<=1
            dividend_abs-=temp_divisor
            qoutient+=multiplier
        if negative:
            qoutient=max(qoutient,-2**31)
        else:
            qoutient=min(qoutient,2**31-1)
        return qoutient

if __name__ == '__main__':
    obj = Solution()
    o = obj.divide(-2147483648,1)
    print(o)