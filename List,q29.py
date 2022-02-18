#How to define First maximum number, second maximum number and third maximum number in a list
num=[10,20,30,80,40,90]
i=0
max1=0
max2=0
max3=0
while i<len(num):
	if num[i]>max1:
		max1=num[i]
	if max2<num[i]<max1:
		max2=num[i]
	if max1<max2<num[i]<max3:
		max3=num[i]
	i=i+1
print(max1)
print(max2)
print(max3) 
