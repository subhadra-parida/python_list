###How to print [[ ],[1,2],[1,2,3],[1,2,3,4].....]
num=int(input("enter a no="))
i=1
a=[ ]
while i<=num:
	j=1
	b=[ ]
	if i==1 and j==1:
		a.append(b)
	else:
		while j<=i:
			b.append(j)
			j=j+1
		a.append(b)
	i=i+1
print(a)