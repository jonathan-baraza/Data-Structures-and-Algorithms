def linear_search(list,target):
    """
    Returns the index position of the target it found, else returns None
    """
    #answer one
    # print(list.index(target))

    #answer two
    # x=0;
    # while(x<len(list)):
    #     if(list[x]==target):
    #         break;
    #     x=x+1
    # print(x)

    #answer three
    for i in range(0,len(list)):
        if list[i]==target:
            return i
    return None

print(linear_search([2,3,4,5],3))