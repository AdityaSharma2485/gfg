class Solution:
    def matchPairs(self, n, nuts, bolts):
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']
        
        # Create a mapping from character to its position in the predefined order
        order_map = {char: i for i, char in enumerate(order)}

        # Define a custom sort key that uses the order_map
        def sort_key(char):
            return order_map[char]

        # Sort the nuts and bolts arrays using the custom sort key
        nuts.sort(key=sort_key)
        bolts.sort(key=sort_key)
