import math

def triangle_square(x, y, z):
    per = (x + y + z) / 2
    square = math.sqrt(per * (per - x) * (per - y) * (per - z))
    return square