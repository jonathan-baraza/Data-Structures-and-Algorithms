def merge_sort(list):
    """
     Sorts a list in ascending order
     Returns a new sorted list

     Divide: Find the midpoint of the list and divide into sublists
     Conquer: Recursively sort hte sublists created in previous step
     Combine: Merge the sorted sublists created in previous step

     Takes O(n log n) time (actual runtime after fixing the caveat)

     After caveat realization from split
     Takes O(Kn log n) time

     space complexity of merge sort is linear
    """

    if len(list)<=1:
        return list

    #fixing the caveat
    #use linear for splitting
    left_half,right_half=split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    :param list: a list
    :returns two sublists - left and right
    
    
    Takes overall  O(log n) time
    But there's a caveat
    Python's slice is not a constant time operation .
    hence:
    Takes overal O(K log n)
    """

    mid=len(list)//2
    left=list[:mid]
    right=list[mid:]

    return left,right

def merge(left,right):
    """
    Merges two list (array) sorting them in the process
    :return: Returns a new merged list

    Runs in overall O(n) time
    """
    l=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i] <right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i<len(left):
        l.append(left[i])
        i+=1
    while j<len(right):
        l.append(right[j])
        j+=1

    return l



def verify_sorted(list):
    n=len(list)
    if n==0 or n==1:
        return True
    return list[0]<list[1] and verify_sorted(list[1:])

alist=[54,26,62,93,17,77,31,44,50,20,1]

l=merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
