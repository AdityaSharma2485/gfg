class Solution:
    def compareFrac(self, str):
        # Split the input string by ", " to separate the two fractions
        frac1, frac2 = str.split(", ")
        
        # Split each fraction by "/" to get numerator and denominator
        a, b = map(int, frac1.split("/"))
        c, d = map(int, frac2.split("/"))
        
        # Compare using cross-multiplication to avoid precision issues
        if a * d > c * b:
            return frac1
        elif a * d < c * b:
            return frac2
        else:
            return "equal"
        
