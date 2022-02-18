###Kitne aadmi the?????
mark=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c1=0
c2=0
while i<len(mark):
	if mark[i]%2==0:
		c1=c1+1
	else:
		c2=c2+1
	i=i+1
print(c1,"even")
print(c2,"odd")