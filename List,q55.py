### How many letters are in the list...
text=["I am Barsha"]
i=0
while i<len(text):
	j=0
	c=0
	while j<len(text[i]):
			c=c+1
			j=j+1
	print(text[i],c)
	i=i+1