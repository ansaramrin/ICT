a=int(input())
b=int(input())
c=int(input())
sm_n=min(a,b,c)
lar_n=max(a,b,c)
mid_n=a+b+c-lar_n-sm_n
print(sm_n,mid_n,lar_n)