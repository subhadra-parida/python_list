### Given two arrays 1,2,3,4,5,6 and 2,3,1,0,6,7 find which numbers are not present in second array..  
list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
list=[ ]
i=0
while i<len(list1):
	if list1[i] not in list2:
		list.append(list1[i])
	i=i+1
print(list)