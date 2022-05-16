""".
The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

# Generate one million (x, y) points. They lie in the quadrant
# x and y both lie in [0, 1)
points_inside_circle = 0
points_outside_circle = 0
for i in range(1000000):
    x = random.random()
    y = random.random()
    # Check if they lie inside the circle
    if x**2 + y**2 < 1:
        points_inside_circle += 1
# Since we considered a quadrant:
# points_inside/total_points = pi/4
print(points_inside_circle/1000000 * 4)