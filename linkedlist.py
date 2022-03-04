class Node:
    def __init__(self,data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):

        if(self.head is None):
            print("The linked list is empty")
            return

        itr = self.head
        llistr = ''

        while itr:
            llistr += str(itr.data) + '-->'
            itr = itr.next

        print(llistr)

    def insert_at_end(self,data):
        if self.head == None:
            node = Node(data,None)

        itr = self.head

        while itr.next:

            itr = itr.next

        
        node = Node(data,None)
        itr.next = node

    def insert_list(self,data_list):

        for val in data_list:
            self.insert_at_end(val)

    def get_length(self):

        itr = self.head
        len = 0
        while itr:
            len += 1
            itr = itr.next

        return len

    def remove_at(self,index):

        if index < 0 or index >= self.get_length():
            print("Index out of bound !!")
            return

        if index == 0:
            self.head = self.head.next #remove first element

        itr = self.head
        i = 0
        while i < index-1:
            i += 1
            itr = itr.next
            

        temp = itr.next.next
        itr.next = temp

        return

    def insert_at(self,index,data):

        if index<0 or index >= self.get_length():
            print("Index out of bound!")
            return

        if index == 0:
            self.insert_in_beginning(data)
            return

        if index == self.get_length() - 1:
            self.insert_at_end(data)
            return
        
        itr = self.head
        count = 0

        while count < index - 1:
            itr = itr.next
            count += 1

        node = Node(data,itr.next)

        itr.next = node

        return




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_in_beginning(23)
    ll.insert_in_beginning(24)
    ll.insert_at_end(50)
    ll.insert_at_end(60)
    ll.insert_list([1,2,3,4,5,6])
    ll.print()
    print(ll.get_length())
    #ll.remove_at(20)
    ll.insert_at(2,45)
    ll.print()

