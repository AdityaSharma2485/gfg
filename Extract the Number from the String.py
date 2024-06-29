class Solution:
    def ExtractNumber(self, sentence):
        # Split the sentence into tokens (words and numbers)
        tokens = sentence.split()
        
        # Variable to store the largest number found that does not contain '9'
        largest_number = -1
        
        # Iterate through each token
        for token in tokens:
            # Check if the token is a number and does not contain '9'
            if token.isdigit() and '9' not in token:
                # Convert the token to an integer
                number = int(token)
                # Update the largest number found
                if number > largest_number:
                    largest_number = number
        
        return largest_number
