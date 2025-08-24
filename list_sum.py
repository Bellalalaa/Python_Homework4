#!/usr/bin/python3

lis = [1,2,3,4,5,6,7]

sumx = 0
for i in lis:
	sumx += i

#div = sumx//len(lis)
#print(div)



try:
	div = sumx//len(lis)
except ZeroDivisionError:
	print("Exception block")
else:
	print(div)
