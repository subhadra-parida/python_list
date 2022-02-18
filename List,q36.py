### How to define even and odd in a list...
list=[14,24,31,15,19,57,88,90,42,66,90]
i=0
a=[ ]
b=[ ]
while i<len(list):
	if list[i]%2==0:
		a.append(list[i])
	else:
		b.append(list[i])
	i=i+1
print(a)
print(b)
