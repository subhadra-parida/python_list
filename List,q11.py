###Write a code that prints the minimum in this list...
numbers=[50,40,26,70,56,12,10,90,7]
i=0
max=0
while i<len(numbers):
	if max<numbers[i]:
		max=numbers[i]
	elif max>numbers[i]:
		max=numbers[i]
	i=i+1
print(max)