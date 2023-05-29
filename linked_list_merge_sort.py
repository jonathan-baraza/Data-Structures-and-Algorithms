from DS.linked_list import LinkedList,Node

def merge_sort(linked_list):
    """
    This function sorts a linked list in ascending order
    -Recursively divide the linked list into sublists containing a single node
    -Repeatedly merge the sublist to produce sorted sublists until one remains

    :param linked_list:
    :return: a sorted linked list
    """

    if linked_list.size()==1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half,right_half=split(linked_list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right)


def split (linked_list):
    """
    divide the unsorted list at midpoint into sublinkedlist
    :param linked_list:
    :return:
    """

    if linked_list==None or linked_list.head is None:
        #Assuming we are splitting a linked list with a single node
        left_half=linked_list
        right_half=None
        return left_half,right_half
    else:
        size=linked_list.size()
        midpoint=size//2

        midNode=linked_list.node_at_index(midpoint-1)
        left_half=linked_list
        right_half=LinkedList()
        #assign the head of the right list to be the node after the mid node
        right_half.head(midNode.next_node)
        midNode.next_node=None

        return left_half,right_half
