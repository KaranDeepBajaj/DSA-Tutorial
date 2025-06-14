class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        if (self.head is None):
            node=Node(data,self.head,self.head)
            self.head=node
            return
        self.head.prev=self.head
        node= Node(data,self.head,None)
        self.head=node

    def insert_at_end(self,data):
        if (self.head is None):
            node=Node(data,self.head,self.head)
            self.head=node
            return
        itr=self.head
        while itr.next:
             itr=itr.next
        node=Node(data,None,itr)
        itr.next=node
        return

    def print(self):
        itr =self.head
        strdll=""
        while itr:
            strdll+=str(itr.data)+"-->"
            itr=itr.next
        print(strdll)
        return

#     def print_forward(self):
#
#     # This method prints list in forward direction. Use node.next
#
#     def print_backward(self):
# # Print linked list in reverse direction. Use node.prev for this.

if __name__ == '__main__':
    dll=DoubleLinkedList()
    dll.insert_at_end(9)
    dll.insert_at_end(67)
    dll.print()