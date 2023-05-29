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
