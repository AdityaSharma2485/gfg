from math import gcd

class Solution:
    def InternalCount(self, p, q, r):
        def triangle_area(x1, y1, x2, y2, x3, y3):
            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

        def boundary_points(x1, y1, x2, y2):
            return gcd(abs(x2 - x1), abs(y2 - y1))
        
        p1, p2 = p
        q1, q2 = q
        r1, r2 = r
        
        # Area of the triangle multiplied by 2 to avoid fractional areas
        A = triangle_area(p1, p2, q1, q2, r1, r2)
        
        # Boundary points
        B1 = boundary_points(p1, p2, q1, q2)
        B2 = boundary_points(q1, q2, r1, r2)
        B3 = boundary_points(r1, r2, p1, p2)
        
        # Total boundary points excluding the vertices
        B = B1 + B2 + B3
        
        # Internal points using Pick's theorem
        I = (A - B + 2) // 2
        
        return I
