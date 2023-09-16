from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
a = Point(1, 2)


print(f"{a.x = }")
print(f"{a.y = }")

print(a.index(2))
