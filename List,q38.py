###Write a python program to concatenate element wise 3 given list...
a=['0','1','2','3','4']
b=["red","green","black","blue","white"]
c=['100','200','300','400','500']
i=0
d=[ ]
while i<len(a) and len(b) and len(c):
	e=a[i]+b[i]+c[i]
	d.append(e)
	i=i+1
print(d)