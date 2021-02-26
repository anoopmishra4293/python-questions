list1 = [10, 20, 30, 20, 30, 40, 20, 50, -20, 60, 60, -20,]
s =set([])
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if(list1[i] == list1[j]):
            b=list1[j]
            s.add(b)

print(list(s))