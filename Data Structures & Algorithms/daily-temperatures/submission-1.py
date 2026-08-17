class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        i = 0
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([t, i])

        return result