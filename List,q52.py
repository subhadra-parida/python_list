###How it will be separated & print a string....
#['I',' ','L','o','v','e',' ','Y','o','u',' ','T','o','o'...]
a="I Love You Too"
b=[ ]
i=0
while i<len(a):
	b.append(str(a[i]))
	i=i+1
print(b)