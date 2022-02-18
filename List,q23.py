list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[ ]
count=0
while i<len(list):
	if list[i] in list:
		a.append(list[i])
		count=count+list[i]
		i=i+1
print(a)
print(count)