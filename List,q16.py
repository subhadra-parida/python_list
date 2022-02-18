###Binary to decimal....
Bnum=int(input("enter any number="))
Dnum=0
i=1
while Bnum!=0:
	rem=Bnum%10
	Dnum=Dnum+(rem*i)
	i=i*2
	Bnum=int(Bnum/10)
print(Dnum)
