# Push file project to Github
# git remote add origin https://github.com/jfields82/Linked_list.git
# git branch -M master
# git push -u origin master

# echo "# test" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M master
# git remote add origin https://github.com/jfields82/Linked_list.git
# git push -u origin master
# Run code in VS - Ctrl + F5

# Created a Node class to call this Node for each method. 
class Node:
    def __init__(self, value):
# The value is passed to a specific instance of Node.
        self.value = value
        self.next = None
        
# Node will called the new class. 
# Create first linked list Constructor
# Pass the value to create the Node
# Creating a head and tail to the linked list
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.leghth = 1
# print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Append a item to the end of a list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
    #   if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.leghth += 1
        return True
        




# Creating a new linked list and calling the linked list class.
# It assigns the value 4 to that new node.
my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()

print(my_linked_list.head.value)