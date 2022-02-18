list=[[5,7,9],[8,9]]
i=0
sum=0
while i<len(list):
	j=i
	while j<len(list[i]):
		sum=sum+(list[i][j])
		j+=1
	i=i+1
print(sum)