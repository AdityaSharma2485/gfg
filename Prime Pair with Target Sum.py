from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        if n < 4:
            return [-1, -1]
        
        # Step 1: Generate all prime numbers up to n using Sieve of Eratosthenes
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
        
        for start in range(2, int(n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start * start, n + 1, start):
                    sieve[multiple] = False
        
        # Step 2: Find the pair of primes that sum to n
        for a in range(2, n):
            if sieve[a] and sieve[n - a]:
                return [a, n - a]
        
        # If no such pair is found
        return [-1, -1]
