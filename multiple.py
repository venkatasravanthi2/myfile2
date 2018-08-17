n=int(input())
for i in range(1,6):
    i=n*i
    if(i<6-1):
        k=' '
    else:
        k=''
    print(i,end=k)
