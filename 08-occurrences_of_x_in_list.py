a = [15,6,7,10,12,20,10,7,10]

x = input("Enter a number to count its occurrence in list : ")
x = int(x)
count=0
for i in range(0,9):
    if x==a[i]:
        count=count+1

print(count)