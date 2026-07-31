class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for n in s:
            if(n == "[" or n == "(" or n == "{"):
                stack.append(n)
            if(n == "]"):
                if(len(stack) == 0 or stack.pop() != "["):
                    return False
            if(n == ")"):
                if(len(stack) == 0 or stack.pop() != "("):
                    return False
            if(n == "}"):
                if(len(stack) == 0 or stack.pop() != "{"):
                    return False
        
        if(len(stack) != 0):
            return False
        

        return True