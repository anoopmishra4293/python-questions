a = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]

for i , value in enumerate(a):
    if a[i]==():   # a[i] is same as value
        a.pop(i)
print(a)






# a.remove(())
# a.remove(())
# a.remove(())

# print(a)