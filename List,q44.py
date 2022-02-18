### Write third maximum number...
n=[50,40,23,70,57,12,10]
i=0
m1=0
m2=0
m3=0
while i<len(n):
	if n[i]>m1:
		m1=n[i]
	if m2<n[i]<m1:
		m2=n[i]
	if m3<m2>n[i]<m1:
		m3=n[i]
	i=i+1
print(m1)
print(m2)
print(m3)