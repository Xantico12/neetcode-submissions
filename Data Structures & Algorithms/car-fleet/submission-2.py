class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carCount = len(position)
        cars = [[0,0]] * carCount

        for i in range(carCount):
            cars[i] = [position[i], speed[i]]

        carsSorted = sorted(cars, reverse=True)

        stack = [(target - carsSorted[0][0]) / carsSorted[0][1]]
        for i in range(1, carCount):
            days = (target - carsSorted[i][0]) / carsSorted[i][1]

            if days < stack[-1]:
                days = stack[-1]
                stack.append(days)
            else:
                stack.append(days)
        return len(set(stack))