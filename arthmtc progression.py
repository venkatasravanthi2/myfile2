n,m,k=map(int,input().split())
s=0
for i in  range(1,n+1):
    s=s+(m+(i-1)*k)
print(s)
