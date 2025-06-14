class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head= None
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        len = 0
        itr=self.head
        while itr:
            len+=1
            itr = itr.next
        return(len)

    def print(self):
        if self.head is None:
            print("Linked List Is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr +=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def remove_at(self,index):
        if (index<0 or index>=self.get_length()):
            raise Exception ("Invalid Index")
        elif (index==0):
            self.head=self.head.next
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:
                    itr.next=itr.next.next
                itr=itr.next
                count+=1
                return

    def insert_at(self,index,data):
        if (index<0 or index>=self.get_length()):
            raise Exception ("Invalid Index")
        elif (index==0):
            self.insert_at_begining(data)
            return
        else:
            itr=self.head
            count=0
            while itr:
                if (count == index-1):
                    dt=Node(data,itr.next)
                    itr.next=dt
                    break
                itr=itr.next
                count +=1

    def insert_after_value(self, data_after, data_to_insert):
        itr=self.head
        count=0
        while itr:
            if (itr.data==data_after):
                node=Node(data_to_insert,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
            if (count==self.get_length()):
                raise Exception ("Invalid Entires")

    def remove_by_value(self, data):
        if (self.head is None):
            return
        elif(self.head.data==data):
            self.head=self.head.next
            return
        itr=self.head
        while itr:
            if (itr.next.data==data):
                itr.next=itr.next.next
                return
            itr=itr.next




if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_values(["Karan", "Deep","Bajaj","Is","Good"])
    ll.print()
    i=ll.get_length()
    print(i)
    ll.remove_at(0)
    ll.print()
    ll.insert_at(2,"Mr")
    ll.insert_after_value("Karan","Very")
    ll.remove_by_value("Bajaj")
    ll.print()
