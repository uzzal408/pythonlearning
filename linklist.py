#class node
class Node:
    def __int__(self, data):
        self.data = data
        self.next = None
#class link list
class LinkedList:
    def __int__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    #start with empty list
    llist = LinkedList()

    #create node
    llist.head = Node(1)
    second = Node(2)
    third  = Node(3)
    ''' 3 node has been created We have references to these 3 blocks as head
     second, third
     '''

    llist.head.next = second
    second.next     = third

    llist.printList()