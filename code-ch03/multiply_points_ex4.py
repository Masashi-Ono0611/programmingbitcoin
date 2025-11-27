from ecc import FieldElement, Point

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

# (n, (x, y)) の形で Exercise 4 の対象を列挙
multiplications = [
    (2, (192, 105)),
    (2, (143, 98)),
    (2, (47, 71)),
    (4, (47, 71)),
    (8, (47, 71)),
    (21, (47, 71)),
]

for n, (x_raw, y_raw) in multiplications:
    x = FieldElement(x_raw, prime)
    y = FieldElement(y_raw, prime)
    p = Point(x, y, a, b)

    result = n * p

    if result.x is None and result.y is None:
        print(f"{n}*({x_raw}, {y_raw}) = infinity")
    else:
        print(
            f"{n}*({x_raw}, {y_raw}) = "
            f"({result.x.num}, {result.y.num})"
        )
