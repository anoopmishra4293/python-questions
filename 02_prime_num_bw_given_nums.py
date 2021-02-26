a = input("Enter first number:  ")
a = int(a)

b = input("Enter last number:  ")
b = int(b)

if a>b:
    print("Please enter a last number greater then first number")

for num in range(a,b+1):
    if num>1:
        for i in range(2,num//2):
            if (num % i) == 0:
                break
        else:
            print(num)
