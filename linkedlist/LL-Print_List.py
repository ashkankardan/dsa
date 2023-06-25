# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#         return True

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def print_length(self):
        print('length', self.length)

    def append(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if(self.length == 0):
            return None

        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if(self.length == 0):
            self.head = None
            self.tail = None

        return temp

        # if(self.length == 0):
        #     return
        # elif(self.length == 1):
        #     self.head = None
        #     self.tail = None
        #     self.length = 0
        # else:
        #     temp = self.head
        #     for _ in range(self.length - 2):
        #         temp = temp.next

        #     temp.next = None
        #     self.tail = None
        #     self.length -= 1
        # return True



my_linked_list = LinkedList(11)
my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()
# my_linked_list.print_length()

# my_linked_list.pop()

# my_linked_list.print_list()
# my_linked_list.print_length()

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
