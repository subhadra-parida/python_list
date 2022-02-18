### wtite a program to print greater than of 20 and less than 40...
num=[50,40,23,60,22,56,39,59]
i=0
c=0
while i<len(num):
	if num[i]>20 and num[i]<40:
		c=c+1
	i=i+1
print(c)