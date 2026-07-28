class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while(len(s) - 1 >= i):
            if(s[i] == '(' or  s[i] == '[' or  s[i] == '{'):
                stack.append(s[i])
            elif(s[i] == ')'):
                if(len(stack) == 0 or stack.pop() != '('):
                    return False
            elif(s[i] == ']'):
                if(len(stack) == 0 or stack.pop() != '['):
                    return False
            elif(s[i] == '}'):
                if(len(stack) == 0 or stack.pop() != '{'):
                    return False
            i += 1

        if(len(stack) != 0):
            return False
        

        return True