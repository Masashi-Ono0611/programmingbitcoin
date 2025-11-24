from ecc import FieldElement, Point

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

points_to_check = [
    (192, 105),
    (17, 56),
    (200, 119),
    (1, 193),
    (42, 99)
]

for x_raw, y_raw in points_to_check:
    x = FieldElement(x_raw, prime)
    y = FieldElement(y_raw, prime)
    try:
        p = Point(x, y, a, b)
        print(f"({x_raw}, {y_raw}) is on the curve")
    except ValueError:
        print(f"({x_raw}, {y_raw}) is NOT on the curve")
