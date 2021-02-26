a = []
element = int(input("enter the number of elements in list:  "))

for i in range(element):
	x=int(input())
	a.append(x)

print("orignal list is :  ",a)

b = a[0]
a[0] = a[-1]
a[-1] = b
print(a)