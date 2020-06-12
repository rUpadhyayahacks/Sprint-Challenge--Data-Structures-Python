class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return None
        if node.get_next() ==  None:
            self.head = node
            self.head.next_node = prev
            return
        self.reverse_list(node.get_next(), node ) 
        # node gets passed in as the argument for previous
        node.next_node = prev
        # reverses the next pointer to the previous node

        # if node is None: 
        #     return None
        # if node.next_node is None:                 
        # #this is pointing to none return node 
        #     return node
        # c_head = node                              
        # # created a variable called current head and assigned it to Node 
        # n_head = c_head.next_node
        # f_head =self.reverse_list(n_head, None)
        # n_head.next_node = c_head
        # n_head = f_head
        # self.head = n_head
        # return n_head 