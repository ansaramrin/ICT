import math
a=int(input())
b=int(input())
sum=a+b
dif=a-b
pr=a*b
quot=a//b
rem=a%b
res1=math.log10(a)
res2=a**b;

print("The sum of a and b:",sum)
print("The difference when b is subtracted from a:",dif)
print("The product of a and b:",pr)
print("The quotient when a is divided by b:",quot)
print("The remainder when a is divided by b:",rem)
print("The result of log10 a:",res1)
print("The result of a**b:",res2)