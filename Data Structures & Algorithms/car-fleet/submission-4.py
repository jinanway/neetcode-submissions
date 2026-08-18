class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort()
        cars.reverse()
        stack = []
        for c in cars:
            time = (target - c[0]) / c[1]
            if (not stack or stack[-1] < time):
                stack.append(time)
        

        return len(stack)