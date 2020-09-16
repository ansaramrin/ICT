from math import sqrt

gravity = 9.8
height = float(input("Height from which object is dropped (in meters): "))

velocity = sqrt(2 * gravity * height)

print("Object will hit the ground at:" ,velocity,"m/s")