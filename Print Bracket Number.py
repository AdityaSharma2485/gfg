class Solution:
    def bracketNumbers(self, str):
        stack = []
        counter = 0
        result = []
        
        for char in str:
            if char == '(':
                counter += 1
                stack.append(counter)
                result.append(counter)
            elif char == ')':
                result.append(stack.pop())
        
        return result
