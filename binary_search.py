import math


def binary_search(list,target):
    myList=list
    myList.sort()

    midValue=None;
    newList=myList

    while len(newList)>0:
        midValue=newList[math.floor(len(newList) / 2)]
        print("midValue up")
        print(midValue)
        if midValue==target:
            print("hitting this one")
            return myList.index(midValue)
        else:
            if midValue>target:
                newList = newList[0:newList.index(midValue)]

            else:
                print("mid value less than")
                newList= newList[newList.index(midValue)+1:]





        print("newList")
        print(newList)

    return None




def verifyResult(result):
    if result is not None:
        print(f"The value was found at index {result}")
    else:
        print("The value was not found on the list provided")




numbers=[1,2,3,4,5,6,7,8,9,10]

verifyResult(binary_search(numbers,10))


