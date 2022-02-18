###List product excluding duplicates...
###list=[6,1,3,5,6,3,1] o/p=60
list=[6,2,5,6,1]
i=0
a=[ ]
p=1
while i<len(list):
	if list[i] not in a:
		a.append(list[i])
		p=p*list[i]
	i=i+1
print(a)
print(p)