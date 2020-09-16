import math
from math import pi
n=int(input("Enter the side: "))
s=int(input("Enter the length: "))
area=n* (s * s) / (4.0 * math.tan(pi / n))
print("Area of a regular polygon is:",area)