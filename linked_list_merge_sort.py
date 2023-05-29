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
        """assign the head of the right list to be the node after the mid node"""
        right_half.head(midNode.next_node)
        midNode.next_node=None

        return left_half,right_half


def merge(left,right):
    """
    Merges two linked list, sorting by data in nodes
    :return: a new merged list
    """

    #create a new linked list that contains nodes from merging left and right

    merged=LinkedList()

    #add a fake head that is discarded later
    merged.add(0)
    #set current to head of linked list
    current=merged.head

    #obtain head nodes from left and right linked lists
    left_head=left.head
    right_head=right.head

    #iterate over left and write untile we reach the tail node of either

    while left_head or right_head:
        #If the head node of head is None, we are past the tail.
        #Add the node from right to merged linked list
        if left_head is None:
            current.next_node=right_head
            #call next on right to set loop condition to False
            right_head=right_head.next_node
        #If the head node of right is None, we're past the tail
        #ADd the tail node from left to merged linked list
        elif right_head is None:
            current.next_node=left_head
            #call next on left to set loop condition to False
            left_head=left_head.next_node
        else:
            #Not at either tail node
            #Obtain node data to perform comparison operations
            left_data=left_head.data
            right_data=right_head.data

            #if data on left is less than right, set current to left node

            if left_data<right_data:
                current.next_node=left_head
                #move left head to next node
                left_head=left_head.next_node
            #If data on left if greater than right set current to right node
            else:
                current.next_node=right_head
                #move right head to next node
                right_head=right_head.next_node

