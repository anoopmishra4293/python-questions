P = input("Enter Principle amount:  ")
P = int(P)

R = input("Enter Rate of intrest:  ")
R = int(R)

T = input("Enter Time span:  ")
T = int(T)

A = P*(1 + R/100)**T
I = A-P
print("Intrest is ", I)
print("Total Amount with intrest is", A)
