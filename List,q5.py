#total makes :-
marks=[25,43,89,90,56,80]
index=0
totalmark=0
while index<len(marks):
	totalmark=marks[index]+totalmark
	index=index+1
print("totalmark"+str(totalmark))
