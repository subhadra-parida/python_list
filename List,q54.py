###Write an descending order...
num=[12,73,41,85,61]
i=0
while i<len(num):
    a=i
    j=i+1
    while j<len(num):
        if num[a]<num[j]:
            a=j
        j=j+1
    num[i],num[a]=num[a],num[i]
    i+=1
print(num)