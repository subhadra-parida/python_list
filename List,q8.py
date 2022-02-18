#Write a code that counts the numbers between 29 and 40 and then print its count?
numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(numbers):
	if 20<numbers[i]and 40>numbers[i]:
		count=count+1
	i=i+1
print(count)