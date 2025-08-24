#!/usr/bin/python3

num = int(input("Enter a number to find the factorial of that number"))


nu = []

while num > 0:
	nu.append(num)
	num -= 1
	
ft = 1
for i in nu:
	ft *= i
print(ft)









