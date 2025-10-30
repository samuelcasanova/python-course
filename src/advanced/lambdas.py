from functools import reduce

points2D = [(1, 2), (3, 4), (5, 6)]
to_print = list(map(lambda point: f"Point(x={point[0]}, y={point[1]})", points2D))
print(to_print)

sorted_points = sorted(points2D, key=lambda point: point[0])
print("Sorted points by x-coordinate:", sorted_points)

filtered_points = list(filter(lambda point: point[0] + point[1] > 5, points2D))
print("Filtered points where x + y > 5:", filtered_points)

reduced_sum = reduce(lambda acc, point: acc + point[0] + point[1], points2D, 0)
print("Sum of all coordinates:", reduced_sum)
