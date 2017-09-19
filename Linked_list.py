class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class Solution:
    def display(self , head):
        current = head
        while current:
            print( current.data , end=' ' )
            current = current.next

    def insert(self , head , data):
        # Complete this method
        new_node = Node( data )
        if head == None:
            self.head = new_node
        elif self.head.next == None:
            self.head.next = new_node
        else:
            tmp = self.head.next
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = new_node
        return self.head


mylist = Solution()
T = int( input() )
head = None
for i in range( T ):
    data = int( input() )
    head = mylist.insert( head , data )
mylist.display( head );
