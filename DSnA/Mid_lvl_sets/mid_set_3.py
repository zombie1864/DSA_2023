def prob_xx():
    '''  '''
    llist = LList() 
    llist.add_node(3)
    llist.add_node(5)
    llist.add_node(8)
    llist.add_node(5)
    llist.add_node(10)
    llist.add_node(2)
    llist.add_node(1)
    llist.sort_llist(5)
    llist.print_list()


class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.nxt = None


class LList():
    def __init__(self) -> None:
        self.head = None 

    def add_node(self, val): 
        '''  '''
        new_node = Node(val)
        curr_node = self.head 

        if self.head is None: 
            self.head = new_node 
            return 

        while curr_node.nxt is not None: # needed for more than 2 nodes 
            curr_node = curr_node.nxt 

        curr_node.nxt = new_node 

    def print_list(self): 
        '''  '''
        curr_node = self.head 
        while curr_node is not None: 
            print(curr_node.val, end=' -> ') 
            curr_node = curr_node.nxt 
        print('None')

    def sort_llist(self,piv):
        if self.head is None: 
            return

        # Initialize two partitions for nodes less than and greater than or equal to the pivot
        less_head    = less_tail     = Node(None)
        equal_head   = equal_tail    = Node(None)
        greater_head = greater_tail  = Node(None)
        curr_node    = self.head

        while curr_node is not None:
            next_node = curr_node.nxt  # Save the next node before modifying the current node

            if curr_node.val < piv:
                less_tail.nxt = curr_node # place curr_node at end of llist 
                less_tail = curr_node # moves pointer to curr_node which is also nxt node  
                '''  
                @ node = 3
                    t_0: less_head = less_tail: None 
                    t_1: less_head = less_tail: None->3
                    t_2: less_head = less_tail: 3->3
                @ node = 2
                    t_4: less_head = less_tail: 3->3->2
                    t_5: less_head = less_tail: 3->2->2 
                @ node = 1
                    t_6: less_head = less_tail: 3->2->2->1
                    t_7: less_head = less_tail: 3->2->1->1
                '''
            elif curr_node.val == piv:
                equal_tail.nxt = curr_node
                equal_tail = curr_node
                '''  
                @ node = 5 
                    t_0: equal_head = equal_tail: None
                    t_1: equal_head = equal_tail: None->5
                    t_2: equal_head = equal_tail: 5->5

                @ node = 5
                    t_3: equal_head = equal_tail: 5->5->5
                    t_4: equal_head = equal_tail: 5->5->5
                '''
            else:
                greater_tail.nxt = curr_node
                greater_tail = curr_node
                greater_tail.nxt = None  # Set the next pointer of the greater tail to None to avoid cycles

            curr_node = next_node  # Move to the next node

        # Connect the three partitions
        less_tail.nxt = equal_head.nxt # 3->2->1->[1] turns to 3->2->1->5->5; head = tail 
        equal_tail.nxt = greater_head.nxt

        # Update the head of the linked list
        self.head = less_head.nxt