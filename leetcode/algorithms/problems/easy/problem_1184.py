from typing import List

url = "https://leetcode.com/problems/distance-between-bus-stops/description/"


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        distance_length = len(distance)
        clockwise_distance = 0
        counterclockwise_distance = 0

        clockwise_index = start
        while clockwise_index != destination:
            clockwise_distance += distance[clockwise_index]
            clockwise_index = (clockwise_index + 1) % distance_length

        counterclockwise_index = start
        while counterclockwise_index != destination:
            counterclockwise_distance += distance[counterclockwise_index - 1]
            counterclockwise_index = (
                (counterclockwise_index - 1) % distance_length
            )

        return min(clockwise_distance, counterclockwise_distance)


print(Solution().distanceBetweenBusStops([1, 2, 3, 4], 0, 3))
