from typing import List
from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_cost = 0

        # Initialize counter object for both baskets
        _temp_b1 = Counter(basket1)
        _temp_b2 = Counter(basket2)

        # To easily check whether the baskets could be equal, we combine both baskets into one then check if even or odd
        # If even, it could be equal. Else, it could never be equal
        total_fruits = _temp_b1 + _temp_b2

        # fruits should be counted individual, not the total since there should be equal amounts of each fruit in two baskets
        for fruit_count in total_fruits.values():
            if fruit_count % 2 == 1:
                return -1

        excess_fruits = []  # stores excess fruits that need to be transferred

        for fruit, fruit_count in total_fruits.items():
            equal_count = (
                fruit_count // 2
            )  # how many fruits should be stored in each basket
            surplus = _temp_b1[fruit] - equal_count

            for _ in range(abs(surplus)):
                excess_fruits.append(fruit)

        excess_fruits.sort()  # sort excess fruits to minimize cost

        transfer_operations = (
            len(excess_fruits) // 2
        )  # 2 fruits are swapped per transfer
        min_fruit_cost = min(total_fruits.keys())  # get the fruit with the minimum cost

        for i in range(transfer_operations):
            min_cost += min(2 * min_fruit_cost, excess_fruits[i])

        return min_cost
