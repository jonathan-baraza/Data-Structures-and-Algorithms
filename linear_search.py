def linear_search(list,target):
    """
    Returns the index position of the target it found, else returns None
    """
    # print(list.index(target))
    x=0;
    while(x<len(list)):
        if(list[x]==target):
            break;
        x=x+1
    print(x)


linear_search([2,3,4,5],2)