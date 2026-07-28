class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if(val == '+'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif(val == '-'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif(val == '*'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif(val == '/'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(val))

        return stack[0]

            