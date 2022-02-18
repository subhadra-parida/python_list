#students marks less than 50=
marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
x=len(marks)
index=0
less50=0
more50=0
while index<x:
	result=marks[index]
	if result<50:
		less50=less50+1
	else:
		more50=more50+1
	index=index+1
print("marks more than 50="+str(more50))
print("marks more than 50="+str(less50))