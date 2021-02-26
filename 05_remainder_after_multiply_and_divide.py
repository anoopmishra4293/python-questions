a = []
element = int(input("enter the number of elements in list :  "))

for i in range(element):
	x=int(input())
	a.append(x)

product=1
for i in a:
	product=product*i

n = input("Enter a divisor 'n' :  ")
n = int(n)

Output = product%n
print("Output = ",Output)