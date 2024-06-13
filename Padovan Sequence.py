class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7
        
        if n == 0 or n == 1 or n == 2:
            return 1
        
        # Initial values for P(0), P(1), P(2)
        P0, P1, P2 = 1, 1, 1
        
        for i in range(3, n + 1):
            Pn = (P0 + P1) % MOD
            P0, P1, P2 = P1, P2, Pn
        
        return P2
