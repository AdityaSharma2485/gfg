class Solution:
	def binaryNextNumber(self, num):
		# Convert binary string to integer
        n = int(num, 2)
         
        # Increment integer by 1
        n += 1
         
        # Convert integer back to binary string
        result = bin(n)[2:]
         
        # Remove leading zeros
        result = result.lstrip('0')
         
        return result
