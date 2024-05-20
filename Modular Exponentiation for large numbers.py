class Solution:
	def PowMod(self, x: int, n: int, M: int) -> int:
        result = 1
        x = x % M  # Handle the case when x is greater than M

        while n > 0:
            # If n is odd, multiply x with the result
            if n % 2 == 1:
                result = (result * x) % M

            # n must be even now
            n = n >> 1  # Divide n by 2
            x = (x * x) % M  # Square x and take mod M

        return result
