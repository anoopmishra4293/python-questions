list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# for i in range(len(list1)):
#     for j in range(len(list2)):
#         list1[i]==list2[j]

list3 = zip(list1,list2)
list4=list(list3)
list4.sort(key = lambda x: x[1])
print(list4)