### How  to print table in list....
n=int(input("enyer any number="))
i=1
a=[ ]
while i<=n:
	j=1
	b=[ ]
	while j<=10:
		c=i*j
		b.append(c)
		j=j+1
	a.append(i)
	a.append(b)
	i=i+1
print(a)
