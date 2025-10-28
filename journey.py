n, a, b,c=map(int,input().split())
x=n//(a+b+c)
w=n%(a+b+c)
if w==0:
    print(3*x)
elif w-a<=0:
    print(3*x+1)
elif w-a-b<=0:
    print(3*x+2)
elif w-a-b-c<=0:
    print(3*x+3)
