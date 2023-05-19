import math
def binary_search(list,target):
    #my implementation
    # myList=list
    # myList.sort()
    # midValue=None;
    # newList=myList
    #
    # while len(newList)>0:
    #     midValue=newList[math.floor(len(newList) / 2)]
    #     if midValue==target:
    #         return myList.index(midValue)
    #     else:
    #         if midValue>target:
    #             newList = newList[0:newList.index(midValue)]
    #         else:
    #             newList= newList[newList.index(midValue)+1:]
    # return None
    first=0
    last= len(list)-1

    while first<=last:
        midpoint=(first+last)//2
        if list[midpoint]==target:
            return midpoint
        elif list[midpoint<target]:
            first=midpoint+1
        else:
            last=midpoint-1
    return None


def verifyResult(result):
    if result is not None:
        print(f"The value was found at index {result}")
    else:
        print("The value was not found on the list provided")



numbers=[1,2,3,4,5,6,7,8,9,10]
verifyResult(binary_search(numbers,10))


