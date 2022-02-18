### Count inque values inside a list...input=[1,2,2,5,8,4,4,8]
#count=5# because [1,2,5,8,4] are inque values...
input=[1,2,2,5,8,4,4,8]
i=0
a=[ ]
count=0
while i<len(input):
	if input[i] not in a:
		a.append(input[i])
		count=count+1
	i=i+1
print(count)
print(a)