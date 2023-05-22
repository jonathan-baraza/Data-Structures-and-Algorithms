
new_list=[1,2,3]
result=new_list[0]

#Searching
if 1 in new_list: print(True)

#or
for x in new_list:
    if x==1:
        print(new_list.index(x))
        break


print(result)