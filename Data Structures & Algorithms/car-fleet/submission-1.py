class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 0
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(key=lambda item: (item[0], item[1]), reverse=True)
        print(cars)

        import math
        stack = []
        for car in cars:
            if len(stack) == 0:
                stack.append(car)
                
                continue

            last_car = stack[-1]
            if (target-last_car[0])/last_car[1] < (target-car[0])/car[1]:
                stack.append(car)


        return len(stack)
            








        return result