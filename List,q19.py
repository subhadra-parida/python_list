### how to add 4 list....
a=['1','2','3','4','5']
b=["ant","ball","cat","dog","egg"]
c=['10','20','30','40','50']
f=['12 3','23.4','65.4','34.3','45.8']
i=0
d=[ ]
while i<len(a) and len(b) and len(c) and len(f):
	e=a[i]+b[i]+c[i]+f[i]
	d.append(e)
	i=i+1
print(d)