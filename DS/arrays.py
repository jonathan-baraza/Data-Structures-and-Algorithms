
new_list=[1,2,3]

listTwo=[4,5,6]

#Searching
if 1 in new_list: print(True)

#or
for x in new_list:
    if x==1:
        print(new_list.index(x))
        break



#Inserting
new_list.insert(2,7) #linear runtime as every item is shifted until that index


#inserting at the end, appending (constant time)
new_list.append(34)



#add one list to another
new_list.extend(listTwo)


#delete
new_list.pop(1) #pop function removes last element if you haven't provided the index
new_list.remove(6) #removes the value provided not the index




#NB: insert shifts elements to the RIGHT while delete shifts elements to the LEFT. (to create and occupy index space respectively)
print(new_list)