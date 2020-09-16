import math
t1=float(input())
g1=float(input())
t2=float(input())
g2=float(input())

distance=6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(distance)