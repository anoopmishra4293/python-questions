a = []
element = int(input("enter the number of elements in list:  "))

for i in range(element):
	x=int(input())
	a.append(x)

n = input("Enter number of largest elements you want from list : ")
n = int(n)

# first method
a.sort()
result=a[-n:]

print(result)


#second method
# b=[]

# if n < element:
#     for i in range(0,n):
#         max1 = 0

#         for j in range(len(a)):
#             if a[j] > max1:
#                 max1 = a[j]
    
#         a.remove(max1)
#         b.append(max1)
#     print(b)
