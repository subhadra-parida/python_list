a=[[1,2,3],[4,5,6],[6,1]]
i=0
sum=0
b=[]
while i<len(a):
    j=0
    c=[]
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
        b.append(sum)
    i=i+1
    c.append(sum)
    print(c)


