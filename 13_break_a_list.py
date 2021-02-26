my_list = ['geeks', 'for', 'geeks', 'like', 'geeky', 'nerdy', 'geek', 'love', 'questions', 'words', 'life']

#print(len(my_list))

n=5

for i in range (0,len(my_list)//n): #0,1, [0:5], [5:10] [i*n,(i+1)*n]
    print(my_list[i*n:(i+1)*n])

if len(my_list)%n !=0:
    i=len(my_list)//n
    print(my_list[i*n:])

