class Solution:
    def armstrongNumber(self, n: int) -> bool:
        # Extract the digits of the number
        hundreds = n // 100
        tens = (n // 10) % 10
        units = n % 10
        
        # Calculate the sum of the cubes of the digits
        sum_of_cubes = hundreds**3 + tens**3 + units**3
        
        # Check if the sum of the cubes equals the original number
        if sum_of_cubes == n:
            return "true"
        else:
            return "false"
