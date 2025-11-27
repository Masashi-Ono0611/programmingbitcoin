from ecc import FieldElement, Point

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

pairs_to_add = [
    ((170, 142), (60, 139)),
    ((47, 71), (17, 56)),
    ((143, 98), (76, 66)),
]

for (x1_raw, y1_raw), (x2_raw, y2_raw) in pairs_to_add:
    x1 = FieldElement(x1_raw, prime)
    y1 = FieldElement(y1_raw, prime)
    x2 = FieldElement(x2_raw, prime)
    y2 = FieldElement(y2_raw, prime)

    p1 = Point(x1, y1, a, b)
    p2 = Point(x2, y2, a, b)

    result = p1 + p2
    if result.x is None and result.y is None:
        print(f"({x1_raw}, {y1_raw}) + ({x2_raw}, {y2_raw}) = infinity")
    else:
        print(
            f"({x1_raw}, {y1_raw}) + ({x2_raw}, {y2_raw}) = "
            f"({result.x.num}, {result.y.num})"
        )
