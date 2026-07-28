class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = []

        while(i < len(s)):
            if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(s[i])
            elif(len(stack) == 0):
                return False
            elif(s[i] == ")" and stack.pop() != "("):
                return False
            elif(s[i] == "]" and stack.pop() != "["):
                return False
            elif(s[i] == "}" and stack.pop() != "{"):
                return False
                
            i += 1

        if(stack):
            return False
        return True