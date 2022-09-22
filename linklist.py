#class node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#class link list
class LinkedList:
    def __init__(self):
        self.head = None
    #traverse node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    #add new node at front
    def push(self,new_data):
        #1 & 2 allocate a new node and put in the data
        new_node = Node(new_data)
        #3 make next of new node as Head
        new_node.next = self.head
        #4 move to the head poin to new node
        self.head = new_node
    def insertAfter(self, prev_node,new_data):
        if prev_node is None:
            print('Previous node must in the list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node









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

    llist.push(4)
    print('after push node')
    llist.printList()
    prev_node = Node(6)
    print(prev_node.next)
    print('after insert specific location node',llist.head.next)
    llist.insertAfter(llist.head.next, 5)
    llist.printList()