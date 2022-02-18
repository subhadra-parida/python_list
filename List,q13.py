###Reverse Ordered... write a code that the reverses the ordered of the items means in opposite order...
places=["delhi","gujrat","rajasthan","punjab","kerala"]
r=[ ]
i=-1
while i>=-len(places):
	r.append(places[i])
	i=i-1
print(r)