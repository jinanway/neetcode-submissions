class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        curr = []
        combos = []

        def maker(openP, closedP):
            if(openP == closedP == n):
                combos.append("".join(curr))
                return
            
            if(openP < n):
                curr.append("(")
                maker(openP + 1, closedP)
                curr.pop()

            if(closedP < openP):
                curr.append(")");
                maker(openP, closedP + 1)
                curr.pop()
        maker(0,0)
        return combos
        