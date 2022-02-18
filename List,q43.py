### a=[1,2,3,4] o)p=[[1,1],[2,2],[3,3],[4,4]]
a=[1,2,3,4]
x=[ ]
i=0
while i<len(a):
	b=[a[i],i+1]
	x.append(b)
	i=i+1
print(x)