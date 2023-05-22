
new_list=[1,2,3]

#Searching
if 1 in new_list: print(True)

#or
for x in new_list:
    if x==1:
        print(new_list.index(x))
        break



#Inserting
new_list.insert(2,7)


#inserting at the end, appending (constant time)
new_list.append(34)

print(new_list)