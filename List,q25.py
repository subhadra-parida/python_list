###Aao Jodein........
mark=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c1=1
c2=0
sum1=0
sum2=0
while i<len(mark):
	if mark[i]%2==0:
		c1=c1+1
		sum1=sum1+mark[i]
	else:
		c2=c2+1
		sum2=sum2+mark[i]
	i=i+1
print(sum1,"even")
print(sum2,"odd")