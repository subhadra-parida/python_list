a=[1,2,3,4,5],[1,2],[2,3],[3,4],[4,5],[5,6]
b=[ ]
i=0
while i<len(a):
	c=[a[i],a[i+1]]
	b.append(c)
	i=i+1
print(b)