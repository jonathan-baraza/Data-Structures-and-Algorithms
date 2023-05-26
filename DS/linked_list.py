class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data=None
    next_node=None

    def __init__(self,data):
        self.data=data

    def __repr__(self):
        return "<Node data: %s>" % self.data



class LinkedList:
    """
    Singly linked list
    """
    head=None
    def __int__(self):
        self.head=None

    # def __repr__(self):
    #     return "<Linked list with %s items>" % self.size()



    def is_empty(self):
        return self.head==None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) i.e. linear time
        :return:
        """
        current=self.head
        count=0

        while current:
            count+=1
            current=current.next_node
        return count

    def add(self,data):
        """
        Adds new Node containing data at the head of the list
        Takes O(n) time i.e. constant time
        """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node


    # def search(self,key):
    #     """
    #     Returns index of the value being searched for
    #     """
    #     found=None
    #     index=0
    #     current=self.head;
    #     while current:
    #         if current.data == key:
    #             found=index
    #         current=current.next_node
    #         index+=1
    #     return found
    def search(self,key):
        current=self.head
        while current:
            if current.data == key:
                return current
            else:
                current=current.next_node
            return None
    def __repr__(self):
        """
        Returns a string representation of the list
        Takes 0(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return "->".join(nodes)




l=LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)

print(l.search(3))