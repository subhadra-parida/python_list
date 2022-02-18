###Write a code that prints the second  maximum in this list...
numbers=[50,40,26,70,56,12,10,90,7]
i=0
max=0
max2=0
while i<len(numbers):
	if numbers[i]>max:
		max=numbers[i]
	if max2<numbers[i]<max:
		max2=numbers[i]
	i=i+1
print(max2)